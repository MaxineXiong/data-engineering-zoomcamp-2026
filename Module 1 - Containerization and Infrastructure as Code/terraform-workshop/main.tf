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
  project     = "ny-taxi-de-zoomcamp-486111"
  region      = "us-central1"
}