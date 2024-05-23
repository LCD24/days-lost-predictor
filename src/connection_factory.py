import pymysql
from config import MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER, MYSQL_DATABASE

def get_connection():
    """
    This function establishes a connection to a MySQL database using the provided credentials.
    
    Returns:
    - connection: A pymysql connection object to interact with the MySQL database.
    """
    return pymysql.connect(host=MYSQL_HOST,
                             user=MYSQL_PASSWORD,
                             password=MYSQL_USER,
                             database=MYSQL_DATABASE,
                             cursorclass=pymysql.cursors.DictCursor
    )