# Phase 3 Project


## Personal Blog

My project is a database of a personal blog with different blog categories containing multiple unique blog entries within each category. The blog has many posts, the post have one blog category they belong to making this a one-to-many type of relationship!

## Start the Program

To begin fork, clone, and open the repository

don't forget to run in the terminal

```
pipenv install
pipenv shell
```

---

## Generating CLI

In the terminal, to run the CLI:

```
python lib/cli.py
```

Then you can follow along with the promts within the terminal to navigate through the data

### About the code

In the CLI file we are importing functions to exit the program, initialize the database, and interact with the blog and post data. The "main()" is the entry point of the program. When the database is initialized it enters an infinite loop (the menu) wher you can interact with the data or exit.

In the helpers file we house functions that interact with the blog and post data and create menu options for the data. Each function is titled in a manner to clearly convey what purpose it is serving. These allow us to interact with the data through a command line interface. Things like create, view, update, delete, are included among these functions.

In post.py we define a Python class "Post", which represents a post in a blog. The "all = []" is a class attribute list that contains all instances of the "Post" class.  The constructor __init__ initilazies a post object with attributes (title, text, blog_id). The property setter is used on each attribute to ensure they behave in a specified way I have chosen, such as if the input is an itneger or string, how long a title can be, ect. Then using CRUD methods to manipulate the table and data.

In blog.py again defining a Python class "Blog" representing a blog. Property setter to set the name. __repr__ returns a string of the blog object including its id and name. The ORM Methods again named to convey their fuction. Creating a table, droping a table. create a block, retrieve all blogs or a specific blog. The post method returns all posts that belong to a specific blog.