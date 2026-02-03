import pandas as pd
import os
import warnings
from sqlalchemy import create_engine
import click


@click.command()
@click.option('--pg_username', default='root', type=str, help='PostgreSQL username')
@click.option('--pg_password', default='root', type=str, help='PostgreSQL password')
@click.option('--pg_host', default='localhost', type=str, help='PostgreSQL host')
@click.option('--pg_port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg_db', default='ny_taxi', type=str, help='PostgreSQL database')
def run(pg_username, pg_password, pg_host, pg_port, pg_db):
    engine = create_engine(
        f'postgresql://{pg_username}:{pg_password}@{pg_host}:{pg_port}/{pg_db}'
    )

    green_trip_data_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet'
    zone_data_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'

    df_green_trip = pd.read_parquet(green_trip_data_url)
    df_zone = pd.read_csv(zone_data_url)

    df_green_trip.to_sql(
        name='green_taxi_trips',
        con=engine,
        if_exists='replace',
    )
    print(f'green_taxi_trips: {len(df_green_trip)} rows inserted.')

    df_zone.to_sql(
        name='zones',
        con=engine,
        if_exists='replace',
    )
    print(f'zones: {len(df_zone)} rows inserted.')
    

if __name__ == '__main__':
    run()