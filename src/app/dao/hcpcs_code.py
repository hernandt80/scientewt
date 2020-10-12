import csv, rbql
from datetime import datetime
from decimal import Decimal

from .. import constants as cons
from ..dao.base import BaseDAO
from ..resources.columns_mapper import cm


class HcpcsDAO(BaseDAO):


    def get_more_profitable_hcpcs(self):
        query = """select 
                    m.hcpcs_code, 
                    AVG(m.avg_medicare_payment) 
                    from medicares m group by 1 order by 2 desc limit 10;"""
        return self._excecute_query(query)


    def get_hcpcs_code_by_services(self):
        query = """select 
                    hcpcs_code, 
                    sum(number_of_services) 
                    from medicares group by 1 order by 2 desc limit 10;"""
        return self._excecute_query(query)


    def get_avg_amounts_by_cpt(self, hcpcs_code):
        start = datetime.now()
        try:
            query = f'select ' \
                    f'AVG({cm.get("avg_medicare_payment")}), ' \
                    f'AVG({cm.get("avg_medicare_allowed")}), ' \
                    f'AVG({cm.get("avg_submitted_charge")}), ' \
                    f'{cm.get("prvider_state")} ' \
                    f'where {cm.get("hcpcs_code")} == \'{hcpcs_code}\' ' \
                    f'group by {cm.get("prvider_state")} '

            rbql.query_csv(
                query_text=query,
                input_path=cons.FILE_PATH_INPUT,
                input_delim=',',
                input_policy='quoted',
                output_path=cons.FILE_PATH_OUTPUT,
                output_delim=',',
                output_policy='quoted',
                csv_encoding='utf-8',
                output_warnings=[], skip_headers=True
            )
            ends = datetime.now()

            with open(cons.FILE_PATH_OUTPUT, newline='') as file:
                reader = csv.reader(file)
                result = []
                for row in reader:
                    data = {
                        'avg_medicare_payment': round(Decimal(row[0]),2),
                        'avg_medicare_allowed': round(Decimal(row[1]),2),
                        'avg_submitted_charge': round(Decimal(row[2]),2),
                        'provider_state': row[3],
                    }

                    result.append(data)

            return {
                "result": result if result else cons.NO_RESULTS,
                "time": ends-start
            }

        except Exception as e:
            return {
                "result": cons.ERROR_RESULT,
                "time": datetime.now()-start
            }

hcpcs_code_dao = HcpcsDAO()