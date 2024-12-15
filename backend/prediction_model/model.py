import pathlib

from asyncio import get_running_loop

import joblib
import pandas as pd

PREDICTION_COLUMNS = [
    # Numerical
    "Income",
    "Travel_Frequency",
    "Vacation_Budget",
    "Proximity_to_Mountains",
    "Proximity_to_Beaches",

    # Categorical
    "Gender",
    "Education_Level",
    "Preferred_Activities",
    "Location",
    "Favorite_Season",
    "Age_Range",

    # Boolean
    "Pets",
    "Environmental_Concerns"
]

OUTPUT_COLUMN = "Preference"


class PredictionModelNotLoadedException(Exception):
    pass


class PredictionModel:
    def __init__(self):
        self._model = None

    def load_model(self):
        path = (pathlib.Path(__file__).parent / "lr.pkl").resolve()
        self._model = joblib.load(path)

    async def load_model_async(self):
        loop = get_running_loop()

        await loop.run_in_executor(None, self.load_model)

    def split_x_y(self, df: pd.DataFrame):
        return df[PREDICTION_COLUMNS], df[OUTPUT_COLUMN]

    def predict(self, x):
        if self._model is None:
            raise PredictionModelNotLoadedException("Model not loaded yet!")

        return self._model.predict(x)

    async def predict_async(self, x):
        loop = get_running_loop()

        return await loop.run_in_executor(None, self.predict, x)

    def predict_proba(self, x):
        if self._model is None:
            raise PredictionModelNotLoadedException("Model not loaded yet!")

        return self._model.predict_proba(x)

    async def predict_proba_async(self, x):
        loop = get_running_loop()

        return await loop.run_in_executor(None, self.predict_proba, x)

    def get_model(self):
        return self._model


prediction_model = PredictionModel()
