import requests
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from config import OUTSYSTEM_DATA_FILENAME
import os
from config import OUTSYSTEM_USER, OUTSYSTEM_PASSWORD,OUTSYSTEM_BASE_URL

colaborators_api_url = OUTSYSTEM_BASE_URL + "/GetColaboradores"
accidents_api_url = OUTSYSTEM_BASE_URL + "/GetSinistros"

def generate_age_column(df):
    """
    Add an 'Age' column to the DataFrame based on the 'BirthDate' column.

    Args:
        df (pd.DataFrame): The DataFrame containing a 'BirthDate' column.

    Returns:
        pd.DataFrame: The DataFrame with an added 'Age' column and the 'BirthDate' column removed.
    """
    # Convert 'Birthdate' column to datetime
    df['BirthDate'] = pd.to_datetime(df['BirthDate'])

    # Calculate age
    today = datetime.today()
    df['Age'] = df['BirthDate'].apply(lambda x: relativedelta(today, x).years)

    # Drop 'Birthdate' column
    return df.drop(columns=['BirthDate'])

def fetch_data(url, selected_columns, index_column):
    """
    Fetch data from an API and load it into a DataFrame.

    This function sends a GET request to the specified URL with basic authentication,
    retrieves the data in JSON format, loads it into a DataFrame, and selects specific
    columns. It also sets a specified column as the index.

    Args:
        url (str): The API endpoint URL.
        selected_columns (list): A list of columns to select from the API response.
        index_column (str): The column to set as the index of the DataFrame.

    Returns:
        pd.DataFrame: The DataFrame containing the selected columns with the specified index.
    """
    response = requests.get(url, auth=(OUTSYSTEM_USER, OUTSYSTEM_PASSWORD))

    # Check if the request was successful
    if response.status_code == 200:
        # Load received data into Pandas DataFrame
        data = response.json()
        df = pd.DataFrame(data)
        
        df = df[selected_columns]
        df.set_index(index_column, inplace=True)
        
        return df
    else:
        print(f"Error accessing {url}: {response.status_code}")


def get_data():
    """
    Retrieve and process data from multiple APIs, combine them, and save to a CSV file.

    This function performs the following steps:
    1. Fetches collaborator data from an API, selects specific columns, and generates an 'Age' column.
    2. Fetches accident data from another API, selects specific columns.
    3. Joins the two DataFrames on a common index.
    4. Renames the 'Occupation' column to 'Function'.
    5. Saves the combined DataFrame to a CSV file specified by `OUTSYSTEM_DATA_FILENAME`.

    Returns:
        pd.DataFrame: The combined DataFrame after processing.
    """
    selected_columns = ['Id','BirthDate', 'Occupation']
    df = fetch_data(colaborators_api_url, selected_columns, "Id")
    df = generate_age_column(df)

    selected_columns = ['WorkerId','TipoDeLesao', 'ZonaCorpoAtingida', 'AreaAT', 'DaysLost']
    accidents_df = fetch_data(accidents_api_url, selected_columns, "WorkerId")

    if df is not None:
        df = df.join(accidents_df)
        df.rename(columns={'Occupation': 'Function'}, inplace=True)
        
        # Create directory structure up to the file path
        directory = os.path.dirname(OUTSYSTEM_DATA_FILENAME)
        os.makedirs(directory, exist_ok=True)       
        df.to_csv(OUTSYSTEM_DATA_FILENAME, index=False)
    
    return df