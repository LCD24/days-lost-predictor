import pymysql, cx_Oracle, oracledb
from config import MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER, MYSQL_DATABASE
from config import ORACLE_HOST, ORACLE_PORT, ORACLE_SERVICE_NAME, ORACLE_USER, ORACLE_PASSWORD

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
    
def get_oracle_connection():
    """
    This function establishes a connection to an Oracle database using the provided credentials.
    
    Returns:
    - connection: A oracledb connection object to interact with the Oracle database.
    """
    dsn = f"{ORACLE_HOST}:{ORACLE_PORT}/{ORACLE_SERVICE_NAME}"
    connection = oracledb.connect(user=ORACLE_USER, password=ORACLE_PASSWORD, dsn=dsn, mode=oracledb.DEFAULT_AUTH)
    return connection