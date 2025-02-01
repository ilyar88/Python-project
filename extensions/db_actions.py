import allure
import test_cases.conftest as conf

class DBActions:
    @staticmethod
    @allure.step('Query builder')
    def query_builder(columns, table, where_name, where_value):
        """
        Builds a SQL query string for retrieving data from a database table.

        Args:
            columns (list): List of column names to retrieve.
            table (str): The name of the database table.
            where_name (str): The column name for the WHERE clause.
            where_value (str): The value to match in the WHERE clause.

        Returns:
            str: A SQL SELECT query string.
        """
        # Join the column names with commas to create the SELECT part
        cols = ','.join(columns)
        # Construct and return the complete query string
        return "SELECT " + cols + " FROM " + table + " WHERE " + where_name + " = '" + where_value + "'"

    @staticmethod
    @allure.step('Get query result')
    def get_query_result(columns, table, where_name, where_value):
        """
        Executes a SQL query and fetches the results from the database.

        Args:
            columns (list): List of column names to retrieve.
            table (str): The name of the database table.
            where_name (str): The column name for the WHERE clause.
            where_value (str): The value to match in the WHERE clause.

        Returns:
            list: A list of tuples containing the query results.
        """
        # Build the query using the query_builder method
        query = DBActions.query_builder(columns, table, where_name, where_value)
        # Get the database cursor from the connection
        db_cursor = conf.db_connector.cursor()
        # Execute the query
        db_cursor.execute(query)
        # Fetch and return all the results
        return db_cursor.fetchall()
