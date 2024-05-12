import matplotlib.pyplot as plt

def plot_data_quality_scores(scores, title='Data Quality Scores'):
    """Plot bar chart of data quality scores."""
    categories = list(scores.keys())
    values = list(scores.values())
    plt.figure(figsize=(10, 5))
    plt.bar(categories, values, color='skyblue')
    plt.xlabel('Data Quality Metrics')
    plt.ylabel('Scores')
    plt.ylim(0, 1)  # Assuming scores are between 0 (worst) and 1 (best)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_missing_data(dataframe, title='Missing Data Visualization'):
    """Plot missing data percentages for each column in a DataFrame."""
    missing_data = (dataframe.isnull().sum() / len(dataframe)) * 100
    missing_data = missing_data[missing_data > 0]
    missing_data.sort_values(inplace=True)
    plt.figure(figsize=(10, 5))
    missing_data.plot(kind='barh', color='salmon')
    plt.xlabel('Percentage of Missing Data (%)')
    plt.title(title)
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    import pandas as pd
    import numpy as np
    
    # Creating a sample DataFrame with missing values and duplicates
    data = pd.DataFrame({
        'A': [np.nan, 1, 2, 3, 4, 5, np.nan],
        'B': ['x', 'y', 'z', 'z', 'y', np.nan, 'x'],
        'C': [25, 50, np.nan, np.nan, 25, 75, 50]
    })

    # Calculate data quality scores for demonstration
    completeness_score = 1 - (data.isnull().sum().sum() / data.size)
    uniqueness_scores = {'A': data['A'].nunique() / len(data['A'].dropna()), 
                         'B': data['B'].nunique() / len(data['B'].dropna()),
                         'C': data['C'].nunique() / len(data['C'].dropna())}

    # Plot data quality scores
    plot_data_quality_scores({'Completeness': completeness_score, **uniqueness_scores})

    # Plot missing data visualization
    plot_missing_data(data, 'Visualization of Missing Data in Sample DataFrame')
