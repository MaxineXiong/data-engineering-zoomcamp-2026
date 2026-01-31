import pandas as pd
import os
import warnings
from sqlalchemy import create_engine
import click


# Define command-line argument options using Click
@click.command()
@click.option('--year', default=2021, type=int, help='Year of the data')
@click.option('--month', default=1, type=int, help='Month of the data')
@click.option('--chunksize', default=100_000, type=int, help='Chunk size for data ingestion')
@click.option('--pg_username', default='root', type=str, help='PostgreSQL username')
@click.option('--pg_password', default='root', type=str, help='PostgreSQL password')
@click.option('--pg_host', default='localhost', type=str, help='PostgreSQL host')
@click.option('--pg_port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg_db', default='ny_taxi', type=str, help='PostgreSQL database name')
@click.option('--target_table', default='yellow_taxi_data', type=str, help='Target table name in the database')
def run(year, month, chunksize, pg_username, pg_password, pg_host, pg_port, pg_db, target_table):
    """Ingest NY Taxi data into PostgreSQL database in chunks."""
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
        print(f'yellow_taxi_trips: {len(df_chunk)} records inserted.')


    # Load taxi zone lookup data
    df_zones = pd.read_csv('https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv')

    # Insert taxi zone data into a separate table
    df_zones.to_sql(
        name='zones',
        con=engine,
        if_exists='replace',
    )
    print(f'zones: {len(df_zones)} records inserted.')


if __name__ == '__main__':
    run()