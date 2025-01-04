from typing import Any

import logging

import pandas as pd

logger = logging.getLogger("mountain_vs_beaches_preference_training")


def _convert_value_to_boolean(x: Any):
    if x in [0, 0.0, "false", "no", "no"]:
        return False

    if x in [1, 1.0, "true", "yes", "si"]:
        return True

    return x


def _convert_columns_to_boolean(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    potentially_boolean_values = [
        set([0, 1]),
        set([0.0, 1.0]),
        set(["false", "true"]),
        set(["no", "yes"]),
        set(["no", "si"]),
    ]

    columns = out.columns.tolist()
    converted_columns = []

    for column in columns:
        unique_values = out[column].dropna().unique()

        boolean_column_found = False

        if len(unique_values) == 2:
            logger.debug(
                "Unique values for column '%s': %s", column, str(unique_values)
            )

        for boolean_values_possibility in potentially_boolean_values:
            if set(unique_values) == boolean_values_possibility:
                logger.debug("Column '%s' is boolean. Converting.", column)
                out[column] = out[column].apply(_convert_value_to_boolean
                                               ).astype("bool")

                boolean_column_found = True
                break

        if boolean_column_found:
            converted_columns.append(column)

    logger.debug("Columns converted to boolean: %s", str(converted_columns))

    return out


def _clean_string(string):
    if isinstance(string, str):
        # 1. Convertir todo a minúsculas
        string = string.lower()
        string = string.strip()

        return string
    return string


def _convert_columns_to_categorical(
    df: pd.DataFrame,
    max_percentage_categorical_column: float = 0.10,
):
    out = df.copy()

    potential_categorical_columns = df.select_dtypes(
        include=[
            'string',
            'object',
        ]
    ).columns.tolist()
    converted_columns_to_categorical = []
    converted_columns_to_string = []

    for column in potential_categorical_columns:
        out[column] = out[column].apply(_clean_string)

    for column in potential_categorical_columns:
        unique_values = out[column].dropna().unique().tolist()
        logger.debug(
            "Amount of unique values for column '%s': %d",
            column,
            len(unique_values),
        )

        if len(unique_values
              ) <= max_percentage_categorical_column * out.shape[0]:
            logger.debug(
                "Unique values for column '%s': %s",
                column,
                str(unique_values),
            )
            logger.debug("Converting column '%s' to categorical.", column)
            out[column] = out[column].astype("category")
            converted_columns_to_categorical.append(column)
        else:
            logger.debug(
                "Column '%s' not categorical. Converting to string.",
                column,
            )
            out[column] = out[column].astype("string")
            converted_columns_to_string.append(column)

    logger.debug(
        "Columns converted to categorical: %s",
        str(converted_columns_to_categorical),
    )

    logger.debug(
        "Columns converted to string: %s",
        str(converted_columns_to_string),
    )

    return out


def _convert_age_to_age_range(x):
    if 0 <= x < 18:
        return "0-18"

    if 18 <= x < 25:
        return "18-25"

    if 25 <= x < 40:
        return "25-40"

    if 40 <= x < 65:
        return "40-65"

    return "65+"


def _add_age_range(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["Age_Range"] = out["Age"].apply(_convert_age_to_age_range
                                       ).astype("category")

    return out


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the data:
    
    Args:
        data (pd.DataFrame): DataFrame with the data to be processed.

    Returns:
        pd.DataFrame: DataFrame with the preprocessed data.
    """
    logger.info("Preprocessing data...")
    out = _convert_columns_to_boolean(df)
    out = _convert_columns_to_categorical(out)
    out = _add_age_range(out)

    return out
