from statistics import median
import random
import matplotlib.pyplot as plt
class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    # def _command_list_movies(self):
    #     movies = self._storage.list_movies()


    def menu(self):
        """
        Generates the menu text for the movie database application.

        Returns:
            str: The menu text.
        """
        return '''
       ************ My Movies Database ************
    Menu: 
    0. Exit  
    1. List Movies
    2. Add Movie
    3. Delete Movie
    4. Update Movie
    5. Movie Stats
    6. Random Movie
    7. Search Movie
    8. Movies Sorted by Rating
    9. Creating a Rating Histogram 

    Enter choice (0-9):  '''

    def command(self, command):
        """
        Executes the specified command based on user input.

        Args:
            command (int): The user's choice of command (0-9).
        """
        if command == 1:
            self._storage.list_movies()
        elif command == 2:
            self._add_movie()
        elif command == 3:
            self._delete_movie()
        elif command == 4:
            self._update_movie()
        elif command == 5:
            self._command_movie_stats()
        elif command == 6:
            self._random_movie()
        elif command == 7:
            self._search_movie()
        elif command == 8:
            self._sorted_by_rating()
        elif command == 9:
            self._create_rating_histogram()
        elif command == 0:
            print("Bye!")

    def run(self):
        while True:
            command = int(input(self.menu()))
            if 0 <= command <= 9:
                self.command(command)
            else:
                print("Choose between 0 to 9")



    def _add_movie(self):
        """
            Add a new movie to the database.

            This method prompts the user to input the title, rating, release year, and poster URL of a new movie.
            The information provided by the user is then used to add the movie to the database via the storage implementation.

            Args:
                None

            Returns:
                None
            """
        movie_title = input("Insert a name of the movie into the list: ")
        movie_rating = float(input("Provide a rating for the given movie: "))
        movie_year = int(input("Enter the year of the movie: "))
        movie_poster = input("Enter the poster url  of the movie: ")

        self._storage.add_movie(movie_title, movie_year, movie_rating, movie_poster)

    def _delete_movie(self):
        """
            Delete a movie from the database.

            This method prompts the user to enter the name of the movie they wish to delete from the database.
            The specified movie is then removed from the database using the storage implementation.

            Args:
                None

            Returns:
                None
            """

        movie = input("Type the movie name to delete from the database: ")
        self._storage.delete_movie(movie)

    def _update_movie(self):
        """
            Update the rating of a movie in the database.

            This method prompts the user to input the name of the movie they want to update,
            displays the current information of the movie, and allows the user to provide a new rating.
            The updated rating is then saved in the database using the storage implementation.

            Args:
                None

            Returns:
                None
            """

        movie_title = input("Name of the movie to update: ")
        self._storage.show_single_movie_info(movie_title)
        movie_rating = float(input("Provide a new rating for the given movie: "))
        self._storage.update_movie(movie_title, movie_rating)


    def _random_movie(self):
        """
            It shows the random movies from the movie db.
            """

        movies_data = self._storage.load_movies_data()

        if not movies_data:
            print("No movies in the database.")
            return

        rand_movie = random.choice(list(movies_data.keys()))
        rand_rating = movies_data[rand_movie]['rating']
        rand_year = movies_data[rand_movie]['year']
        rand_poster = movies_data[rand_movie]['poster']  # Assuming the 'poster' key exists in your movie data

        print(f'Random Movie: {rand_movie}\tRating: {rand_rating}\tYear: {rand_year}\tPoster: {rand_poster}')

    def _search_movie(self):
        """
            Search for a movie in the database by its name.

            This method prompts the user to enter a movie name to search for in the movie database. It then performs
            a case-insensitive search and displays the details (rating, year, and poster) of all movies whose names contain
            the searched keyword.

            If no movies are found with a matching keyword, it prints a message indicating that no matching movies were found.

            Returns:
                None
            """
        movie_name = input("Enter the movie name to search from the movie database: ")
        name_lower = movie_name.lower()
        found = False
        for movie_name, info in self._storage.load_movies_data().items():
            if name_lower in movie_name.lower():
                print(f"The name of the movie \"{movie_name}\" is: {info['rating']} "
                      f"(Rating), {info['year']} (Year), {info['poster']} (poster)")

                found = True
        if not found:
            print(f"No movie has found for the name: {movie_name}")


    def _sorted_by_rating(self):
        """
           Display movies sorted by their ratings.
           """
        movies_info = self._storage.load_movies_data()
        if not movies_info:
            print("No movies in the database.")
            return

        movies_sorted_by_rating = sorted(movies_info.items(),
                                         key=lambda item: item[1]['rating'], reverse=True)
        if movies_sorted_by_rating:
            print("Movies sorted by rating:")
            for movie_name, movie_info in movies_sorted_by_rating:
                poster = movie_info.get('poster', 'Poster not available')
                print(f"The name of the movie \"{movie_name}\" is: {movie_info['rating']}"
                      f"(Rating), {movie_info['year']} (Year),{poster}(Poster)")

    def _create_rating_histogram(self):
        """
            Creates and saves a rating histogram for the movies in the database.

            This method retrieves the ratings of all movies from the storage and generates a histogram to visualize
            the distribution of movie ratings. The histogram is then saved to a file provided by the user.

            Returns:
                None
            """

        movie_info = self._storage.load_movies_data()

        if not movie_info:
            print("No movies available in the movie database.")
            return

        ratings = [info['rating'] for info in movie_info.values()]

        if ratings:
            plt.hist(ratings, bins=10, edgecolor='black')
            plt.xlabel('Rating')
            plt.ylabel('Frequency')
            plt.title('Rating Histogram')
            file_name = input("Enter the file name to save the histogram (e.g., histogram.png): ")
            plt.savefig(file_name)
            plt.close()
            print(f"Histogram saved to {file_name}")
        else:
            print("No movies available in the movie database.")

    def _command_movie_stats(self):
        """
            Displays statistics about the movies in the database.

            This method retrieves movie data from the storage and calculates various statistics, including the average rating,
            median rating, and the best and worst-rated movies. It then prints these statistics to the console.

            Returns:
                None
            """

        movies_data = self._storage.load_movies_data()
        ratings = [movie_info["rating"] for movie_info in movies_data.values()]

        if ratings:
            average = sum(ratings) / len(ratings)
            median_raiting = median(ratings)
            best_movie = max(movies_data, key=lambda title: movies_data[title]["rating"])
            worst_movie = min(movies_data, key=lambda title: movies_data[title]["rating"])

            print(f"Average rating: {average:.2f}")
            print(f"Median rating: {median_raiting:.2f}")
            print(f"Best movie: {best_movie} ({movies_data[best_movie]['rating']:.2f})")
            print(f"Worst movie: {worst_movie} ({movies_data[worst_movie]['rating']:.2f})")
        else:
            print("No movies available in the movie database.")





# Your IStorage class and its derived classes (e.g., StorageJson, StorageCsv) would remain the same.
