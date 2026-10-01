import pandas as pd
from typing import List


def load_data(url: str) -> pd.DataFrame:
    """Load a CSV dataset from a URL."""
    try:
        # Read the CSV file into a Pandas DataFrame
        return pd.read_csv(url)
    except Exception as e:
        # Provide a clear error if the dataset cannot be loaded
        raise RuntimeError(f"Failed to load dataset: {e}")


def validate_columns(df: pd.DataFrame, required_columns: List[str]) -> None:
    """Check that all required columns exist in the dataset."""

    # Identify any columns that are missing from the dataset
    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )


def calculate_average(df: pd.DataFrame, column: str) -> float:
    """Return the average value of a specified numeric column."""

    # Make sure the requested column exists
    validate_columns(df, [column])

    # Prevent calculations on an empty dataset
    if df.empty:
        raise ValueError("Dataset cannot be empty.")

    # Make sure the selected column contains numeric data
    if not pd.api.types.is_numeric_dtype(df[column]):
        raise TypeError(f"Column '{column}' must contain numeric values.")

    return df[column].mean()


def find_max(df: pd.DataFrame, column: str) -> float:
    """Return the maximum value from a specified numeric column."""

    # Check that the column exists before performing the calculation
    validate_columns(df, [column])

    if df.empty:
        raise ValueError("Dataset cannot be empty.")

    # Confirm that the column can be used for a numeric calculation
    if not pd.api.types.is_numeric_dtype(df[column]):
        raise TypeError(f"Column '{column}' must contain numeric values.")

    return df[column].max()


def filter_by_value(
    df: pd.DataFrame,
    column: str,
    value: str
) -> pd.DataFrame:
    """Return rows where a column matches a specified value."""

    # Check that the column exists before filtering
    validate_columns(df, [column])

    # Return only rows that match the requested value
    return df[df[column] == value]


def main() -> None:
    """Run the data analysis workflow."""

    # Dataset used for the classroom activity
    url = (
        "https://raw.githubusercontent.com/"
        "mwaskom/seaborn-data/master/iris.csv"
    )

    # Load the dataset
    df = load_data(url)

    # Make sure all columns required for our analysis are available
    validate_columns(
        df,
        ["sepal_length", "petal_width", "species"]
    )

    # Calculate and display the average sepal length
    average_sepal_length = calculate_average(
        df, "sepal_length"
    )
    print("Average sepal length:", average_sepal_length)

    # Find and display the maximum petal width
    max_petal_width = find_max(df, "petal_width")
    print("Max petal width:", max_petal_width)

    # Filter the dataset to show only the Setosa species
    setosa = filter_by_value(
        df, "species", "setosa"
    )

    print("\nSetosa rows:")
    print(setosa.head())


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()