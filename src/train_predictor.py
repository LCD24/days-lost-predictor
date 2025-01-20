import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from connection_factory import get_connection
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
import pickle
import os
from config import MODEL_FILENAME, DATASET_FILENAME
from dataset_generator import generate_dataset

def clean_data(df):
    """
    Cleans the input DataFrame by removing rows with missing values (NaN)
    and filtering out entries where 'DaysLost' is greater than 365.

    Args:
        df (pandas.DataFrame): The DataFrame to be cleaned.

    Returns:
        pandas.DataFrame: The cleaned DataFrame.
    """
    
    df = df.dropna()
    df = df[df['DaysLost'] <= 365]

    return df

 
    
def find_best_model(X, y, test_size=0.4,random_state=20):
    """
    Evaluates multiple regression models and returns the result metrics of all models and
    the best performing model based on mean squared error (MSE).

    Args:
        X (pd.DataFrame): Input features.
        y (pd.Series): Target variable.

    Returns:
        best_model_info: Dictionary containing the best model's name, random state, and performance metrics
            (MSE, RMSE, MAE, R²).
        results: Dictionary containing the metrics of each model. The key is the model name.
    """

    models = {
        'Random Forest': RandomForestRegressor(random_state=20),
        'Ridge Regression': Ridge(),
        'Lasso Regression': Lasso(),
        'Gradient Boosting': GradientBoostingRegressor(),
        'AdaBoost': AdaBoostRegressor()
    }

    results = {}
    best_model_name = None  
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    for name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)

            results[name] = {
                    'name': name,
                    'model': model,
                    'MSE': mse,
                    'RMSE': mean_squared_error(y_test, y_pred, squared=False),
                    'MAE': mean_absolute_error(y_test, y_pred),
                    'R²': r2_score(y_test, y_pred)
            }

            if best_model_name is None or mse < results[best_model_name]['MSE']:
                best_model_name = name
            
    best_model = results[best_model_name]
    return best_model, results

def print_model_evaluation(name, metrics):
    """
        Prints the evaluation metrics for a given model.

        Args:
            name (str): The name of the model.
            metrics (dict): A dictionary containing the model's evaluation metrics,
                            including 'MSE', 'RMSE', 'MAE', and 'R²'.
    """
    
    print(f"Model: {name}")
    print("Performance Metrics:")
    print(f"\tMSE: {metrics['MSE']}")
    print(f"\tRMSE: {metrics['RMSE']}")
    print(f"\tMAE: {metrics['MAE']}")
    print(f"\tR²: {metrics['R²']}")
    print()

def print_models_evaluation(results):
    """
        Prints the evaluation metrics for all models in a dictionary.

        Args:
            results (dict): A dictionary containing evaluation metrics for different
                            models. The keys are model names, and the values are
                            dictionaries containing individual model metrics (same as
                            in the `print_model_evaluation` function).
    """
    for name, metrics in results.items():
        print_model_evaluation(name,metrics)

def save_model(model):
    """
    Saves a machine learning model object to a file using pickle serialization.

    Args:
        model: The machine learning model object to be saved.
    """

    directory = os.path.dirname(MODEL_FILENAME)
    os.makedirs(directory, exist_ok=True)    
    with open(MODEL_FILENAME, 'wb') as file:
        pickle.dump(model, file=file)

def train_model():
    """
    Loads, preprocesses data, selects features, trains a model, and saves the best model.
    """
    generate_dataset()
    data =  pd.read_csv(DATASET_FILENAME)

    data = clean_data(data)

    X= data.iloc[:,:-1]
    Y= data.iloc[:,-1]

    best_features= SelectKBest(score_func=chi2, k=3)
    fit= best_features.fit(X,Y)

    df_scores= pd.DataFrame(fit.scores_)
    df_columns= pd.DataFrame(X.columns)

    # top features
    features_scores= pd.concat([df_columns, df_scores], axis=1)
    features_scores.columns= ['Features', 'Score']
    features_scores = features_scores.sort_values(by = 'Score', ascending=False)

    # print("\nScore")
    # print(features_scores)

    top_features = features_scores[:4]
    top_features = top_features['Features'].tolist()
    X = data[top_features]

    best_model_result, results = find_best_model(X, Y)

    print_models_evaluation(results)
    print("\nBest Model")
    print_model_evaluation(best_model_result['name'], best_model_result)

    save_model(best_model_result['model'])
    return best_model_result
    
    
if __name__ == "__main__":
    train_model()