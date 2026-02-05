##########################  Define Provider  #########################################
# Terraform provider for Google Cloud: https://registry.terraform.io/providers/hashicorp/google/latest/docs
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "7.18.0"
    }
  }
}

provider "google" {
  # Configuration options
  credentials = "./keys/gcp_credentials.json"
  project     = "ny-taxi-de-zoomcamp-486111"
  region      = "us-central1"
}


##########################  Define Resources  #########################################

# Define a resource for GCS bucket: https://registry.terraform.io/providers/hashicorp/google/4.35.0/docs/resources/storage_bucket#example-usage---life-cycle-settings-for-storage-bucket-objects
# Define the GCS bucket "google_storage_bucket.terraform_demo_bucket"
resource "google_storage_bucket" "terraform_demo_bucket" {
  name          = "ny-taxi-de-zoomcamp-486111-terraform-demo-bucket"   # resource name has to be globally unique
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3      # Age in days
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
      type = "AbortIncompleteMultipartUpload"   # Abort incomplete multipart (partition) uploads after 1 day
    }
  }
}


