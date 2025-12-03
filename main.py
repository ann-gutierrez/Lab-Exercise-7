from reflections_utils import *

REFLECTIONS_FILE = "reflections.txt"

def display_menu():
    print("---------- QUIETMIND REFLECTION LOG ----------")
    print("1. Add a New Reflection")
    print("2. View All Reflections")
    print("3. Search Reflections")
    print("4. Exit")

def get_menu_choice():
    while True:
        try:
            choice = input("Enter your choice: ").strip()
            choice_number = int(choice)

            if 1 <= choice_number <= 4:
                return choice_number
            else:
                print("INVALID CHOICE! Please enter a number between 1 and 4.")
                input("Press Enter to continue...")

        except ValueError:
                print("INVALID CHOICE! Please enter a number between 1 and 4.")
                input("Press Enter to continue...")

        except KeyboardInterrupt:
                print("\n Session Interrupted! Exiting Program...")
                return 4

def add_reflection():
    print("Please Enter your Reflection: ")

    try:
        reflection_text = input().strip()

        if not reflection_text:
            print("ERROR: Please enter a Reflection Text. Reflection Text cannot be empty.")
            return

        print("Saving your reflection...")
        save_reflection(REFLECTIONS_FILE,reflection_text)
        print("Reflection Saved!")

    except ValueError as e:
        print(f"ERROR: {e}")
    except PermissionError as e:
        print(f"ERROR: {e}")
    except Exception as e:
        print(f"UNEXPECTED ERROR: {e}")

    input("Press Enter to return to Main Menu...")

def view_reflections():
    print("\n ----- Saved Reflections -----")

    try:
        reflections = read_reflection(REFLECTIONS_FILE)

        if not reflections:
            print("No reflections found yet. Try adding one!")
        else:
            for reflection in reflections:
                print(reflection)

    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    print()
    input("Press Enter to return to Main Menu...")

def search_reflections():
    print("\n ----- Search for a Reflection -----")
    print("\n Please Enter a Keyword to Search: ", end="")

    try:
        keywords = input().strip()

        if not keywords:
            print("ERROR: Please enter a Keyword to Search. Keywords cannot be empty.")
            return

        print("Searching Reflections...")
        
        all_reflections = read_reflection(REFLECTIONS_FILE)

        if not all_reflections:
            print("No reflections found yet. Try adding one!")
            return

        matches = search_reflections(keywords, all_reflections)

        if not matches:
            print(f"No reflections found with {keywords}.")
        else:
            print(f"Found {len(matches)} reflections with {keywords}.")
            for reflection in matches:
                print(reflection)

    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    print()
    input("\nPress Enter to return to Main Menu...")

