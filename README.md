# ChatBoom BE

The fast and right way to start a grace conversation.

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt

$ python manage.py migrate
$ python manage.py runserver
```

## Features

- BE for chat application
- Use Python Channel as a heart of application
- Run CI with pre-commit with flow of tools: black, isort, autoflake (not included). So, before committing code, developers must run these tools to check the validation of pre-commit

## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.
