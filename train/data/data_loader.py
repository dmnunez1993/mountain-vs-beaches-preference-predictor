import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads the data from a CSV.

    Args:
        file_path (str): The file path.
    Returns:
        pd.DataFrame: A dataframe with the loaded data
    """
    return pd.read_csv(file_path)
