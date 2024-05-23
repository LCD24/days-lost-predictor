from fetch_outsystems_data import get_data
from connection_factory import get_connection
import pymysql

def add_mapping(value, table_name, connection=None):
    """
    Add a mapping value to the specified table in the database.

    This function checks if a given value already exists in the specified table.
    If the value does not exist, it inserts the value into the table.

    Args:
        value (str): The value to be checked and potentially added to the table.
        table_name (str): The name of the table in which the value will be checked and potentially added. Should be equal 
        to the corresponding field.
        connection (pymysql.connections.Connection, optional): The database connection. If None, a new connection is created.

    Raises:
        pymysql.Error: If an error occurs during database operations, it raises a pymysql.Error.
    """
    connection_created = False
    if connection is None:
        connection = get_connection()
        connection_created=True

    try:
        with connection.cursor() as cursor:
            # Check if the occupation already exists in the database
            query = f"SELECT * FROM {table_name} WHERE {table_name} = %s"
            cursor.execute(query, (value,))
            result = cursor.fetchone()

            # If occupation doesn't exist, insert it into the database
            if not result:
                query = f"INSERT INTO {table_name} ({table_name}) VALUES (%s)"
                cursor.execute(query, (value,))
                connection.commit()
                print(f"Function '{value}' added to database.")
    except pymysql.Error as e:
        if connection_created:
            connection.close()
            
        raise pymysql.Error(e)
    finally:
        if connection_created:
            connection.close()

def add_function_mappings_from_outsystem_data():
    """
    Add function mappings from OutSystems data to the 'funcao' table in the database.

    This function retrieves data from OutSystems, extracts unique functions, and adds them
    to the 'funcao' table in the database.

    Raises:
        pymysql.Error: If an error occurs during database operations, it raises a pymysql.Error.
    """
    df = get_data()
    
    connection = get_connection()
    
    # Drop duplicate entries in the 'Function' column
    df = df.drop_duplicates(subset=['Function'])
    
    # Iterate through each unique function and add it to the 'funcao' table
    for _, row in df.iterrows():
        function = row['Function']
        add_mapping(function, "funcao", connection)
    
    connection.close()
        
def add_function_mapping(function):
    """
    Add a single function mapping to the 'funcao' table in the database.

    Args:
        function (str): The function value to be added to the 'funcao' table.

    Raises:
        pymysql.Error: If an error occurs during database operations, it raises a pymysql.Error.
    """
    add_mapping(function, "funcao")

    
# Ensure the main function is called when the script is executed directly
if __name__ == "__main__":
    add_function_mappings_from_outsystem_data()