import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(
    df: pd.DataFrame,
    independent_columns: list[str],
    target_column: str,
    test_size: float = 0.3,
    random_state: int = 42
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Splits the dataset in train and test sets

    Args:
        df (pd.DataFrame): DataFrame containing the data to be split.
        independent_columns (list of str): Names of the independent columns.
        target_column (str): Name of the target column.
        test_size (float, optional): Proportion of that used for test. Defaults to 0.3
        random_state (int, optional): Random seed. Defaults to 42.
    Returns:
        Tuple: A tuple containing the sets for train and tests.
        - X_train (pd.DataFrame): Train set containing independent variables
        - X_test (pd.DataFrame): Test set containing independent variables
        - y_train (pd.Series): Train set containing the target variable
        - y_test (pd.Series): Test set containing the target variable.
    """
    x = df[independent_columns]
    y = df[target_column]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=test_size, random_state=random_state
    )

    return x_train, x_test, y_train, y_test
