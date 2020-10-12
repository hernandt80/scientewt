from ..dao.hcpcs_code import hcpcs_code_dao
from ..dao.provider_state import provider_state_dao


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


    def get_avg_amounts_by_cpt(self, hcpcs_code):
        return self.hcpcs_code_dao.get_avg_amounts_by_cpt(hcpcs_code)


    def create_database(self):
        from .database import SqlConnector
        message = 'Database created!'
        try:
            sql = SqlConnector()
            sql._connect_and_create()

            return message
        except Exception:
            message = 'Error creating database!'

        return message