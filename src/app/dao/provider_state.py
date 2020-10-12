from src.app.dao.base import BaseDAO


class ProviderStateDAO(BaseDAO):

    def get_states_less_hcpcs_coverage(self):
        query = """select
                    p.prvider_state,
                    count(distinct m.hcpcs_code)
                    from medicares m 
                    inner join providers p on p.npi = m.npi 
                    group by p.prvider_state order by 2 asc limit 10;"""
        return self._excecute_query(query)


    def get_more_reliable_states_by_hcpcs(self, hcpcs_code):
        query = f""""select 
                    p.prvider_state, 
                    ( CAST(m.avg_medicare_payment as float)  * 100 / CAST(m.avg_medicare_allowed as float) )
                    from medicares m 
                    inner join providers p on p.npi = m.npi 
                    where m.hcpcs_code = {hcpcs_code}
                    group by p.prvider_state order by 2 desc limit 100;"""
        return self._excecute_query(query)


    def get_top_payers_by_hcpcs_code(self, hcpcs_code):
        query = f"""select p.prvider_state, AVG(m.avg_medicare_payment) 
                      from medicares m 
                      inner join providers p on p.npi = m.npi 
                      where m.hcpcs_code = {hcpcs_code}
                      group by p.prvider_state order by 2 desc limit 10;"""
        return self._excecute_query(query)


    def get_best_payer_states_by_hcpcs_code(self, hcpcs_code):
        query = f"""select p.prvider_state, AVG(m.avg_medicare_payment) 
                      from medicares m 
                      inner join providers p on p.npi = m.npi 
                      where m.hcpcs_code = {hcpcs_code}
                      group by p.prvider_state order by 2 desc limit 10;"""
        return self._excecute_query(query)


provider_state_dao = ProviderStateDAO()