# The Dockerfile is used to create a custom Docker image.

# Base image
FROM python:3.13.11-slim

# Copy the uv binary "/uv" from the official uv image to the "/bin/" folder (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin

# Set working directory
WORKDIR /app

# Modify the PATH to prioritize the virtual environment
# All commands executed in the container will prefer using the Python version and packages from the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency files first to the working directory in container
COPY .python-version pyproject.toml uv.lock ./
# Install dependencies from the "uv.lock" file
RUN uv sync --locked

# Copy the application code to the working directory in container
COPY NY_Taxi_Data_Ingestion.py ./

# Set the entry point for the container to run the data pipeline
ENTRYPOINT ["python", "NY_Taxi_Data_Ingestion.py"]