import logging

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

logger = logging.getLogger("mountain_vs_beaches_preference_training")


def _create_preprocessor() -> ColumnTransformer:
    return ColumnTransformer(
        transformers=[
            (
                "ordinal",
                OrdinalEncoder(
                    categories=[
                        [
                            "high school",
                            "bachelor",
                            "master",
                            "doctorate",
                        ],    # Categories for Education_Level
                        [
                            "18-25",
                            "25-40",
                            "40-65",
                            "65+",
                        ],    # Categories for Age_Range
                    ]
                ),
                ("Education_Level", "Age_Range"),
            ),
            (
                "onehot",
                OneHotEncoder(handle_unknown="ignore", sparse_output=False),
                (
                    "Gender",
                    "Preferred_Activities",
                    "Location",
                    "Favorite_Season",
                ),
            )
        ],
        remainder="passthrough"
    )


def train_model(x_train: pd.DataFrame, y_train: pd.Series) -> Pipeline:
    """
    Trains a Logistic Regression Prediction Model.

    Args:
        X_train (pd.DataFrame): Dataframe with the independent variables.
        y_train (pd.Series): Series with the target values.

    Returns:
        Pipeline: Trained model with preprocessing included.
    """
    preprocessor = _create_preprocessor()
    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),    # Preprocessor
            (
                "model",
                LogisticRegression(
                    C=1000,
                    solver='lbfgs',
                    max_iter=30000,
                    tol=1e-4,
                    random_state=42,
                )
            ),    # Logistic regression model
        ]
    )

    logger.info("Training Logistic Regression Model...")
    model.fit(x_train, y_train)

    return model
