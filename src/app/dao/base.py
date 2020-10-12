from datetime import datetime

from src.app.resources.database import SqlConnector
from src.app import constants as cons

class BaseDAO(object):

    def __init__(self):
        self.sql = SqlConnector()


    def _response_builder(self, result, time):

        response = {
            "result": {i[0]: i[1] for i in result} if result else cons.NO_RESULTS,
            "time": f'{time}'
        }
        return response


    def _excecute_query(self, query):
        con = None
        result = None
        start = datetime.now()

        try:
            con = self.sql.get_sql_connection()
            c = con.cursor()

            c.execute(query)
            result = c.fetchall()

        except Exception:
            result = cons.ERROR_RESULT

        finally:
            con.close()
            return self._response_builder(result, datetime.now() - start)