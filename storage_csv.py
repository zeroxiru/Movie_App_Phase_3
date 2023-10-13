import csv
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, file_path):
        self._file_path = file_path
        self._movies_data = self.load_movies_data()

    def load_movies_data(self):
        """
        Loads the CSV data from a file.

        Returns:
            dict: The loaded CSV data as a dictionary of dictionaries.
        """
        movies_data = {}
        with open(self._file_path, mode='r', newline='') as file_obj:
            reader = csv.DictReader(file_obj)
            for row in reader:
                movie_title = row['title']
                movie_info = {
                    'rating': float(row['rating']),
                    'year': int(row['year']),
                    'poster': row['poster']

                }
                movies_data[movie_title] = movie_info
        return movies_data

    def save_data(self, data):
        """
        Saves the data to a CSV file.

        Args:
            data (dict): The data to be saved.
        """
        with open(self._file_path, mode='w', newline='') as file_obj:
            fieldnames = ['title', 'rating', 'year', 'poster']
            writer = csv.DictWriter(file_obj, fieldnames=fieldnames)
            writer.writeheader()
            for movie, info in data.items():
                writer.writerow({'title': movie, 'rating': info['rating'], 'year': info['year'], 'poster': info['poster']})

    def list_movies(self):
        """
          Lists the movies in the database along with their ratings and release years.

          This function retrieves the movie data from the database and prints the information for each movie.
          If there are no movies in the database, it displays a message indicating the absence of movies.

          Returns:
          None
          """
        if self._movies_data:
            print("List of Movies")
            for movie, info in self._movies_data.items():
                print(f'Movie Title: {movie}')
                print(f"Movie Rating: {info['rating']}")
                print(f"Movie Year: {info['year']}")
                print(f"Movie Poster: {info['poster']}")
        else:
            print("No available movies in the database.")

    def add_movie(self, title, year, rating, poster):
        """
            Adds a new movie to the database.

            This function allows users to add a new movie to the database by providing the movie's title,
            release year, and rating. It checks if the movie already exists and adds it if it's not in the database.
            The movie information is then saved to the database.

            Args:
                title (str): The title of the movie.
                year (int): The release year of the movie.
                rating (float): The rating of the movie.

            Returns:
            None
            """
        if title not in self._movies_data:
            self._movies_data[title] = {
                'year': year,
                'rating': rating,
                'poster': poster
            }
            self.save_data(self._movies_data)
            print(f"{title} movie has added into the database")
        else:
            print(
                f"A movie with title: {title}, rating: {rating},  year: " \
                f"{year} and poster: {poster} already exists in the movies database.")


    def delete_movie(self, title):
        """
            Deletes a movie from the movies database.
            Loads the information from the JSON file, deletes the movie,
            and saves it. The function doesn't need to validate the input.
            """
        movie = title
        if movie in self._movies_data:
            print(f"{movie} = {self._movies_data[movie]}")
            confirm = input(f"Do you want to delete {movie} from the movie database? (Y/N): ")
            if "Y" in confirm.upper():
                del self._movies_data[movie]
                self.save_data(self._movies_data)
                print(f"{movie} is deleted from the movie db.")
            else:
                print(f"{movie} was not deleted.")
        else:
            print(f'{movie} was not found in the movie database')

    def show_single_movie_info(self, title):

        if title in self._movies_data:
            movie_info = self._movies_data[title]
            print(f"{title}:")
            print(f"  Rating: {movie_info['rating']}")
            print(f"  Year: {movie_info['year']}")
            print(f"  Poster: {movie_info['poster']}")
        else:
            print(f"{title} was not found in the movie database.")

    def update_movie(self, title, rating):
        """
            Updates a movie from the movies database.
            Loads the information from the JSON file, updates the movie,
            and saves it. The function doesn't need to validate the input.
            """

        if title in self._movies_data:
            self._movies_data[title]["rating"] = rating
            self.save_data(self._movies_data)
            print(f"{title} updated with rating {rating}.")
        else:
            print(f"{title} was not found in the movie database.")


   # def list_movies(self):
