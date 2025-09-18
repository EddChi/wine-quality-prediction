import matplotlib.pyplot as plt
import seaborn as sns

def check_missing_and_duplicates(df):
    # Print missing values and duplicate count
    duplicates = df.duplicated().sum()
    missing = df.isnull().sum()
    total_missing = df.isnull().sum().sum()

    print(f"Number of duplicate rows: {duplicates}")
    print(f"Number of missing values in rows: \n{missing}")
    print(f"Total number of missing values in dataset: {total_missing}")

def plot_correlation_heatmap(df, save_path=None):
    # Plot and optionally save correlation heatmap
    plt.figure(figsize=(10,8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Feature Correlation Heatmap")
    if save_path:
        plt.savefig(save_path)
    plt.show()