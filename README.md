# Days Lost Predictor API

The Days Lost Predictor API is a Flask-based web service created to predict the number of lost working days due to work-related injuries. It provides an endpoint where users can submit detailed information about an injury, such as the worker's age, occupation, area of work, affected body zone, and type of injury. Using a pre-trained machine learning model, the API will predict the how much days the worker is expected to be absent from work due to the injury.

## Mapping
The API includes functionality to add new function mappings to the system. Functions, or job roles, can be mapped to unique identifiers in the database. **Whenever the user adds a new function, the function mapping endpoint must be called.**

This feature is essential to train the model correctly, as it ensures that the prediction model has the latest information about the inputs possibilities.

## Database Setup

To set up the database for the Days Lost Predictor API, follow these steps:

1. Create a new database: Create a MySQL database:

    ```
    CREATE DATABASE days_off_database;
    ```

2. Select the database:

    ```
    USE days_off_database;
    ```

2. Create tables: 

    ```
    # File included in project repository
    source database_schema.sql;
    ```

3. Configure database connection  

    Update the database connection settings in the `src/config.py` file to match your database configuration, including the database host, username, password, and database name.

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/LCD24/days-lost-predictor
    ```

2. Navigate to the project directory:

    ```
    cd days-lost-predictor
    ```

3. Create a virtual environment:

    ```
    # For Windows
    python -m venv venv

    # For Unix/Mac
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    ```
    # For Windows
    venv\Scripts\activate

    # For Unix/Mac
    source venv/bin/activate
    ```

5. Install dependencies:

    ```
    cd ../..
    pip install -r requirements.txt
    ```

6. Populate database mappings:

    ```
    cd src
    py populate_mapping.py
    ```

6. Run the app:

    ```
    py app.py
    ```

## Usage

To interact with the Days Lost Predictor API, users can utilize the provided Swagger UI interface for easy visualization and interaction with the API documentation. Simply navigate to the following URL in your browser:

http://localhost:5000/api/docs

In the other hand, you can make POST requests to the following endpoints:

- `/predict-lost-days/`: Endpoint for predicting the number of lost working days due to an injury. Requires a JSON payload containing injury information.
- `/add-function/`: Endpoint for adding new function mappings to the system. Requires a JSON payload containing the new function name.