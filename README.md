# Onidevs Challenge 
- Participant: Joao Victor Ferreira
- **IMPORTANT:** For technical explanation about the project code and access routes, please [CLICK HERE](https://github.com/kizzcross/OniDevs-Challenge/blob/master/TECHNICAL.md) for access the technical markdown.

## Requirements for build/execute:
- [Docker](https://docs.docker.com/get-docker/) (Lastest Version)
- [Docker-Compose](https://docs.docker.com/compose/install/) (Lastest Version) 

## How to build

After have `Docker` and `Docker-Compose` installed, use the command below to build the project instance and the requirements:

```
docker-compose build
```

After the Docker environment finish the project building, run the following command for the first execution:

```
docker-compose up
```

If you don`t want an runtime console of Django envroiment, you can use the flag ``-d`` for run on silent mode (without console logging). Like this example below:

```
docker-compose up -d
```

## How to access the project page

The project page is listened on port ```8000```, you can access with the link: [localhost:8000](http://localhost:8000). 
To acccess the Django Admin page, the link is: [localhost:8000/admin](http://localhost:8000/admin).

The credentials of admin user access is ```admin:admin (user:password)```.

## Python Packages that i used

This packages are automatically builded by docker, you can see their names on the file ``requirements.txt``.

- [Django](https://www.djangoproject.com/) **(required)**
- [Django Admin](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/) **(required)**
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html) **(required)**
- [simplejson](https://pypi.org/project/simplejson/) **(optinally added for fix decimal issues when parsing to json/str)**

## External Sources
Some of them already had been quoted in this project, in the docs of the technologies used.
- [How to Export Your Data as CSV, XLS, or XLSX - DjangoTricks](https://djangotricks.blogspot.com/2013/12/how-to-export-data-as-excel.html)
- [How to export django admin changelist as csv - StackOverflow](https://stackoverflow.com/questions/59574280/how-to-export-django-admin-changelist-as-csv)