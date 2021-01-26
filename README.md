# django-uml
`django-uml` is a boilerplate project for generating UML diagrams using Django.

The project utilizes `django-extensions`'s `graph_model` command to generate UML diagrams.


**Note:** The project itself is not meant to run as a web application. Therefore, all files/settings
that are normally used when setting up a web application, have been removed.


## How to use this project
1. Add your apps and models to the project
2. Run `python manage.py uml` to generate a PNG-file depicting your UML diagram.

## Quickstart
Since there is an `example` app within the project, 
you can follow these instructions to get started quickly:

1. Clone the repository

2. Install the requirements using either `poetry` or `pip`:
    
    `poetry install`
    
    or
    
    `pip install -r requirements.txt`

3. Copy `.env.example` to `.env` to set your environment variables:

    `cp .env.example .env`
 
4. Run the migrations on your database:

    `python manage.py migrate`
   
5. Run the command to generate a UML:

    `python manage.py uml`
    
6. You should now have a UML.png file in `.exports`

## Example UML file

![UML diagram](.examples/UML.png?raw=true "UML diagram")
