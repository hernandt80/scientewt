import csv
import sqlite3

from sqlite3 import Error

DATABASE_NAME = 'science.db'
FILE_NAME = 'file.csv'

class SqlConnector(object):


    def get_sql_connection(self):
        try:
            con = sqlite3.connect(DATABASE_NAME)
            return con
        except Error as e:
            raise Exception(e)


    def _connect_and_create(self):
        con = self.get_sql_connection()
        self._create_sql_tables(con)
        self._populate_medicare(con)
        self._populate_providers(con)


    def _create_sql_tables(self, con):
        cursorObj = con.cursor()

        cursorObj.execute(
            'CREATE TABLE IF NOT EXISTS providers('
            'npi integer PRIMARY KEY, '
            'provider_last_name text, '
            'provider_first_name text, '
            'provider_middle_name text, '
            'provider_credentials text, '
            'provider_gender text, '
            'provider_entity_type text, '
            'provider_address_1 text, '
            'provider_address_2 text, '
            'provider_city text, '
            'provider_zipcode text, '
            'prvider_state text, '
            'prvider_country text, '
            'provider_type text, '
            'CONSTRAINT fk_medicares FOREIGN KEY (npi) REFERENCES medicares(npi)'
            ');'
        )

        cursorObj.execute(
            'CREATE TABLE IF NOT EXISTS medicares('
            'id integer PRIMARY KEY AUTOINCREMENT, '
            'npi integer, '
            'medicare_participation_indicator text, '
            'pos text, '
            'hcpcs_code text, '
            'hcpcs_description text, '
            'hcpcs_drug_indicator text, '
            'number_of_services integer, '
            'number_of_medicare_beneficiaries integer, '
            'number_of_distinct_medicare_ben integer, '
            'avg_medicare_allowed REAL, '
            'avg_submitted_charge REAL, '
            'avg_medicare_payment REAL, '
            'avg_medicare_standarized REAL);'
        )

        con.commit()


    def _populate_medicare(self, con):

        with open('file.csv', 'r') as file:
            dr = csv.DictReader(file)

            medicares = [(
                i['﻿National Provider Identifier'],
                i['Medicare Participation Indicator'],
                i['Place of Service'],
                i['HCPCS Code'],
                i['HCPCS Description'],
                i['HCPCS Drug Indicator'],
                i['Number of Services'],
                i['Number of Medicare Beneficiaries'],
                i['Number of Distinct Medicare Beneficiary/Per Day Services'],
                i['Average Medicare Allowed Amount'],
                i['Average Submitted Charge Amount'],
                i['Average Medicare Payment Amount'],
                i['Average Medicare Standardized Amount']
            ) for i in dr]

        con.cursor().executemany("INSERT INTO medicares ("
                                 "npi, "
                                 "medicare_participation_indicator, "
                                 "pos, "
                                 "hcpcs_code, "
                                 "hcpcs_description, "
                                 "hcpcs_drug_indicator, "
                                 "number_of_services, "
                                 "number_of_medicare_beneficiaries, "
                                 "number_of_distinct_medicare_ben, "
                                 "avg_medicare_allowed, "
                                 "avg_submitted_charge, "
                                 "avg_medicare_payment, "
                                 "avg_medicare_standarized"
                                 ") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", medicares)

        con.commit()
        con.close()


    def _populate_providers(self, con):

        with open('file.csv', 'r') as file:
            dr = csv.DictReader(file)

            providers = [(i['﻿National Provider Identifier'],
                i['Last Name/Organization Name of the Provider'],
                i['First Name of the Provider'],
                i['Middle Initial of the Provider'],
                i['Credentials of the Provider'],
                i['Gender of the Provider'],
                i['Entity Type of the Provider'],
                i['Street Address 1 of the Provider'],
                i['Street Address 2 of the Provider'],
                i['City of the Provider'],
                i['Zip Code of the Provider'],
                i['State Code of the Provider'],
                i['Country Code of the Provider'],
                i['Provider Type']
            ) for i in dr]

            prov_uniques = [t for t in (set(tuple(i) for i in providers))]

        con.cursor().executemany("INSERT INTO providers ("
                                 "npi, "
                                 "provider_last_name, "
                                 "provider_first_name, "
                                 "provider_middle_name, "
                                 "provider_credentials, "
                                 "provider_gender, "
                                 "provider_entity_type, "
                                 "provider_address_1, "
                                 "provider_address_2, "
                                 "provider_city, "
                                 "provider_zipcode, "
                                 "prvider_state, "
                                 "prvider_country, "
                                 "provider_type"
                                 ") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", prov_uniques)

        con.commit()
        con.close()


if __name__ == "__main__":
    sql = SqlConnector()
    sql._connect_and_create()