# Module 1 Homework: Docker & SQL

My solutions to the **Module 1 Homework of the** [**Data Engineering Zoomcamp 2026**](https://github.com/DataTalksClub/data-engineering-zoomcamp.git) 
by [**DataTalks.Club**](https://datatalks.club/).


## Question 1. Understanding Docker images

Run docker with the `python:3.13` image. Use an entrypoint `bash` to interact with the container.

What's the version of `pip` in the image?

- **25.3** ✔️
- 24.3.1
- 24.2.1
- 23.3.1

<br>

**My Solution**:

The following **2 commands** were executed in the Terminal to figure out the `pip` version:

```bash
# Create and start a container based on the "python:3.13" image
docker run -it --rm --entrypoint=bash python:3.13

# Find the pip version when inside the container
pip --version
```

Output result:
```bash
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)
```


## Question 2. Understanding Docker networking and docker-compose

Given the following `docker-compose.yaml`, what is the `hostname` and `port` that pgadmin should use to connect to the postgres database?

```yaml
services:
  db:
    container_name: postgres
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - '5433:5432'
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
      PGADMIN_DEFAULT_PASSWORD: "pgadmin"
    ports:
      - "8080:80"
    volumes:
      - vol-pgadmin_data:/var/lib/pgadmin

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data
```

- postgres:5433
- localhost:5432
- db:5433
- postgres:5432
- **db:5432** ✔️

If multiple answers are correct, select any 


## Prepare the Data

The green taxi trips data for November 2025 can be downloaded here:

```bash
wget https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet
```

Zone data can be downloaded here:

```bash
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv
```

**Step 1: Create virtual environment with `uv`.**

The folder was initiated with the `uv` package, which automatically handles virtual environment.

```bash
# Initialise the folder with python>=3.13
uv init --python=3.13
```

**Step 2: Create a Python script for data ingestion.**

Add the dependencies required for running the script:
```bash
uv add pandas pyarrow sqlalchemy psycopg2-binary click
```

Create a Python script for the ingestion of both datasets: [**ingest_data.py**](./ingest_data.py).

**Step 3: Create a [Dockerfile](./Dockerfile) for the custom Docker image of the data ingestion script.**


**Step 4: Create [docker-compose.yaml](./docker-compose.yaml) for orchestrating multiple services to run together in the same network.**


**Step 5: Run all three containers (incl. PostgreSQL database, data ingestion script, and pgAdmin) by executing the command below.**

```bash
docker-compose up
```

**Step 6: Log into pgAdmin and query from the database.**


## Question 3. Counting short trips

For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a `trip_distance` of less than or equal to 1 mile?

- 7,853
- **8,007** ✔️
- 8,254
- 8,421

<br>

**My Solution**:

The following SQL query was used in pgAdmin to pull out the number of trips with `trip_distance` less than or equal to 1 mile:
```sql
SELECT COUNT(*) AS trip_count
FROM green_taxi_trips
WHERE 
	trip_distance <= 1
	AND lpep_pickup_datetime >= '2025-11-01'
	AND lpep_pickup_datetime < '2025-12-01';
```

<br>

## Question 4. Longest trip for each day

Which was the pick up day with the longest trip distance? Only consider trips with `trip_distance` less than 100 miles (to exclude data errors).

Use the pick up time for your calculations.

- **2025-11-14** ✔️
- 2025-11-20
- 2025-11-23
- 2025-11-25

<br>

**My Solution**:

The following SQL query was used in pgAdmin:

```sql
SELECT 
	DATE(lpep_pickup_datetime) AS pickup_day,
	MAX(trip_distance) AS max_trip_distance
FROM green_taxi_trips
WHERE trip_distance < 100
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY max_trip_distance DESC
LIMIT 1;
```

<br>

## Question 5. Biggest pickup zone

Which was the pickup zone with the largest `total_amount` (sum of all trips) on November 18th, 2025?

- **East Harlem North** ✔️
- East Harlem South
- Morningside Heights
- Forest Hills

<br>

**My Solution**:

The following SQL query was used in pgAdmin:

```sql
SELECT
	z."Zone" AS pickup_zone,
	SUM(total_amount) AS total_amount
FROM green_taxi_trips AS gt
JOIN zones AS z
ON gt."PULocationID" = z."LocationID"
WHERE DATE(lpep_pickup_datetime) = '2025-11-18'
GROUP BY z."Zone"
ORDER BY total_amount DESC
LIMIT 1;
```

<br>

## Question 6. Largest tip

For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?

Note: it's `tip` , not `trip`. We need the name of the zone, not the ID.

- JFK Airport
- **Yorkville West** ✔️
- East Harlem North
- LaGuardia Airport

<br>

**My Solution**:

The following SQL query was used in pgAdmin:

```sql
SELECT
	dz."Zone" AS dropoff_zone,
	gt.tip_amount
FROM green_taxi_trips AS gt
JOIN zones AS pz
ON gt."PULocationID" = pz."LocationID"
JOIN zones AS dz
ON gt."DOLocationID" = dz."LocationID"
WHERE 
	pz."Zone" = 'East Harlem North'
	AND EXTRACT(YEAR FROM gt.lpep_pickup_datetime) = 2025
	AND EXTRACT(MONTH FROM gt.lpep_pickup_datetime) = 11
ORDER BY gt.tip_amount DESC
LIMIT 1;
```

<br>

## Terraform

In this section homework we'll prepare the environment by creating resources in GCP with Terraform.

In your VM on GCP/Laptop/GitHub Codespace install Terraform.
Copy the files from the course repo
[here](../../../01-docker-terraform/terraform/terraform) to your VM/Laptop/GitHub Codespace.

Modify the files as necessary to create a GCP Bucket and Big Query Dataset.


## Question 7. Terraform Workflow

Which of the following sequences, respectively, describes the workflow for:
1. Downloading the provider plugins and setting up backend,
2. Generating proposed changes and auto-executing the plan
3. Remove all resources managed by terraform`

Answers:
- terraform import, terraform apply -y, terraform destroy
- teraform init, terraform plan -auto-apply, terraform rm
- terraform init, terraform run -auto-approve, terraform destroy
- **terraform init, terraform apply -auto-approve, terraform destroy** ✔️
- terraform import, terraform apply -y, terraform rm

**My solution**: [Terraform Project](../terraform_workshop)

<br>