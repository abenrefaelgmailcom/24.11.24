
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}


#a
''' הוסף את השחקנית Watson Emma לרשימת זוכי האוסקר'''

oscar_winners.add('Emma watson')
print(oscar_winners)


#b
new_winners = oscar_winners.copy()
new_winners.remove("Meryl Streep")
new_winners.clear()
print(new_winners)


#c
common_actors = titanic_actors & dark_knight_actors  # שימוש ב-& לחיתוך
print("actors in both titanic and the dark knight", common_actors)



# #d
# avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
# iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
# print(avengers_actors.issuperset(iron_man_actors))
#

common_in_iron_and_avengers = iron_man_actors & avengers_actors
print("common actors in-Iron Man and-Avengers:", common_in_iron_and_avengers)




#e
is_all_oscar_winners = actor_list.issubset(oscar_winners)
print("does all the actors in actor+list won the oscar?", is_all_oscar_winners)


# #f
includes_all_avengers = actor_list.issuperset(avengers_actors)  # שימוש ב-issuperset
print("does actor_list contain all Avengers actors?", includes_all_avengers)

# #g
removed = movie_cast.pop()
print(removed)
print(movie_cast)


#h
movie_cast.discard("Matt Damon")
print(movie_cast)


#i
non_oscar_titanic = titanic_actors - oscar_winners
print("titanic actors who didnt won the oscar:", non_oscar_titanic)

non_oscar_titanic = titanic_actors - oscar_winners
print(" titani actor who didnt won an oscar:", non_oscar_titanic)



# #j
exclusive_actors = titanic_actors ^ dark_knight_actors
print("actors that appeared only in titanic or the dark knight:", exclusive_actors)

#k
oscar_winners.update('Blanchett Cate', 'Lewis-Day Daniel')
print(oscar_winners)

#l

all_titanic_dark_knight = titanic_actors | dark_knight_actors  # שימוש ב-| לאיחוד
print("actors from both titanic and the dark knight:", all_titanic_dark_knight)