FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Create the environment
RUN conda create -n mlops -y python=3.10

# Activate the environment
SHELL ["conda", "run", "-n", "mlops", "/bin/bash", "-c"]

# Copy the code
COPY . .

# Install the packages from the requirements file
RUN conda activate mlops && \
    pip install -r requirements.txt

# Expose the API port
EXPOSE 8000

# Set the entrypoint
ENTRYPOINT ["conda", "run", "-n", "mlops", "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
