from models.post import Post

  #post functions
        
def interact_with_post_data():
    while(True):
        post_options_menu()
        user_choice = input("Select an option from the menu: ")
        if(user_choice == 'c'):
            create_post()
            break
        elif(user_choice == 'v'):
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
    print("\nPost Menu!")
    print("c: Create a new post")
    print("v: View post data")
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
            all_posts = Post.get_all()
            print(all_posts)
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