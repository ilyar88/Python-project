import allure
import test_cases.conftest as conf

class DBActions:
    @staticmethod
    @allure.step('Query builder')
    def query_builder(columns, table, where_name, where_value):
        cols = ','.join(columns)
        return "SELECT " + cols + " FROM " + table + " WHERE " + where_name + " = '" + where_value + "'"

    @staticmethod
    @allure.step('Get query result')
    def get_query_result(columns, table, where_name, where_value):
        query = DBActions.query_builder(columns, table, where_name, where_value)
        db_cursor = conf.db_connector.cursor()
        db_cursor.execute(query)
        return db_cursor.fetchall()
