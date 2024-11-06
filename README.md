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


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

[For email sending functionality obtain a SendGrid Account, Single Sender Address, and API Key]
(https://login.twilio.com/u/signup?state=hKFo2SBncmVNMFZvcEZTNV9Yd3R0d2hVZVNUaEt4RlRVSnBqZaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIDVVd053ci1iZVFJWjFTSllMNkVQOVpRdWg3ZlVWcGdFo2NpZNkgR244UWMyZ1FOa2trZ0llT2s4QlJqRWZ5eWNoMTU2VUk)
First, sign up for a SendGrid account, and click the verification link sent to your email address.

Then follow the instructions to complete your "Single Sender Verification", and click the verification link sent in another confirmation email to verify your single sender address (i.e. the SENDGRID_SENDER_ADDRESS). You should be able to access these settings via the "Sender Authentication" section of the settings menu.

(https://app.sendgrid.com/settings/api_keys)
Finally, create a SendGrid API Key with "full access" permissions (i.e. the SENDGRID_API_KEY). You should be able to access these settings via the "API Keys" section of the settings menu.

Finally, create a SendGrid API Key with "full access" permissions (i.e. the SENDGRID_API_KEY). You should be able to access these settings via the "API Keys" section of the settings menu. 


Create a ".env" file and add contents like the following (using your own AlphaVantage API Key, SendGrid single sender addres and API Key):

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
python app/stocks.py
```

Run the example email sending file:
```
python app/email_service.py
```