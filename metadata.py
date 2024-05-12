import pandas as pd
import psycopg2
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables for database connections
load_dotenv()

# PostgreSQL Metadata Retrieval
def get_postgresql_metadata():
    """Retrieve metadata from a PostgreSQL database."""
    connection = psycopg2.connect(
        dbname=os.getenv('POSTGRESQL_DB'),
        user=os.getenv('POSTGRESQL_USER'),
        password=os.getenv('POSTGRESQL_PASSWORD'),
        host=os.getenv('POSTGRESQL_HOST')
    )
    query = """
    SELECT
        table_schema,
        table_name,
        column_name,
        data_type,
        is_nullable
    FROM information_schema.columns
    WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
    ORDER BY table_schema, table_name, ordinal_position;
    """
    df = pd.read_sql(query, con=connection)
    connection.close()
    return df

# MongoDB Metadata Retrieval
def get_mongodb_metadata():
    """Retrieve metadata from a MongoDB database."""
    client = MongoClient(os.getenv('MONGODB_URI'))
    db = client[os.getenv('MONGODB_DB')]
    metadata = {}
    for collection_name in db.list_collection_names():
        collection = db[collection_name]
        one_document = collection.find_one()
        metadata[collection_name] = list(one_document.keys()) if one_document else []
    client.close()
    return metadata

# Example usage
if __name__ == "__main__":
    # Fetch and print PostgreSQL metadata
    postgres_metadata = get_postgresql_metadata()
    print("PostgreSQL Metadata:")
    print(postgres_metadata.head())

    # Fetch and print MongoDB metadata
    mongo_metadata = get_mongodb_metadata()
    print("\nMongoDB Metadata:")
    for collection, keys in mongo_metadata.items():
        print(f"Collection: {collection}, Keys: {keys}")
