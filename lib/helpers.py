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

def interact_with_blog_data():
    while True:
        blog_options_menu()
        user_choice = input("Select an option from the menu: ")
        if user_choice == 'c':
            create_blog()
            break
        elif user_choice == 'v':
            view_blogs()
            break
        elif user_choice == 'pc':
            post_content()
            break
        elif user_choice == 'u':
            update_blog()
            break
        elif user_choice == 'd':
            delete_blog()
            break
        else:
            print("Invalid input! Please try again!\n")
            break

def blog_options_menu():
    print("\nBlog Menu!")
    print("c: Create a new blog")
    print("v: View blog data")
    print("pc: Display post content")
    print("u: Update a blog")
    print("d: Delete a blog\n")

    #blog functions

def view_blogs():
    options_for_view_blogs()
    user_choice = input("Select an option from the menu: ")

    while(True):
        if(user_choice == 'a'):
            print("\nAll Blogs:")
            all_blogs = Blog.get_all()
            print(all_blogs)
            user_choice = input("\nPress 'return' to continue...")
            break
        elif(user_choice == '1'):
            while(True):
                try:
                    user_choice = input("\nEnter the blog id to search: ")
                    user_choice = int(user_choice)
                    blog = Blog.find_by_id(user_choice)
                    if(blog):
                        print("\nSelected Blog:")
                        print(Blog.find_by_id(user_choice))
                    else:
                        print("\nBlog Not Found!")
                    user_choice = input("\nPress 'return' to continue...")
                    break
                except:
                    print("Invalid selection! Please try again!")
                    break
            break
        else:
            print("Invalid selection! Please try again!\n")
            break

def options_for_view_blogs():
    print("\nAll blogs or a blog by id?")
    print("a: View all blogs")
    print("1: View blog by id\n")

def create_blog():
    name = input("Create new Blog category: ")
    new_blog = Blog.create(name)
    print("Name for new Blog category: ")
    print(new_blog)
    user_choice = input("\nPress 'return' to continue...")

def post_content():
    while True:
        try:
            blog_id_input = input("\nEnter the blog id you want to return post titles for (press 'm' to return to main menu): ")
            if blog_id_input.lower() == 'm':
                break
                
            blog_id = int(blog_id_input)
            blog = Blog.find_by_id(blog_id)
            
            if blog:
                print("\nPosts for Blog:", blog.name)
                posts = blog.posts()
                if posts:
                    print("\nPost Titles:")
                    for post in posts:
                        print(f"- {post.title}")
                    input("\nPress 'return' to continue...")
                else:
                    print("No posts found for this blog.")
            else:
                print("\nBlog Not Found!")
        except ValueError:
            print("Invalid input! Please enter a valid blog ID.")
        except Exception as e:
            print("An error occurred:", e)

def update_blog():
    while(True):
        try:
            user_choice = input("\nEnter the blog id to update: ")
            user_choice = int(user_choice)
            blog = Blog.find_by_id(user_choice)
            if(not blog):
                print("\nBlog Not Found!")
            break
        except:
            print("Invalid selection! Please try again!")
        
    updated_blog_name = input("Update Blog Name: ")
    blog.name = updated_blog_name
    blog.update()
    print("Blog name has been updated: ")
    print(blog)
    user_choice = input("\nPress 'return' to continue...")

def delete_blog():
    while(True):
        try:
            user_choice = input("\nEnter the blog id to delete: ")
            user_choice = int(user_choice)
            blog = Blog.find_by_id(user_choice)
            if(blog):
                blog.delete()
                print("Blog has been deleted!")
            else:
                print("\nBlog not found!")
            break
        except:
            print("Invalid selection! Please try again!")
            break