# 🐳 Lesson 1 - Docker for Data Engineering

This project demonstrates a containerized data ingestion pipeline using **Docker** and **Docker Compose**. It orchestrates a Python data ingestion script, a PostgreSQL database, and the pgAdmin interface to process and analyse the NY Taxi dataset.

> 📘 **Study Notes:** Check out my detailed learning notes on [here](https://www.notion.so/DE-Zoomcamp-2ed7e1378ad2801ebecad95626440112?source=copy_link).

## 🏗 Architecture

The project consists of three services (or containers) in the same network:

1.  **`pg-database`**: PostgreSQL 18 container (Stores the raw data).
3.  **`ingest-data`**: Custom Python script for data ingestion (Ingests CSV data into Postgres).
2.  **`pgadmin`**: pgAdmin4 Web UI (For complex queries and data management).

[docker-architecture](../assets/docker-architecture.png)

## 🛠 Tech Stack
* **Docker & Docker Compose**: Orchestration and Containerization.
* **uv**: Modern Python package manager for fast dependency resolution.
* **PostgreSQL**: Data Warehousing.
* **Python>=3.13**: Data Ingestion script.
* **pgAdmin 4**: Database GUI.

