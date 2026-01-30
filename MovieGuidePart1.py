# Name: Axel Cordova
# Course: CIS261
# Lab Title: MovieGuidePart1

def display_menu():
    print("The Movie List\n")
    print("COMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")

def prepopulate_movies():
    # Minimum of 3 titles
    return ["The Matrix", "Interstellar", "Spider-Man: Into the Spider-Verse"]

def list_movies(movies):
        print("\nMovie Titles")
        for i, title in enumerate(movies, start=1):
            print(f"{i}. {title}")

def add_movie(movies):
    title = input("Movie: ").strip()
    if title == "":
        print("Movie title cannot be blank.")
        return
    movies.append(title)
    print(f"{title} was added.")


def delete_movie(movies):
    num_str = input("Number: ").strip()

    # invalid number check
    if not num_str.isdigit():
        print("Invalid number.")
        return
    
    num = int(num_str)
    index = num - 1

    if index < 0 or index >= len(movies):
        print("Invalid movie number.")
        return

    removed = movies.pop(index)
    print(f"{removed} was deleted.")

def main():
    movies = prepopulate_movies()
    display_menu()
    
    while True:
        command = input("\nCommand: ").strip().lower()
    
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
            list_movies(movies)   # show list after add
        elif command == "del":
            delete_movie(movies)
            list_movies(movies)   # show list after delete
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")
if __name__ == "__main__":
    main()
