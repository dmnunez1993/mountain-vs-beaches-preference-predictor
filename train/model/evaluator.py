import logging

import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)
from sklearn.base import BaseEstimator

logger = logging.getLogger("mountain_vs_beaches_preference_training")


def evaluate_model(
    model: BaseEstimator,
    x_test: pd.DataFrame,
    y_test: pd.Series,
) -> tuple[float, float, float, float, float]:
    """
    Evaluates the prediction model.

    Args:
        model (BaseEstimator): A scikit learn model already fitted.
        x_test (pd.DataFrame): The test data to perform the predictions.
        y_test (pd.Series): The expected outputs.
    Returns:
        tuple[float, float, float, float, float]: Accuracy, Precision, Recall, F1, AUC
    """
    logger.info("Evaluating model...")
    y_pred = model.predict(x_test)
    y_prob = model.predict_proba(x_test)[:, 1]
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)
    logger.info("Linear Regression model metrics:")
    logger.info("Accuracy: %.2f", accuracy)
    logger.info("Precision: %.2f", precision)
    logger.info("Recall: %.2f", recall)
    logger.info("F1: %.2f", f1)
    logger.info("AUC: %.2f", auc)

    return accuracy, precision, recall, f1, auc
