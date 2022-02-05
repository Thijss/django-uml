# django-uml
`django-uml` is a template repository for generating UML diagrams using Django.

The project utilizes `django-extensions`'s `graph_model` command to generate UML diagrams.


**Note:** The project itself is not meant to run as a web application. Therefore, all files/settings
that are normally used when setting up a Django web application, have been removed.


## How to use this project
1. Add your apps and models to the project
2. Run `python manage.py uml` to generate a PNG-file depicting your UML diagram.

## Prerequisites
This project expects the user to have `poetry` installed, to install it's requirements.

You can install poetry from [here](https://python-poetry.org/docs/master/#installation)

## Quickstart
Since there is an `example` app within the project, 
you can follow these instructions to get started quickly:

1. Click on the [**Use this template**] button and create your repositort

1. Clone your repository
    ```bash
    git clone https://github.com/Thijss/<your_repo_name>.git
    ```
    
1. Install the requirements using `poetry` (`poetry` will create a virtualenv for you):
    
    ```bash
    poetry install
    ```

1. Copy `.env.example` to `.env` to set your environment variables:

    ```bash
    cp .env.example .env
    ```

1. Run the migrations on your database:

    ```bash
    python manage.py migrate
   ```

1. Run the command to generate a UML:

    ```bash
    python manage.py uml
    ```

1. You should now have a UML.png file in `.exports/`

## Example UML.png

![UML diagram](.examples/UML.png?raw=true "UML diagram")
