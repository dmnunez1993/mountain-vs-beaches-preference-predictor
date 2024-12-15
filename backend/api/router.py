from typing import List, Dict, Any

from fastapi.routing import APIRouter
import pandas as pd
from pydantic import validator

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

    return {"status": "success", "data": data}
