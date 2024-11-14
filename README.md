# my-first-app-fall-2024

## Setup

Create a virtual environment (first time only):

```sh
conda create -n reports-env-2024 python=3.10
```

Activate the environment (whenever you come back to this project):

```sh
conda activate reports-env-2024
```

Install packages:

```sh
pip install -r requirements.txt
```

Obtaining API Keys from Alphavantage and SendGrid:

[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage by filling out the form at the aforementioned link.

Sign up for a [SendGrid account](https://signup.sendgrid.com/) and click the verification link sent to your email address. Then follow the instructions to complete your "Single Sender Verification", and click the verification link sent in another confirmation email to verify your single sender address (i.e. the ```SENDGRID_SENDER_ADDRESS```). You should be able to access these settings via the "Sender Authentication" section of the settings menu. Lastly, [create a SendGrid API Key](https://app.sendgrid.com/settings/api_keys) with "full access" permissions (i.e. the ```SENDGRID_API_KEY```). You should be able to access these settings via the "API Keys" section of the settings menu.

Next, create your own ".env" file in your repository folder and add the following contents (your own AlphaVantage API Key, SendGrid single sender address and API Key):

```sh
# this is the ".env" file:
ALPHAVANTAGE_API_KEY="______"

SENDGRID_API_KEY="______"
SENDGRID_SENDER_ADDRESS="______"
```

## Usage

Run the example script:

```sh
python app/my_script.py
```

Run the unemployment report:

```sh
#ALPHAVANTAGE_API_KEY="..." python app/unemployment.py

python app/unemployment.py
```

Run the stocks report:

```sh
python -m app.stocks
```

Run the example email sending file:
```
python app/email_service.py
```

Run the stocks report:

```sh
python -m app.stocks
```

Run the example rock, paper, scissors game:
```
python app/rps.py
```

## Testing

Run tests:

```sh
pytest
```