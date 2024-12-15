from typing import List, Dict, Any

from fastapi.routing import APIRouter
import pandas as pd
from pydantic import validator
from sqlalchemy import func, select, or_, desc

from database.connection import db
from database.models.dataset import dataset
from database.models.model_metrics import model_metrics
from database.models.predictions import predictions

from api.models.base import BaseModel
from prediction_model.model import (
    prediction_model,
)

router = APIRouter()


class _PredictionRequest(BaseModel):
    age_range: str
    gender: str
    income: int
    education_level: str
    travel_frequency: int
    preferred_activities: str
    vacation_budget: int
    location: str
    proximity_to_mountains: int
    proximity_to_beaches: int
    favorite_season: str
    pets: bool
    environmental_concerns: bool | None
    preference: bool | None

    @validator("age_range")
    @classmethod
    def validate_age_range(cls, v):
        possibilities = ['40-65', '65+', '25-40', '18-25']
        if v not in possibilities:
            raise ValueError(f"Age range must be one of: {str(possibilities)}")

        return v

    @validator("gender")
    @classmethod
    def validate_gender(cls, v):
        possibilities = ['male', 'female', 'non-binary']
        if v not in possibilities:
            raise ValueError(f"Gender must be one of: {str(possibilities)}")

        return v

    @validator("education_level")
    @classmethod
    def validate_education_level(cls, v):
        possibilities = ['bachelor', 'master', 'high school', 'doctorate']
        if v not in possibilities:
            raise ValueError(
                f"education_level must be one of: {str(possibilities)}"
            )

        return v

    @validator("preferred_activities")
    @classmethod
    def validate_preferred_activities(cls, v):
        possibilities = ['skiing', 'swimming', 'hiking', 'sunbathing']
        if v not in possibilities:
            raise ValueError(
                f"preferred_activities must be one of: {str(possibilities)}"
            )

        return v

    @validator("location")
    @classmethod
    def validate_location(cls, v):
        possibilities = ['urban', 'suburban', 'rural']
        if v not in possibilities:
            raise ValueError(f"location must be one of: {str(possibilities)}")

        return v

    @validator("favorite_season")
    @classmethod
    def validate_favorite_season(cls, v):
        possibilities = ['summer', 'fall', 'winter', 'spring']
        if v not in possibilities:
            raise ValueError(
                f"favorite_season must be one of: {str(possibilities)}"
            )

        return v


class _PredictionResponseData(BaseModel):
    prediction: bool
    real_value: bool | None
    probabilities: List[float]


class _PredictionResponse(BaseModel):
    status: str
    data: List[_PredictionResponseData]


class _ErrorResponse(BaseModel):
    status: str
    detail: str


def _prediction_requests_to_df(requests: List[Dict[str, Any]]):
    request_list = []

    for request in requests:
        request_list.append(request.model_dump())
    request_df = pd.DataFrame(request_list)
    request_df.rename(
        columns={
            "age_range": "Age_Range",
            "gender": "Gender",
            "income": "Income",
            "education_level": "Education_Level",
            "travel_frequency": "Travel_Frequency",
            "preferred_activities": "Preferred_Activities",
            "vacation_budget": "Vacation_Budget",
            "location": "Location",
            "proximity_to_mountains": "Proximity_to_Mountains",
            "proximity_to_beaches": "Proximity_to_Beaches",
            "favorite_season": "Favorite_Season",
            "pets": "Pets",
            "environmental_concerns": "Environmental_Concerns",
            "preference": "Preference"
        },
        inplace=True,
    )

    return request_df


@router.post(
    "/predict/",
    response_model=_PredictionResponse | _ErrorResponse,
)
async def predict_endpoint(prediction_requests: List[_PredictionRequest]):
    data = []
    if len(prediction_requests) == 0:
        return {
            "status": "error",
            "detail": "Must provide at least more than 1 sample"
        }
    request_df = _prediction_requests_to_df(prediction_requests)

    x, y = prediction_model.split_x_y(request_df)

    y_pred = await prediction_model.predict_async(x)
    y_pred_proba = await prediction_model.predict_proba_async(x)

    for y_curr, proba_curr, y_real_curr in zip(y_pred, y_pred_proba, y):
        data.append(
            {
                "prediction": y_curr,
                "real_value": y_real_curr,
                "probabilities": proba_curr
            }
        )

    x_rows = x.to_dict(orient="records")

    new_dataset_rows = []
    new_prediction_rows = []

    for (
        x_row_curr,
        y_real_curr,
        y_pred_curr,
        y_pred_proba_curr,
    ) in zip(
        x_rows,
        y,
        y_pred,
        y_pred_proba,
    ):
        if y_real_curr is not None:
            new_dataset_row = {**x_row_curr, "preference": y_real_curr}
            new_dataset_row_correct_names = {}

            for key, value in new_dataset_row.items():
                new_dataset_row_correct_names[key.lower()] = value
            new_dataset_rows.append(new_dataset_row_correct_names)

        new_prediction_row = {
            **x_row_curr,
            "preference": y_real_curr,
            "preference_prediction": y_pred_curr,
            "preference_prediction_probabilities": y_pred_proba_curr,
        }
        new_prediction_row_correct_names = {}
        for key, value in new_prediction_row.items():
            new_prediction_row_correct_names[key.lower()] = value
        new_prediction_rows.append(new_prediction_row_correct_names)

    async with db.transaction():
        q1 = dataset.insert(new_dataset_rows)
        await db.execute(q1)
        q2 = predictions.insert(new_prediction_rows)
        await db.execute(q2)

    return {"status": "success", "data": data}


class _MetricsData(BaseModel):
    model_name: str | None
    accuracy: float | None
    precision: float | None
    recall: float | None
    f1_score: float | None
    roc_auc: float | None
    precision_false: float | None
    recall_false: float | None
    f1_score_false: float | None
    precision_true: float | None
    recall_true: float | None
    f1_score_true: float | None
    conf_matrix_0_0: int | None
    conf_matrix_0_1: int | None
    conf_matrix_1_0: int | None
    conf_matrix_1_1: int | None


class _MetricsResponse(BaseModel):
    status: str
    data: _MetricsData


@router.get(
    "/metrics/",
    response_model=_MetricsResponse | _ErrorResponse,
)
async def metrics_endpoint():
    metrics = {
        "model_name": None,
        "accuracy": None,
        "precision": None,
        "recall": None,
        "f1_score": None,
        "roc_auc": None,
        "precision_false": None,
        "recall_false": None,
        "f1_score_false": None,
        "precision_true": None,
        "recall_true": None,
        "f1_score_true": None,
        "conf_matrix_0_0": None,
        "conf_matrix_0_1": None,
        "conf_matrix_1_0": None,
        "conf_matrix_1_1": None,
    }

    q = select(model_metrics).order_by(model_metrics.c.id.desc()).limit(1)

    rows = await db.fetch_all(q)
    rows = [dict(row) for row in rows]
    if len(rows) > 0:
        metrics = rows[0]
        metrics.pop("id")
        metrics.pop("created_at")
        metrics.pop("updated_at")

    return {"status": "success", "data": metrics}
