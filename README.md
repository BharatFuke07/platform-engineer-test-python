# Platform Engineer Test - Starter Project

## Prerequisites

### Python 3.6 to 3.9

See [installation instructions](https://www.python.org/downloads/).

Check you have python3 installed. **Make sure your python version is between 3.6 and 3.9. This is required for compatibility with the Snowflake Python Connector**:

```bash
python3 --version
```

### IDE

Preferably an IDE such as [VSCode](https://code.visualstudio.com/) or [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/)

## Dependencies and data

### Creating a virtual environment

Ensure your pip (package manager) is up to date:

```bash
pip3 install --upgrade pip
```

To check your pip version run:

```bash
pip3 --version
```

Create the virtual environment in the root of the cloned project:

```bash
python3 -m venv .venv
```

### Activating the newly created virtual environment

You always want your virtual environment to be active when working on this project.

```bash
source ./.venv/bin/activate
```

### Installing Python requirements

This will install some of the packages you might find useful:

```bash
pip3 install -r ./requirements.txt
```

### Environment Variables

Create a placeholder file: `.env` in the top-level of the repository, alongside the `README.md`, `requirements.txt` etc... files. We are going to be storing your login credentials in this file, so make sure you edit the permissions on this file to secure it.

```bash
touch .env
chmod 600 .env
```

Populate this file with the values that you have been provided:

```bash
SNOWFLAKE_USER=YOUR_PROVIDED_USER_NAME
SNOWFLAKE_PASSWORD=my_dummy_not_secure_password
SNOWFLAKE_ACCOUNT=the_account_name
```

### Running tests to ensure everything is working correctly

```bash
pytest ./tests -v 
```

### Getting started

The skeleton of a possible solution is provided in `./solution/solution_start.py`
You do not have to use this code if you want to approach the problem in a different way.
