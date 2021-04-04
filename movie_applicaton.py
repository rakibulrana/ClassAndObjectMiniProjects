class Movie:
    """This is a bacis movie info application """

    def __init__(self, title, hero, heroine):
        self.title = title
        self.heor = hero
        self.heroine = heroine

    def info(self):
        print("Movie Name: ", self.title)
        print("Name of the Hero: ", self.heor)
        print("Name of the Heroine: ", self.heroine)


list_of_movies = []

while True:

    title = input("Enter your movie title: ")
    hero = input("Enter name of the hero: ")
    heroine = input("Enter name of the heroine: ")

    movie_object = Movie(title, hero, heroine)
    list_of_movies.append(movie_object)
    print("Movies added to the list successfully")

    option = input("Do you want to add one more movie [Yes|No]:")

    if option.lower() == 'no':
        break

print("All Movies Information...")
print("#" * 40)

for movie in list_of_movies:
    movie.info()
    print()  # add a down space
