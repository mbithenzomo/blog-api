# Blog API

This is an API that exposes articles and categories for a blog. It has the following functionality:

1. Admin user - create using command line
* log in
* create, view, edit, delete article
* create, view, edit, delete category

2. Category - name

3. Article - writer (foreign key), title, content, category (foreign key), image

4. Permissions:
* only admin can create, edit, and delete articles and categories
* no login required for viewing articles
