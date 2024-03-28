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
    while True:
        blog_options_menu()
        user_choice = input("Select an option from the menu: ")
        if user_choice == 'c':
            create_blog()
            break
        elif user_choice == 'r':
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
    print("r: View blog data")
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
            for blog in Blog.all:
                print(blog)
            # return to cont
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
    while(True):
                try:
                    user_choice = input("\nEnter the blog id to return posts: ")
                    user_choice = int(user_choice)
                    blog = Blog.find_by_id(user_choice)
                    if(blog):
                        print("\nBlogs Posts:")
                        print(Blog.find_by_id(user_choice))
                        user_choice = input("\nPress 'return' to continue...")
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

  #post functions
        
def interact_with_post_data():
    while(True):
        post_options_menu()
        user_choice = input("Select an option from the menu: ")
        if(user_choice == 'c'):
            create_post()
            break
        elif(user_choice == 'r'):
            view_posts()
            break
        elif(user_choice == 'u'):
            update_post()
            break
        elif(user_choice == 'd'):
            delete_post()
            break
        elif(user_choice == "s"):
            sorted_posts()
            break
        else:
            print("Invalid input! Please try again!\n")
            break
        
def post_options_menu():
    print("\Post Menu!")
    print("c: Create a new post")
    print("r: View post data")
    print("u: Update a post")
    print("d: Delete a post")
    print("s: Sort posts alphabetically\n")

def sorted_posts():
    sorted_posts = Post.sorted_posts()
    # print("Number of sorted posts:", len(sorted_posts))
    print("\nPosts in alphabetical order:")
    for post in sorted_posts:
        print("Post Title:", post.title)
    input("\nPress 'return' to continue...")

def view_posts():
    options_for_view_posts()
    user_choice = input("Select an option from the menu: ")

    while(True):
        if(user_choice == 'a'):
            print("\nAll Posts:")
            for post in Post.all:
                print(post)
            # return to continue
            user_choice = input("\nPress 'return' to continue...")
            break
        elif(user_choice == '1'):
            while(True):
                try:
                    user_choice = input("\nEnter the post id to search: ")
                    user_choice = int(user_choice)
                    post = Post.find_by_id(user_choice)
                    if(post):
                        print("\nSelected Post:")
                        print(Post.find_by_id(user_choice))
                        user_choice = input("\nPress 'return' to continue...")
                        break
                    else:
                        print("\nPost Not Found!")
                    break
                    
                except:
                    print("Invalid selection! Please try again!")
                    user_choice = input("\nPress 'return' to continue...")
                    break
                
        else:
            # print("Invalid! Please try again!\n")
            break
            

def options_for_view_posts():
    print("\nWould you like to see all your posts or a post by id?")
    print("a: View all posts")
    print("1: View post by id\n")

def create_post():
    name = input("Create new Post to Blog: ")
    new_post = Post.create(name)
    print("Title for new Post ")
    print(new_post)
    user_choice = input("\nPress 'return' to continue...")


def update_post():
    while True:
        try:
            user_choice = input("\nEnter the post id to update: ")
            user_choice = int(user_choice)
            post = Post.find_by_id(user_choice)
            if not post:
                print("\nPost Not Found!")
                break
        except:
            print("Invalid! Please try again!")
            break

        
    updated_post_name = input("Update Post Name: ")
    post.name = updated_post_name
    post.update()
    print("Post name has been updated: ")
    print(post)
    user_choice = input("\nPress 'return' to continue...")

def delete_post():
    while(True):
        try:
            user_choice = input("\nEnter the post id to delete: ")
            user_choice = int(user_choice)
            post = Post.find_by_id(user_choice)
            if(post):
                post.delete()
                print("Post has been deleted!")
            else:
                print("\nPost not found!")
            break
        except:
            print("Invalid! Please try again!")
            break