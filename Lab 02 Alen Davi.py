def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name' : 'Alen Mulangan Davi',
        'student_id': '10332934',
        'pizza_toppings' : ['PEPPRONI',
                            'MUSHROOM', 
                            'ONIONS'
                            ],
        'movies' : [
                    { 'Title' : 'Titanic',
                      'Genre' : 'Romantic'
                    },
                    {'Title' : 'Avatar',
                     'Genre' : 'Action'
                    }
                    ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {
        'Title' : 'Jurassic Park',
        'Genre':'Adventure'
    }
    about_me['movies'].append(new_movie)

    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ("bacon", "hot peppers"))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me["movies"])


# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    first_name = about_me['full_name'].split()[0]
    print(f"My name is {about_me['full_name']}, but you can call me Sir {first_name}.")
    print(f"My student ID is {about_me['student_id']}.")
    
 
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    about_me['pizza_toppings'].sort()
    about_me['pizza_toppings']= [topping.lower() for topping in about_me['pizza_toppings']]

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("My favourite pizza toppings are:")
    for topping in about_me["pizza_toppings"]:
     print(f"- {topping}")

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genre = [movies['Genre'] for movies in about_me['movies']]
    movies_genre= f"{', '.join(genre[:-1])}, and {genre[-1]} movies"
    print(f'I like to watch {movies_genre}')

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    movie_list= [movies['Title'].title() for movies in movie_list]
    movies_title= f"{', '.join(movie_list[:-1])}, and {movie_list[-1]}"
    print(f'Some of my favourite movies are {movies_title}!')

    
if __name__ == '__main__':
    main()
