from fetch_outsystems_data import get_data
import pandas as pd
from config import DATASET_FILENAME, ARTIFICIAL_DATASET_FILENAME

def generate_dataset():
    """
    Generate a combined dataset from fetched data and an artificial dataset.

    This function performs the following steps:
    1. Fetches data using the `get_data` function.
    2. Attempts to read an artificial dataset from a CSV file specified by `ARTIFICIAL_DATASET_FILENAME`.
    3. If the artificial dataset is successfully read, it concatenates the fetched data and the artificial dataset vertically.
    4. If the artificial dataset is not found or cannot be read, it proceeds with the fetched data alone.
    5. Saves the combined DataFrame (or the fetched data alone) to a new CSV file specified by `DATASET_FILENAME`.
    6. Prints a success message upon completion.

    Returns:
        None
    """
    
    # Fetch data using the get_data function
    df1 = get_data()
    combined_df=df1
    
    # Read the artificial dataset from a CSV file
    try:
        df2 = pd.read_csv(ARTIFICIAL_DATASET_FILENAME)
        
        # Concatenate the DataFrames vertically
        combined_df = pd.concat([df1, df2], ignore_index=True)
    except:
        pass
    finally:
        # Save the combined DataFrame to a new CSV file
        combined_df.to_csv(DATASET_FILENAME, index=False)
        
        print("Dataset created successfully.")
    
# Ensure the function is called only when the script is executed directly
if __name__ == "__main__":
    generate_dataset()