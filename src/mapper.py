from connection_factory import get_connection, get_oracle_connection
import pymysql

def map_function(function):
    """
    Map a function name to its corresponding identifier from the 'funcao' table in the database.

    This function retrieves the unique identifier (id_funcao) associated with the provided function name
    by fetching mapping data from the 'funcao' table in the database.

    Args:
        function (str): The name of the function to be mapped.

    Returns:
        int: The identifier (id_funcao) corresponding to the provided function name.

    Raises:
        pymysql.Error: If an error occurs during database operations.
        Exception: If the provided function name is not mapped in the database.
    """
    try:
        # Establish a database connection
        connection = get_oracle_connection()

        # Fetch mapping data from MySQL for the provided function name
        query = "SELECT id_funcao FROM funcao WHERE funcao = :1"
        with connection.cursor() as cursor:
            cursor.execute(query, (function,))
            result = cursor.fetchone()

            # If no matching row is found, raise an exception
            if not result:
                raise Exception(f"The function '{function}' is not mapped in the database.")
            
        # Close the database connection
        connection.close()

        # Return the identifier corresponding to the provided function name
        return result[0]
    except pymysql.Error as e:
        # Handle pymysql errors
        raise pymysql.Error(f"Error occurred during database operation: {e}")