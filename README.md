# Eventex

This project was developed in [Welcome to the Django](http://welcometothedjango.com.br) course

This project consists in system to manage events, ordered by a client.

## Demo

Here's a [link](https://eventex-luiswitz.herokuapp.com/) to my version of Eventex

## Development

Clone the repository
```
git clone https://github.com/luiswitz/eventex.git wttd
cd wttd
```

Create a virtual environment
```console
python -m venv .wttd
```

Enable virtual environment
```console
source .wttd/bin/activate
```

Install dependencies
```console
pip install -r requirements.txt
```

Copy env-sample to .env
```console
cp contrib/env-sample .env
```

Config manage.py
```console
alias manage='python $VIRTUAL_ENV/../manage.py'
```

Run tests
```console
manage test
```

Run server
```console
manage runserver
```
