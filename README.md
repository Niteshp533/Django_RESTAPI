# Django RESTAPI
Django REST Framework is a toolkit for building REST APIs with Django. In this tutorial, you’ll use Django REST Framework to build a blog API. This API will have endpoints for users, blog posts, comments, and categories.

You’ll also learn how to authenticate user actions to ensure only authenticated users can modify your app’s data.
<img src="https://www.django-rest-framework.org/img/logo.png">
>  This API project demonstrates the following skills:

* Adding new and existing Django models to an API
* Serializing these models using built-in serializers for common API patterns
* Creating views and URL patterns
* Defining many-to-one and many-to-many relationships
* Authenticating user actions

## Setting up the Python environment
> To create a new API project, first set up a Python environment in your working directory. Run the following in your terminal:
On Windows,
* python -m venv env
* .\env\Scripts\activate

Be sure to run all commands in this tutorial from this virtual environment <b>(make sure you see (env) at the beginning of the input line in your terminal)</b>.
> Next, install Django and Django REST framework into the virtual environment:

* pip install django
* pip install djangorestframework

