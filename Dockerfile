# Use the stable, lightweight Python base image
FROM python:3.12-slim

# Set the working directory (best practice)
WORKDIR /app

# Copy the dependency list first (needed for the next step)
COPY requirements.txt requirements.txt

# Install dependencies. This now succeeds because psycopg2-binary is used.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code (app.py, templates, static, boot.sh)
COPY . .

# Ensure the startup script is executable
RUN chmod a+x boot.sh

# The entry point for the application runner
ENTRYPOINT ["./boot.sh"]