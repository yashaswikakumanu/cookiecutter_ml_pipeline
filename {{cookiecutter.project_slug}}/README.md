# {{ cookiecutter.project_name }}
{{ cookiecutter.project_short_description }}

## Prerequisites

1. Install make package

```bash
conda install make
```

## Getting Started

Navigate to Makefile directory and get started with below steps

1. Install the dependencies and activate environment: \
    `make install` \
    `conda activate mlops` \
    `pip install -r requirements.txt`
2. Run the tests: `make test`
3. Build the Docker image: `make build`
4. Start the API server: `make up`

## Requirements

- Python 3.10
- Conda


# Usage

## API

To start the API, run the following command:
```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 8000
```

Once the API is running, you can make predictions by sending a POST request to the `/predict` endpoint. The request body should contain a JSON object with the input data for the prediction.

For example, to make a prediction for a single sample, you might send a request like this:

```bash
curl -X POST \
  http://localhost:8000/predict \
  -H 'Content-Type: application/json' \
  -d '{ "input_1": 0.5, "input_2": 0.6, "input_3": 0.7 }'
```

The response will be a JSON object with the prediction result.
```bash
{ "prediction": 0.8 }
```

You can also make predictions for multiple samples by sending a request like this:
```bash
curl -X POST \
  http://localhost:8000/predict \
  -H 'Content-Type: application/json' \
  -d '[{ "input_1": 0.5, "input_2": 0.6, "input_3": 0.7 }, { "input_1": 0.6, "input_2": 0.7, "input_3": 0.8 }]'
```

The response will be a JSON array with the prediction results for each sample.
```bash
[{ "prediction": 0.8 }, { "prediction": 0.9 }]
```
Note that the input keys (e.g. "input_1", "input_2", etc.) may vary depending on the specific model and input data used.

## Data

To preprocess the raw data, run the following command:
```bash
python -m src.data.preprocess
```

To ingest new data, run the following command:
```bash
python -m src.data.ingest
```

## Models

To train a new model, run the following command:
```bash
python -m src.models.train
```

To evaluate the performance of a trained model, run the following command:
```bash
python -m src.models.evaluate
```

## Tests

To run the tests, run the following command:
```bash
pytest
```

## Documentation

To build the documentation, run the following command:
```bash
cd docs && make html
```

The documentation will be built in the docs/_build/html directory.

<!-- TODO: hyperlink license file -->
## License

This project is licensed under the MIT License - see the LICENSE file for details.
