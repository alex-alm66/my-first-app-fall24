# my-first-app-fall24

## Setup

Create and activate a virtual environment:

```sh
conda create -n reports-env-2024 python=3.10
```

Activate the environment:

```sh
conda activate reports-env-2024
```

Install packages:

```sh
pip install -r requirements.txt
```


## Usage

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
ALPHAVANTAGE_API_KEY="..." python app/unemployment.py
```