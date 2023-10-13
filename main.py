import sys
from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv

def main():
    """
        The main entry point for the movie database application.

        This function handles the initialization of storage, whether it's based on command-line arguments or user input.
        It allows users to choose between different storage options and family member storage.
        After selecting the storage, it creates a MovieApp object and runs the application.

        Returns:
            None
        """
    if len(sys.argv) == 2:
        storage_file = sys.argv[1]
        # Determine storage type from the file extension
        storage_type = "JSON" if storage_file.lower().endswith(".json") else "CSV"
        print(f"Using {storage_type} storage")

        if storage_type == "JSON":
            storage = StorageJson(storage_file)
        elif storage_type == "CSV":
            storage = StorageCsv(storage_file)
        else:
            print("Invalid file extension. Please use JSON or CSV files.")
            return
    else:
        print("######## Movie Database ########")
        storage_option = int(input("Enter the number 1 to choose JSON and 2 for CSV file format: "))
        if storage_option == 1:
            storage = StorageJson('movies.json')
        elif storage_option == 2:
            storage = StorageCsv('movies.csv')
        else:
            print("Invalid choice. Please enter 1 for JSON or 2 for CSV.")
    family_storage = {
        'John': StorageJson('john.json', 'John'),
        'Sara': StorageJson('sara.json', 'Sara'),
        'Jack': StorageJson('jack.json', 'Jack')
    }

    family_option = int(input("Enter the number 3 to work with family members' storage or 1 for Json and 2 for CSV default storage: "))

    if family_option ==3:
        print("Choose a Family member: ")
        for index, (family_member, _) in enumerate(family_storage.items(), 1):
            print(f"{index}. {family_member}")

        choice = int(input("Enter the number of the family member: "))


        if choice < 1 or choice > len(family_storage):
            print("Invalid choice. Please choose a valid family member.")
        else:
            selected_family_member = list(family_storage.keys())[choice - 1]
            selected_file = family_storage[selected_family_member]
            storage = selected_file
            print(f'You are working on {selected_family_member} files.')
    else:
        print(f'Working with default Json/CSV storage.')

    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
