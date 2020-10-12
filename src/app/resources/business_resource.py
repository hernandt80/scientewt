import csv
import rbql
from datetime import datetime

from src.app import constants as cons
from src.app.dao.hcpcs_code import hcpcs_code_dao
from src.app.dao.provider_state import provider_state_dao
from src.app.resources.columns_mapper import cm


class Business_resource(object):

    def __init__(self):
        self.hcpcs_code_dao = hcpcs_code_dao
        self.provider_state_dao = provider_state_dao



    def get_hcpcs_code_by_services(self):
        return self.hcpcs_code_dao.get_hcpcs_code_by_services()


    def get_more_profitable_hcpcs(self):
        return self.hcpcs_code_dao.get_more_profitable_hcpcs()


    def get_top_payers_by_hcpcs_code(self,hcpcs_code):
        return self.provider_state_dao.get_top_payers_by_hcpcs_code(hcpcs_code)


    def get_best_payer_states_by_hcpcs_code(self, hcpcs_code):
        return self.provider_state_dao.get_best_payer_states_by_hcpcs_code(hcpcs_code)


    def get_states_less_hcpcs_coverage(self):
        return self.provider_state_dao.get_states_less_hcpcs_coverage()


    def get_more_reliable_states_by_hcpcs(self, hcpcs_code):
        return self.provider_state_dao.get_more_reliable_states_by_hcpcs(hcpcs_code)




    def other(self, cpt_code):
        query = f'select ' \
                f'{cm.get("avg_medicare_allowed")}, ' \
                f'{cm.get("avg_medicare_payment")}, ' \
                f'{cm.get("avg_medicare_standarized")}, ' \
                f'{cm.get("avg_submitted_charge}")}, ' \
                f'{cm.get("npi")}, ' \
                f'{cm.get("hcpcs_code")} ' \
                f'where {cm.get("hcpcs_code")} == \'{cpt_code}\''
        start = datetime.now()
        rbql.query_csv(
            query_text=query,
            input_path='data_acotada.csv',
            input_delim=',',
            input_policy='quoted',
            output_path='result.csv',
            output_delim=',',
            output_policy='quoted',
            csv_encoding='utf-8',
            output_warnings=[]
        )
        ends = datetime.now()

        row_last = None

        with open('result.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                row_last = row

        return self.build_response(row_last, ends-start, None)



    def get_statistics_by_cpt2(self, cpt_code):
        '''
            select
                avg(payment)
            group by state


            By CPT code:

            cpt:
                menor diff :
                    estado:
                    monto:
                menor pago:
                    estado:
                    monto:
                mayor diff

        '''




        start = datetime.now()

        query = f'select ' \
                f'AVG({cm.get("avg_medicare_payment")}), ' \
                f'AVG({cm.get("avg_medicare_allowed")}), ' \
                f'AVG({cm.get("avg_submitted_charge")}), ' \
                f'{cm.get("prvider_state")} ' \
                f'where {cm.get("hcpcs_code")} == \'{cpt_code}\' ' \
                f'group by {cm.get("prvider_state")} '

        print(f'corriendo query: {query}')

        rbql.query_csv(
            query_text=query,
            input_path=cons.f,
            input_delim=',',
            input_policy='quoted',
            output_path=cons.FILE_PATH_OUTPUT,
            output_delim=',',
            output_policy='quoted',
            csv_encoding='utf-8',
            output_warnings=[]
        )
        ends = datetime.now()

        with open('result.csv', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                result = row

        return self.build_response(
            cpt_code,
            result if result else None,
            ends-start
        )


    def build_response(self, cpt_code, result, time):
        response = {
            "cpt_code": cpt_code,
            "result": result,
            "took": f'{time} hs.'
        }

        return response