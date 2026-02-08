##########################  Define Provider  #########################################
# Terraform provider for Google Cloud: https://registry.terraform.io/providers/hashicorp/google/latest/docs
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.18.0"
    }
  }
}

provider "google" {
  # Configuration options
  credentials = var.credentials
  project     = var.project_id
  region      = var.region
}

# This data source gets a temporary token for the service account
 data "google_service_account_access_token" "default" {
   provider               = google
   target_service_account = var.service_account_email
   scopes                 = ["https://www.googleapis.com/auth/cloud-platform"]
   lifetime               = "3600s"
 }
 
 # This second provider block uses that temporary token and does the real work
 provider "google" {
   alias        = "impersonated"
   access_token = data.google_service_account_access_token.default.access_token
   project      = var.project_id
   region       = var.region
 }


##########################  Define Resources  #########################################

# Define a resource for GCS bucket: https://registry.terraform.io/providers/hashicorp/google/4.35.0/docs/resources/storage_bucket#example-usage---life-cycle-settings-for-storage-bucket-objects
# Define the GCS bucket "google_storage_bucket.terraform_demo_bucket"
resource "google_storage_bucket" "terraform_demo_bucket" {
  name          = var.gcs_bucket_name # bucket name has to be globally unique
  location      = var.location
  force_destroy = true
  storage_class = var.gcs_storage_class

  lifecycle_rule {
    condition {
      age = 3 # Age in days
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload" # Abort incomplete multipart (partition) uploads after 1 day
    }
  }
}

# Define a resource for BigQuery dataset: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset#example-usage---bigquery-dataset-basic
# Define the BigQuery dataset "google_bigquery_dataset.terraform_demo_dataset"
resource "google_bigquery_dataset" "terraform_demo_dataset" {
  dataset_id = var.bigquery_dataset_id
  location   = var.location
}