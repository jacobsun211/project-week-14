import mysql.connector
from core.settings import setting
from core.errors import MySQLError
from contextlib import contextmanager

class SQL_Manager:
    cnx = None

    @classmethod
    def connect(cls):
        if cls.cnx is not None:
            raise Exception
        
        cls.cnx = mysql.connector.connect(host=setting.HOST_MYSQL, 
                                    port=setting.PORT_MYSQL,
                                    user=setting.USER_MYSQL,
                                    password=setting.PASSWORD_MYSQL)
        
    @classmethod
    def close(cls):
        if cls.cnx is None:
            raise Exception
        
        cls.cnx.close()
        


    @classmethod
    def init(cls):
    # delete this when the statefulset initilized the sql scehma
        with open('sql\schema.sql', 'r') as file:
            sql_queries = file.read()

        queries = sql_queries.split(';')

        for query in queries:
            try:
                if query.strip() != '':
                    cls.cnx.cursor().execute(query)
                    cls.cnx.commit()
                    print("Query executed successfully!")
            except Exception as e:
                print("Error executing query:", str(e))


    
def get_cursor():

    try:
        cnx = SQL_Manager.cnx
        cursor = cnx.cursor(dictionary=True)

        yield cursor

        cnx.commit()

    except Exception as e:
        if cnx:
            cnx.rollback()

        raise MySQLError(str(e))
    
    finally:
        if cursor:
            cursor.close()

