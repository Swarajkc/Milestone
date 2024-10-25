# connection.py

from snowflake.connector import connect
from main import connect_dict  # Import connect_dict from main.py

class Connection:
    def __init__(self):
        # Use credentials from main.py
        self.username = connect_dict['username']
        self.account = connect_dict['hostname']
        self.password = connect_dict['password']

    def create_connection(self, **parameters):
        # Disable Arrow result format
        session_parameters = {
            'CLIENT_RESULT_PREFETCH_THREADS': 1,
            'ENABLE_ARROW_RESULT_FORMAT': False  # Disable Arrow result format
        }

        # Establish connection
        conn = connect(
            user=self.username,
            password=self.password,
            account=self.account,
            session_parameters=session_parameters,
        )
        return conn

    def run_query(self, query_string, **params):
        """
        This function runs the query in Snowflake once a connection object is created.
        """
        try:
            conn = self.create_connection(parameters=params)

            with conn.cursor() as cursor:
                # Execute SQL query
                cursor.execute(query_string)

                # Fetch all the results
                result = cursor.fetchall()

            return result
        except Exception as exp:
            print(f"An error occurred: {exp}")
            raise exp
