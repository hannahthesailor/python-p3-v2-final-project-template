# lib/helpers.py
from models.blog import Blog
from models.post import Post

def initialize_database():
    Blog.create_table()
    Post.create_table()

    Blog.get_all
    Post.get_all
    
def menu():
    print("\nMain Menu")
    print("b: Blog data")
    print("p: Post data")
    print("q: Quit the program\n")

def exit_program():
    print("Bye!\n")
    quit()
# def helper_1():
#     print("Performing useful function#1.")


# def exit_program():
#     print("Goodbye!")
#     exit()
