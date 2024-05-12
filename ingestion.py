import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from simple_salesforce import Salesforce
import cx_Oracle
from google.cloud import bigquery

# Load environment variables
load_dotenv()

# Salesforce Ingestion
def load_data_from_salesforce(query):
    sf = Salesforce(
        username=os.getenv('SALESFORCE_USERNAME'), 
        password=os.getenv('SALESFORCE_PASSWORD'), 
        security_token=os.getenv('SALESFORCE_TOKEN')
    )
    query_result = sf.query_all(query)
    return pd.DataFrame(query_result['records'])

# Oracle Ingestion
def load_data_from_oracle(username, password, dsn, query):
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    df = pd.read_sql(query, con=connection)
    connection.close()
    return df

# Google Cloud BigQuery Ingestion
def load_data_from_bigquery(project_id, query):
    client = bigquery.Client(project=project_id)
    query_job = client.query(query)
    return query_job.to_dataframe()

# MySQL Ingestion using SQLAlchemy for enhanced security with SSL
def load_data_from_mysql(query, db_url):
    engine = create_engine(db_url)
    with engine.connect() as connection:
        df = pd.read_sql_query(query, connection)
    return df

# PostgreSQL Ingestion using SQLAlchemy
def load_data_from_postgresql(query, db_url):
    engine = create_engine(db_url)
    with engine.connect() as connection:
        df = pd.read_sql_query(query, connection)
    return df

# Example usage:
if __name__ == "__main__":
    # Example Salesforce query
    sf_data = load_data_from_salesforce("SELECT Id, Name FROM Account")
    print(sf_data.head())

    # Example Oracle query
    oracle_data = load_data_from_oracle(
        username='your_username', 
        password='your_password', 
        dsn='your_dsn', 
        query='SELECT * FROM your_table'
    )
    print(oracle_data.head())

    # Example BigQuery query
    bq_data = load_data_from_bigquery(
        project_id='your_project_id',
        query='SELECT * FROM `your_project.your_dataset.your_table`'
    )
    print(bq_data.head())

    # Example MySQL query
    mysql_data = load_data_from_mysql(
        query='SELECT * FROM your_table', 
        db_url=os.getenv('MYSQL_DB_URL')
    )
    print(mysql_data.head())

    # Example PostgreSQL query
    pg_data = load_data_from_postgresql(
        query='SELECT * FROM your_table',
        db_url=os.getenv('POSTGRESQL_DB_URL')
    )
    print(pg_data.head())
