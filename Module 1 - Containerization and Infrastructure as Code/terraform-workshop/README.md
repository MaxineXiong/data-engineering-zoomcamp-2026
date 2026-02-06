# Lesson 2 - Terraform Workshop ☁️

This folder contains the Infrastructure as Code (IaC) configuration to provision Google Cloud Platform (GCP) resources using Terraform.

## 📂 Project Structure

* **`main.tf`**: The primary configuration file where resources (Buckets, BigQuery datasets, etc.) are defined.
* **`variables.tf`**: Contains variable definitions to make the code reusable and flexible (e.g., project ID, region).

## 🛠 Prerequisites

Before running the code, you must set up your Google Cloud environment.

### 1. GCP Account & Service Account
1.  Log in to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Navigate to **IAM & Admin** > **Service Accounts**.
3.  Click **Create Service Account** and provide a name (e.g., `terraform-runner`).
4.  **Grant Permissions:** Assign the following roles to the service account:
    * `BigQuery Admin`
    * `Compute Admin`
    * `Service Account Token Creator`
    * `Storage Admin`
5.  Click **Done**.

### 2. Download Credentials
1.  Click on the newly created service account.
2.  Go to the **Keys** tab > **Add Key** > **Create new key**.
3.  Select **JSON** and click **Create**.
4.  Save the downloaded file into this `terraform-workshop/` folder.
    * *Tip: Rename it to something simple like `google_credentials.json`.*

> ⚠️ **IMPORTANT:** Never commit your JSON key to GitHub! Ensure your `.gitignore` file includes `*.json`.

---

## 🚀 Usage

Open your terminal in this directory and run the following commands to manage your infrastructure.

### 1. Initialize
Downloads the Google Provider and sets up the local backend.
```bash
terraform init
```

### 2. Plan
Previews the changes Terraform will make to match your configuration. It shows you what will be created (+), modified (~), or destroyed (-).
```bash
terraform plan
```

### 3. Apply
Executes the plan and actually creates/modifies the resources in Google Cloud.
```bash
terraform apply
# Type 'yes' when prompted to confirm.
```

### 4. Destroy
Removes all resources created by this project. Use this when you are done to avoid incurring costs.
```bash
terraform destroy
# Type 'yes' when prompted to confirm.
```

