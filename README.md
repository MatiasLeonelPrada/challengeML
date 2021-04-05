# ChallengeML

This library was made for the "operacion fuego de quasar" challenge for MELI using Python as a lenguage.

## Installation

Requires Python >= 3.8

```
pip install -r requirements.txt
```

## Usage

In order to serve the API, do the following:

### bash:
```
python src/op_fuego_de_quasar.py
```

The API expects a POST request to /topsecret service with a payload like this:
```
{
"satellites": [
		{
			"name": "kenobi",
			"distance": 4.47,
			"message": ["este", "", "", "mensaje", ""]
		},
		{
			"name": "skywalker",
			"distance": 4.12,
			"message": ["", "es", "", "", "secreto"]
		},
		{
			"name": "sato",
			"distance": 3.16,
			"message": ["este", "", "un", "", ""]
		}
	]
}
```

And this is the response for a valid request:
```
{
    "message": "este es un mensaje secreto",
    "position": {
        "x": "2.0",
        "y": "4.0"
    }
}
```

If you want to run the tests you need to install Pytest library:

```
pip install pytest
```

To run the tests do the following on the root folder:

### bash:
```
pytest /tests
```