# by Kami Bigdely
# Extract class
first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],
          ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]


class Actor:
    def __init__(self, first_name, last_name, birth_year, email, movies):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.email = email
        self.movies = movies

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def print_movie_list(self):
        print('Movies Played: ', end='')
        for movie in self.movies:
            print(movie, end=', ')
        print()

    def send_email(self):
        print("email sent to: ", self.email)


actors = [Actor('elizabeth', 'debicki', 1990, 'deb@makeschool.com', ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby']),
          Actor('Jim', 'Carrey', 1962, 'jim@makeschool.com', ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man'])]


for actor in actors:
    if actor.birth_year > 1985:
        print(actor.get_full_name())
        actor.print_movie_list()
        actor.send_email()
        # for i, value in enumerate(emails):
#     if birth_year[i] > 1985:
#         print(first_names[i], last_names[i])
#         print('Movies Played: ', end='')
#         for m in movies[i]:
#             print(m, end=', ')
#         print()

#         send_hiring_email(value)
