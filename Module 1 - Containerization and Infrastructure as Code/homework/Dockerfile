# Base image
FROM python:3.13.11-slim

# Copy the UV binary from the official docker image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set the working directory
WORKDIR /app

# Prioritize the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency files to the working directory in container
COPY .python-version pyproject.toml uv.lock ./
# Install dependencies from uv.lock file
RUN uv sync --locked

# Copy the application code to the working directory in container
COPY ingest_data.py ./

# Set the entry point command to run the application
ENTRYPOINT ["python", "ingest_data.py"]