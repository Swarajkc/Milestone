# query_data.py

from utils.connection import Connection  # Import the Connection class

def fetch_sample_data():
    """
    Fetch and print sample data from Snowflake using the Connection class.
    """
    # Initialize the connection object
    conn_obj = Connection()

    try:
        # Query to fetch data from TPCDS_SF100TCL.CALL_CENTER table
        query = "SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCDS_SF100TCL.CALL_CENTER LIMIT 10;"

        # Run the query and fetch results
        result = conn_obj.run_query(query_string=query)

        # Print each row of the result
        print("\nFetched Data:")
        for row in result:
            print(row)

    except Exception as e:
        print(f"Error executing query: {e}")

if __name__ == "__main__":
    fetch_sample_data()
