import asyncio
import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix,
)

from logger import logger

from database.connection import db
from database.models.dataset import dataset
from database.models.model_metrics import model_metrics
from prediction_model.model import prediction_model

if os.path.isfile(".env"):
    print("Loading env file...")
    load_dotenv(".env")


def _db_rows_to_df(rows):
    db_df = pd.DataFrame(rows)

    column_mapping = {
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
    }

    for column in db_df.columns.tolist():
        if column not in column_mapping:
            db_df.drop(column, axis=1, inplace=True)

    db_df.rename(
        columns=column_mapping,
        inplace=True,
    )

    return db_df


async def evaluate_model_performance():
    logger.info("Evaluating model performance...")
    await db.connect()
    q = dataset.select()

    rows = await db.fetch_all(q)
    rows = [dict(row) for row in rows]

    db_df = _db_rows_to_df(rows)

    x, y = prediction_model.split_x_y(db_df)

    y_pred = await prediction_model.predict_async(x)
    y_pred_proba = await prediction_model.predict_proba_async(x)

    accuracy_score_lr = accuracy_score(y, y_pred)
    precision_score_lr = precision_score(y, y_pred)
    recall_score_lr = recall_score(y, y_pred)
    f1_score_lr = f1_score(y, y_pred)
    roc_auc_score_lr = roc_auc_score(y, y_pred_proba[:, 1])
    classification_report_lr = classification_report(
        y,
        y_pred,
        output_dict=True,
    )
    confusion_matrix_lr = confusion_matrix(y, y_pred)

    logger.info("LR Accuracy: %.2f", accuracy_score_lr)
    logger.info("LR Precision: %.2f", precision_score_lr)
    logger.info("LR Recall: %.2f", recall_score_lr)
    logger.info("LR F1 Score: %.2f", f1_score_lr)
    logger.info("LR ROC AUC Score: %.2f", roc_auc_score_lr)
    logger.info("LR Classification Report: %s", str(classification_report_lr))
    logger.info("LR Confusion Matrix: %s", str(confusion_matrix_lr))

    new_model_metrics = {
        "model_name": "Logistic Regression",
        "accuracy": accuracy_score_lr,
        "precision": precision_score_lr,
        "recall": recall_score_lr,
        "f1_score": f1_score_lr,
        "roc_auc": roc_auc_score_lr,
        "precision_false": classification_report_lr["False"]["precision"],
        "recall_false": classification_report_lr["False"]["recall"],
        "f1_score_false": classification_report_lr["False"]["f1-score"],
        "precision_true": classification_report_lr["True"]["precision"],
        "recall_true": classification_report_lr["True"]["recall"],
        "f1_score_true": classification_report_lr["True"]["f1-score"],
        "conf_matrix_0_0": confusion_matrix_lr[0][0],
        "conf_matrix_0_1": confusion_matrix_lr[0][1],
        "conf_matrix_1_0": confusion_matrix_lr[1][0],
        "conf_matrix_1_1": confusion_matrix_lr[1][1],
    }

    query = model_metrics.insert([new_model_metrics])

    await db.execute(query)

    await db.disconnect()


def main():
    logger.info("Staring Model Evaluation Scheduler...")
    prediction_model.load_model()
    scheduler = AsyncIOScheduler()

    scheduler.add_job(evaluate_model_performance, 'interval', hours=1)

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        scheduler.start()
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == '__main__':
    main()
