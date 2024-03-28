# lib/helpers.py
from models.blog import Blog
from models.post import Post

def initialize_database():
    Blog.create_table()
    Post.create_table()

    Blog.get_all
    Post.get_all

def exit_program():
    print("Ciao!\n")
    quit()
