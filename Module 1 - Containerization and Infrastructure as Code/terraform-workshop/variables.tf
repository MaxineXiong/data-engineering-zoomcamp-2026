variable "location" {
  description = "The location of the resources"
  default     = "US"
}

variable "credentials" {
  description = "Path to the GCP credentials JSON file"
  default     = "./keys/gcp_credentials.json"
}

variable "project_id" {
  description = "The GCP project ID"
  default     = "ny-taxi-de-zoomcamp-486111"
}

variable "region" {
  description = "The GCP region"
  default     = "us-central1"
}

# bucket name has to be globally unique
variable "gcs_bucket_name" {
  description = "The name of the GCS bucket"
  default     = "ny-taxi-de-zoomcamp-486111-terraform-demo-bucket"
}

variable "gcs_storage_class" {
  description = "The storage class of the GCS bucket"
  default     = "STANDARD"
}

variable "bigquery_dataset_id" {
  description = "The ID of the BigQuery dataset"
  default     = "demo_dataset"
}