import pandas as pd

def fill_missing_values(dataframe, strategy='mean', columns=None):
    """Fill missing values in specified columns based on a defined strategy."""
    if columns is None:
        columns = dataframe.columns
    for column in columns:
        if dataframe[column].dtype == 'float64' or dataframe[column].dtype == 'int64':
            if strategy == 'mean':
                fill_value = dataframe[column].mean()
            elif strategy == 'median':
                fill_value = dataframe[column].median()
            elif strategy == 'zero':
                fill_value = 0
            else:
                continue
            dataframe[column] = dataframe[column].fillna(fill_value)
        else:
            dataframe[column] = dataframe[column].fillna('Unknown')
    return dataframe

def remove_duplicates(dataframe, subset=None):
    """Remove duplicate rows from the DataFrame based on specified subset of columns."""
    return dataframe.drop_duplicates(subset=subset)

def standardize_case(dataframe, columns=None):
    """Standardize the text to lower case for specified columns."""
    if columns is None:
        columns = dataframe.columns
    for column in columns:
        if dataframe[column].dtype == 'object':
            dataframe[column] = dataframe[column].str.lower()
    return dataframe

# Example usage
if __name__ == "__main__":
    # Example DataFrame
    data = pd.DataFrame({
        'A': [1, 2, None, 4, 4],
        'B': ['Apple', 'banana', 'Grape', 'apple', None]
    })

    # Fill missing values
    filled_data = fill_missing_values(data)
    print("Data after filling missing values:")
    print(filled_data)

    # Remove duplicates
    unique_data = remove_duplicates(filled_data, subset=['A'])
    print("\nData after removing duplicates:")
    print(unique_data)

    # Standardize case
    standardized_data = standardize_case(unique_data, columns=['B'])
    print("\nData after standardizing case:")
    print(standardized_data)
