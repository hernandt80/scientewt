from src.app.dao.base import BaseDAO


class HcpcsDAO(BaseDAO):


    def get_more_profitable_hcpcs(self):
        query = """select 
                    m.hcpcs_code,
	                AVG(m.avg_medicare_payment)
                    from medicares m 
                    group by 1 order by 2 desc limit 10;"""
        return self._excecute_query(query)


    def get_hcpcs_code_by_services(self):
        query = """select 
                    hcpcs_code, 
                    sum(number_of_services) 
                    from medicares group by 1 order by 2 desc limit 10;"""
        return self._excecute_query(query)


    def get_top_covered_hcps(self):
        query = """
        """
        return self._excecute_query(query)


hcpcs_code_dao = HcpcsDAO()