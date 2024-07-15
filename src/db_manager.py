from connection_factory import get_connection, get_oracle_connection

class DB_Manager:
    def __init__(self):
        self.connection = get_oracle_connection()
        
    def enter_accidente_data(self, data):
        
        insert_query = """
        INSERT INTO acidente 
        (id_funcionario, id_area_trabalho, id_zona_corpo_atingida, id_tipo_lesao, dias_perdidos)
        VALUES (:funcionario, :area_trabalho, :zona_corpo_atingida, :tipo_lesao, :dias_perdidos)
        """

        params = {
            'funcionario': 1,
            'area_trabalho': data['area_trabalho'],
            'zona_corpo_atingida': data['zona_corpo_atingida'],
            'tipo_lesao': data['tipo_lesao'],
            'dias_perdidos': data['result']
        }
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query, params)
            self.connection.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.connection.rollback()
        finally:
            cursor.close()