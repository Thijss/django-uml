# django-uml
`django-uml` is a boilerplate project for generating UML diagrams using Django.

The project utilizes `django-extensions`'s `graph_model` command to generate UML diagrams.


**Note:** The project itself is not meant to run as a web application. Therefore, all files/settings
that are normally used when setting up a Django web application, have been removed.


## How to use this project
1. Add your apps and models to the project
2. Run `python manage.py uml` to generate a PNG-file depicting your UML diagram.

## Quickstart
Since there is an `example` app within the project, 
you can follow these instructions to get started quickly:

1. Clone the repository
    ```bash
    git clone https://github.com/Thijss/django-uml.git <your_project_name>
    ```

2. Create and activate a virtualenv:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
    
3. Install the requirements using either `poetry` or `pip`:
    
    ```bash
    poetry install
    ```
    
    or
    
    ```bash
    pip install -r requirements.txt
    ```
    
4. Copy `.env.example` to `.env` to set your environment variables:

    ```bash
    cp .env.example .env
    ```

5. Run the migrations on your database:

    ```bash
    python manage.py migrate
   ```

6. Run the command to generate a UML:

    ```bash
    python manage.py uml
    ```

7. You should now have a UML.png file in `.exports/`

## Example UML.png

![UML diagram](.examples/UML.png?raw=true "UML diagram")
