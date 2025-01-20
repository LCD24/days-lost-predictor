from flask import Flask, request, jsonify, send_from_directory
import pymysql 
from flask_swagger_ui import get_swaggerui_blueprint
from predict_lost_days import predict_lost_days as predict
from populate_mapping import add_function_mapping
from auth.password_hasher import BcryptPasswordHasher
from auth.authenticator import Authenticator
from train_predictor import train_model
from db_manager import DB_Manager

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/swagger.json'  # Our API url (can of course be a local resource)

# Create a Flask instance 
app = Flask(__name__)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Days Lost Predictor API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

password_hasher = BcryptPasswordHasher()
authenticator = Authenticator(password_hasher)

@app.route('/swagger.json')
def swagger_json():
    """
    Serve the Swagger JSON file.
    """
    return send_from_directory('.', 'swagger.json')

@app.route('/train/', methods=['POST'])
@authenticator.requires_auth
def retrain_model():
    """
    Retrain the prediction model using the latest data available.
    """
    try:
        model = train_model()
        print(model)
        return jsonify({'MSE': model['MSE'],'RMSE': model['RMSE'],'MAE': model['MAE'],'R2': model['R²']}), 200
    except Exception as e:
        return jsonify({'message': f"An unknown error occured: {e}"}), 500

@app.route('/predict-lost-days/', methods=['POST'])
@authenticator.requires_auth
def predict_lost_days():
    """
    Predict the number of lost working days due to an injury.
    """
    data = request.json
    
    # Extract data
    idade = data.get('idade')
    area_trabalho = data.get('area_trabalho')
    zona_corpo_atingida = data.get('zona_corpo_atingida')
    tipo_lesao = data.get('tipo_lesao')
    
    # Check if all data was sent
    if (not idade or  not area_trabalho or not zona_corpo_atingida or not tipo_lesao):
        return jsonify({'message': "You should include 'idade',  'area_trabalho', 'zona_corpo_atingida' and 'tipo_lesao' in your body"}), 400
    
    try:
        result = predict(idade,area_trabalho,zona_corpo_atingida,tipo_lesao)
    except FileNotFoundError:
        return jsonify({'message': "An error occured while loading the model"}), 500
    except Exception as e:
        return jsonify({'message': f"An unknown error occured: {e}"}), 500

    #Log data in DB
    db_manager = DB_Manager()
    acidente_data = {
            'funcionario': 1,
            'area_trabalho': data.get('area_trabalho'),
            'zona_corpo_atingida': data.get('zona_corpo_atingida'),
            'tipo_lesao': data.get('tipo_lesao'),
            'result': result
        }
    db_manager.enter_accidente_data(acidente_data)
    
    return jsonify({'days_lost': result}), 200

@app.route(rule='/add-function/', methods=['POST'])
@authenticator.requires_auth
def add_function():
    """
    Add a new function to be mapped .
    """
    data = request.json
    
    return '', 204
    
    
# Execute Flask app
if __name__ == '__main__':
    app.run(debug=True)
