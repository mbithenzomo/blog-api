# Requirements

1. Admin user - create using command line
* log in
* create, view, edit, delete article
* create, view, edit, delete category

2. Category - name

3. Article - writer (foreign key), title, content, category (foreign key), image

4. Permissions:
* only admin can create, edit, and delete articles and categories
* no login required for viewing articles

# Plan

1. Initial set-up

* Create GitHub repo and clone
* Create feature branch
* Create virtualenv
* Install Django; freeze to req file
* Create project
* Create app
* Install DRF; freeze to req file
* Register apps in settings file

2. Models

* Create tests directory with init file
* Write tests for models
* Run tests, fail
* Write models
* Run migrations
* Run tests, pass

3. Serializers

* Category serializer
* Article serializer

4. Views

* Write tests for views
* Run tests, fail
* Write API views
* Add API routes
* Register API urls on main urls file
* Run tests, pass

5. Bug fixes

6. README.md
