import logging

import joblib
from sklearn.base import BaseEstimator

logger = logging.getLogger("mountain_vs_beaches_preference_training")


def save_model(model: BaseEstimator, output_path: str) -> None:
    """
    Saves the model using joblib.

    Args:
        model: The model to be saved.
        output_path: The path to save the model to.
    """
    logger.info("Saving model...")
    joblib.dump(model, output_path)
    logger.info("Model saved at %s", output_path)
