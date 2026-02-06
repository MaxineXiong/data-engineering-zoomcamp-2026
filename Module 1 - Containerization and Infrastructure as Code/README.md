# Module 1: Containerization and Infrastructure as Code 🐳🏗️

This repository contains my learning materials and exercises for [Module 1 of the Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform) by [DataTalks.Club](https://datatalks.club/).

In this module, I learned how to containerize applications using Docker and provision infrastructure on Google Cloud Platform (GCP) using Terraform.

## 📂 Project Structure

This folder is organized into three main sections:

### 1. [Docker Workshop](./docker-workshop)
Contains the setup and scripts for running data pipelines in containers.
* **Docker & Docker Compose**: Setting up a local environment with PostgreSQL and pgAdmin.
* **Data Ingestion**: Python scripts to ingest NY Taxi data into the database.
* **SQL Refresher**: Basic SQL queries to explore the dataset.

### 2. [Terraform Workshop](./terraform-workshop)
Contains the Infrastructure as Code (IaC) configuration to manage cloud resources.
* **Terraform Basics**: Understanding `init`, `plan`, `apply`, and `destroy`.
* **GCP Resources**: Provisioning Google Cloud Storage (GCS) buckets and BigQuery datasets.
* **Variables**: Making infrastructure code reusable.

### 3. [Homework for Module 1](./homework)
Contains my solutions for the Module 1 homework assignments.

---

## 🛠 Technologies Used
* **Docker**: For containerization and environment consistency.
* **Terraform**: For provisioning and managing GCP infrastructure.
* **Google Cloud Platform (GCP)**: Cloud provider for storage and compute.
* **PostgreSQL**: Relational database for data storage.
* **pgAdmin**: UI for managing the PostgreSQL database.
* **Python (Pandas)**: For data processing and ingestion.