# lib/cli.py

from helpers import (
    exit_program,
    initialize_database,
    interact_with_blog_data,
    interact_with_post_data
)


def main():
    initialize_database()

    while True:
        menu()
        choice = input("Select Option")
        if choice == "q":
            exit_program()
        elif choice == "b":
            interact_with_blog_data()
        elif choice == "p":
            interact_with_post_data()
        else:
            print("Invalid option!")


def menu():
    print("\nMain Menu")
    print("b: Blog data")
    print("p: Post data")
    print("q: Quit the program\n")


if __name__ == "__main__":
    main()
