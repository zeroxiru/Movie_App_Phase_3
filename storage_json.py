from istorage import IStorage
import json
import statistics


class StorageJson(IStorage):
    def __init__(self, file_path, family_member_name=None):
        self._file_path = file_path
        self._movies_data = self.load_movies_data()
        self._family_member_name = family_member_name

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value

    @property
    def family_member_name(self):
        return self._family_member_name

    @family_member_name.setter
    def family_member_name(self, value):
        self._family_member_name = value

    def load_movies_data(self):
        """
        Loads the JSON data from a file.
        """
        with open(self._file_path, "r") as file_obj:
            return json.load(file_obj)

    def save_data(self, data):
        """
        Saves the data to a JSON file.
        """
        movie_info_to_save = {movie: info for movie, info in data.items()}
        with open(self._file_path, "w") as file_obj:
            json.dump(movie_info_to_save, file_obj, indent=4)

    def list_movies(self):
        """
           Lists the movies in the database along with their ratings, release years, and posters (if available).

           This function retrieves the movie data from the database and prints the information for each movie.
           If there are no movies in the database, it displays a message indicating the absence of movies.

           Returns:
           None
           """

        if self._movies_data:
            print("List of Movies")
            for movie, info in self._movies_data.items():
                print(f'Movie Title: {movie}')
                print(f"Movie Rating: {info.get('rating', 'N/A')}")
                print(f"Movie Year: {info.get('year', 'N/A')}")
                print(f"Movie Poster: {info.get('poster', 'N/A')}")
        else:
            print("No available movies in the database.")

    def add_movie(self, title, year, rating, poster):
        """
        Adds a new movie to the database.
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
                f"A movie with title: {title}, rating: {rating}, and year: " \
                f"{year} already exists in the movies database.")

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
        """
        It shows single movie information from the movie database.
        """

        if title in self._movies_data:
            movie_info = self._movies_data[title]
            print(f"{title}:")
            print(f"  Rating: {movie_info['rating']}")
            print(f"  Year: {movie_info['year']}")
        else:
            print(f"{title} was not found in the movie database.")

    def update_movie(self, title, rating):
        """
        Updates a movie's rating in the movies database.
        """
        if title in self._movies_data:
            self._movies_data[title]['rating'] = rating
            self.save_data(self._movies_data)
            print(f"{title} movie rating have updated in the movie database.")

        else:
            print(f"{title} was not found in the movie database.")



