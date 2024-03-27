# lib/helpers.py
from models.blog import Blog
from models.post import Post

def initialize_database():
    Blog.create_table()
    Post.create_table()

    Blog.get_all
    Post.get_all

def exit_program():
    print("Bye!\n")
    quit()

def interact_with_blog_data():
    while(True):
        blog_options_menu()
        user_input = input("Select an option from the menu: ")
        if(user_input == 'c'):
            create_blog()
            break
        elif(user_input == 'r'):
            view_blogs()
            break
        elif(user_input == 'pc'):
            post_content()
            break
        elif(user_input == 'u'):
            update_blog()
            break
        elif(user_input == 'd'):
            delete_blog()
            break
        else:
            print("Invalid input! Please try again!\n")
            break

def blog_options_menu():
    print("\nBlog Menu!")
    print("c: Create a new blog")
    print("r: View blog data")
    print("pc: Display post content")
    print("u: Update a blog")
    print("d: Delete a blog\n")

    #blog functions

def view_blogs():
    options_for_view_blogs()
    user_input = input("Select an option from the menu: ")

    while(True):
        if(user_input == 'a'):
            print("\nAll Blogs:")
            for blog in Blog.all:
                print(blog)
            # return to cont
            user_input = input("\nPress 'return' to continue...")
            break
        elif(user_input == '1'):
            while(True):
                try:
                    user_input = input("\nEnter the blog id to search: ")
                    user_input = int(user_input)
                    blog = Blog.find_by_id(user_input)
                    if(blog):
                        print("\nSelected Blog:")
                        print(Blog.find_by_id(user_input))
                    else:
                        print("\nBlog Not Found!")
                    user_input = input("\nPress 'return' to continue...")
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
    user_input = input("\nPress 'return' to continue...")

def post_content():
    while(True):
                try:
                    user_input = input("\nEnter the blog id to return posts: ")
                    user_input = int(user_input)
                    blog = Blog.find_by_id(user_input)
                    if(blog):
                        print("\nBlogs Posts:")
                        print(Blog.find_by_id(user_input))
                        user_input = input("\nPress 'return' to continue...")
                        break
                    else:
                        print("\nBlog Posts Not Found!")
                        break
                except:
                    print("Invalid selection! Please try again!")
                    break

def update_blog():
    while(True):
        try:
            user_input = input("\nEnter the blog id to update: ")
            user_input = int(user_input)
            blog = Blog.find_by_id(user_input)
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
    user_input = input("\nPress 'return' to continue...")

def delete_blog():
    while(True):
        try:
            user_input = input("\nEnter the blog id to delete: ")
            user_input = int(user_input)
            blog = Blog.find_by_id(user_input)
            if(blog):
                blog.delete()
                print("Blog has been deleted!")
            else:
                print("\nBlog not found!")
            break
        except:
            print("Invalid selection! Please try again!")
            break

            #post functions
        
def interact_with_post_data():
    while(True):
        post_options_menu()
        user_input = input("Select an option from the menu: ")
        if(user_input == 'c'):
            create_post()
            break
        elif(user_input == 'r'):
            view_posts()
            break
        elif(user_input == 'u'):
            update_post()
            break
        elif(user_input == 'd'):
            delete_post()
            break
        else:
            print("Invalid input! Please try again!\n")
            break
        
def post_options_menu():
    print("\Post Menu!")
    print("c: Create a new post")
    print("r: View post data")
    print("u: Update a post")
    print("d: Delete a post\n")

def view_posts():
    options_for_view_posts()
    user_input = input("Select an option from the menu: ")

    while(True):
        if(user_input == 'a'):
            print("\nAll Posts:")
            for post in Post.all:
                print(post)
            # return to cont
            user_input = input("\nPress 'return' to continue...")
            break
        elif(user_input == '1'):
            while(True):
                try:
                    user_input = input("\nEnter the post id to search: ")
                    user_input = int(user_input)
                    post = Post.find_by_id(user_input)
                    if(post):
                        print("\nSelected Post:")
                        print(Post.find_by_id(user_input))
                        user_input = input("\nPress 'return' to continue...")
                        break
                    else:
                        print("\nPost Not Found!")
                    break
                    
                except:
                    print("Invalid selection! Please try again!")
                    user_input = input("\nPress 'return' to continue...")
                    break
                
        else:
            # print("Invalid selection! Please try again!\n")
            break
            

def options_for_view_posts():
    print("\nWould you like to see all your posts or a post by?")
    print("a: View all posts")
    print("1: View post by id\n")

def create_post():
    name = input("Create new Post category: ")
    new_post = Post.create(name)
    print("Name for new Post category: ")
    print(new_post)
    user_input = input("\nPress 'return' to continue...")


def update_post():
    while True:
        try:
            user_input = input("\nEnter the post id to update: ")
            user_input = int(user_input)
            post = Post.find_by_id(user_input)
            if not post:
                print("\nPost Not Found!")
                break
        except:
            print("Invalid selection! Please try again!")
            break

        
    updated_post_name = input("Update Post Name: ")
    post.name = updated_post_name
    post.update()
    print("Post name has been updated: ")
    print(post)
    user_input = input("\nPress 'return' to continue...")

def delete_post():
    while(True):
        try:
            user_input = input("\nEnter the post id to delete: ")
            user_input = int(user_input)
            post = Post.find_by_id(user_input)
            if(post):
                post.delete()
                print("Post has been deleted!")
            else:
                print("\nPost not found!")
            break
        except:
            print("Invalid selection! Please try again!")
            break
    