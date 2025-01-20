import pickle
from config import MODEL_FILENAME
import pandas as pd

def predict_lost_days(idade,area_trabalho,zona_corpo_atingida,tipo_lesao):
    """
    Predict the number of lost days based on input features using a pre-trained model.

    This function performs the following steps:
    1. Loads a pre-trained model from a pickle file specified in config by `MODEL_FILENAME`.
    2. Creates a DataFrame with the provided input features.
    3. Ensures the input DataFrame has the correct column order expected by the model.
    4. Uses the model to predict the number of lost days.
    5. Returns the predicted number of lost days.

    Args:
        idade (int): The age of the individual.
        area_trabalho (str): The area of work where the individual is employed.
        zona_corpo_atingida (str): The body zone affected by the injury.
        tipo_lesao (str): The type of injury sustained.

    Returns:
        int: The predicted number of lost days.

    Raises:
        FileNotFoundError: If the model file specified by `MODEL_FILENAME` is not found.
    """
    # Load the pre-trained model from the pickle file
    with open(MODEL_FILENAME, 'rb') as file:
        model = pickle.load(file)
    
    # Create a DataFrame with the input features
    input_data = pd.DataFrame([{
        'Age': idade,
        'AreaAT': area_trabalho,
        'ZonaCorpoAtingida': zona_corpo_atingida,
        'TipoDeLesao': tipo_lesao
    }])
    
    # Ensure the input DataFrame has the correct column order expected by the model
    expected_features = model.feature_names_in_
    input_data = input_data[expected_features]
    
    # Use the model to predict the number of lost days
    predictions = model.predict(input_data)
    
    # Return the first prediction result
    return predictions[0]
    