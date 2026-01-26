import pandas as pd
import os
import warnings
from sqlalchemy import create_engine


def run():
    pg_username = "root"
    pg_password = "root"
    pg_host = "localhost"
    pg_port = 5432
    pg_db = "ny_taxi"

    year = 2021
    month = 1

    chunksize = 100_000

    target_table = 'yellow_taxi_data'

    dtype = {
        "VendorID": "Int64",
        "passenger_count": "Int64",
        "trip_distance": "float64",
        "RatecodeID": "Int64",
        "store_and_fwd_flag": "string",
        "PULocationID": "Int64",
        "DOLocationID": "Int64",
        "payment_type": "Int64",
        "fare_amount": "float64",
        "extra": "float64",
        "mta_tax": "float64",
        "tip_amount": "float64",
        "tolls_amount": "float64",
        "improvement_surcharge": "float64",
        "total_amount": "float64",
        "congestion_surcharge": "float64"
    }

    date_cols = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime"
    ]

    dir_path = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
    filename = f'yellow_tripdata_{year}-{month:02d}.csv.gz'
    filepath = os.path.join(dir_path, filename)

    # Create engine that builds connection to PostgreSQL database
    engine = create_engine(
        f'postgresql://{pg_username}:{pg_password}@{pg_host}:{pg_port}/{pg_db}'
    )

    # Load data in batches
    df_chunks = pd.read_csv(
        filepath,
        dtype=dtype,
        parse_dates=date_cols,
        chunksize=chunksize,
    )

    df_chunks = list(df_chunks)

    # Create a table with headers only but no data
    df_chunks[0].head(0).to_sql(
        name=target_table,
        con=engine,                 # Use the engine to connect to DB
        if_exists='replace',
    )

    # Insert data chunk by chunk
    for df_chunk in df_chunks:
        df_chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists='append',
        )
        print(f'{len(df_chunk)} records inserted.')


if __name__ == '__main__':
    run()