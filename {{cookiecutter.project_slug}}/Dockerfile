FROM continuumio/miniconda3

# Set the working directory
WORKDIR /app

# Copy the code
COPY . .

# Install dependent libraries
RUN apt-get update && \
    apt-get install make

# Create the environment
RUN make install

# Expose the API port
EXPOSE 8000

# Set the entrypoint
ENTRYPOINT ["conda", "run", "-n", "mlops", "uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]