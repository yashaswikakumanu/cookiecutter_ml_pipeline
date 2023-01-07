FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the dependencies file
COPY environment.yml .

# Create the environment
RUN conda env create -f environment.yml

# Activate the environment
SHELL ["conda", "run", "-n", "mlops", "/bin/bash", "-c"]

# Copy the code
COPY . .

# Expose the API port
EXPOSE 8000

# Set the entrypoint
ENTRYPOINT ["conda", "run", "-n", "mlops", "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
