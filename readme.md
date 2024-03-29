
# Seir-Seal Project 4

- **Jeff McDonald** (2024-03-27)

- **App Name:** MLB Stats
- **Description:** Historical Statisicts on Major League Baseball

- **Github Backend:** 
- **Deployed Backend:** 

- **Github Frontend:** 
- **Deployed Frontend:** 

- **Miro Board:** https://miro.com/app/board/uXjVKarxPOI=/
    - #### ERD (Entity Relationship Diagram)
    - #### My diagram showing the models and relationships between them.

## List of Dependencies

##### Backend (python-django)

- django
- asgiref
- dj-database-url
- Django
- django-cors-headers
- django-environ
- djangorestframework
- gunicorn
- packaging
- pip
- psycopg2-binary
- setuptools
- sqlparse
- typing_extensions


##### Frontend (React)

- react
- react-dom
- react-router-dom
- milligram

## Route Map

| Route Name | Endpoint | Method | Decsription |
|------------|----------|--------|-------------|
| Index | /mountains | GET | Renders team details |
| New | /mountains/new | GET | Display a form to add new players |
| Delete | /mountains/:id | DELETE | Remove a particular player then redirect |
| Update | /mountains/:id | PUT | Update a particular player then redirect |
| Create | /mountains | GET | Add a new player to the database then redirect |
| Edit | /mountains/:id/edit | POST | Show edit form for one player |
| Show | /mountains/:id | GET | Show info about one player |
| Create User | /auth/signup/ | POST | User create account |
| User Login | /auth/login/ | POST | User sign into account |


| Endpoint | Method | Response | Other |
| -------- | ------ | -------- | ----- |
| /item | GET | JSON of all items | |
| /item | POST | Create new item return JSON of new item | body must include data for new item |
| /item/:id | GET | JSON of item with matching id number | |
| /item/:id | PUT | update item with matching idea, return its JSON | body must include updated data |
| /item/:id | DELETE | delete the item with the matching id | |
| /auth/signup | POST | creates new user account returns user JSON | new user info must be included in body |
| /auth/login | POST | logs in user and returns user JSON with JWT token | username and password must be included in body |


## Design Mockups (Mobile & Desktop)

##### Mobile Design

![Mobile Design Mockup](https://i.imgur.com/lw1B6J0.png)

##### Desktop Design

![Desktop Design Mockup](https://i.imgur.com/B9EXxQb.png)


