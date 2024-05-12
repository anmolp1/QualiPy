import pandas as pd

def calculate_completeness(dataframe):
    """Calculate the completeness of each column in the dataframe."""
    total_cells = dataframe.size
    missing_cells = dataframe.isnull().sum().sum()
    completeness_score = 1 - (missing_cells / total_cells)
    return completeness_score

def calculate_uniqueness(dataframe):
    """Calculate the uniqueness of each column in the dataframe."""
    uniqueness_scores = {}
    for column in dataframe.columns:
        total_rows = dataframe.shape[0]
        unique_rows = dataframe[column].nunique()
        uniqueness_score = unique_rows / total_rows
        uniqueness_scores[column] = uniqueness_score
    return uniqueness_scores

def calculate_accuracy(dataframe, reference_data):
    """Calculate the accuracy of data in dataframe compared to a reference dataset."""
    # This is a simple example where we assume both dataframes are aligned and have the same columns.
    accuracy_scores = {}
    for column in dataframe.columns:
        if column in reference_data.columns:
            matched_records = (dataframe[column] == reference_data[column]).sum()
            total_records = dataframe.shape[0]
            accuracy_score = matched_records / total_records
            accuracy_scores[column] = accuracy_score
    return accuracy_scores

# Example usage
if __name__ == "__main__":
    # Example DataFrame
    data = pd.DataFrame({
        'A': [1, 2, None, 4],
        'B': ['a', 'b', 'b', 'c']
    })
    
    reference_data = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': ['a', 'b', 'c', 'c']
    })

    # Calculate completeness
    completeness = calculate_completeness(data)
    print(f"Completeness Score: {completeness:.2f}")

    # Calculate uniqueness
    uniqueness = calculate_uniqueness(data)
    print("Uniqueness Scores:", uniqueness)

    # Calculate accuracy
    accuracy = calculate_accuracy(data, reference_data)
    print("Accuracy Scores:", accuracy)
