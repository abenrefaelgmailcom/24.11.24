#hw17

# #a
# '''tuple that contain number 99'''
#
# tuple = (99,)
# print('tuple with the number  99', tuple)
#
# #b
# '''tuple that contain number 99,88,87'''
# tuple = (77, 88, 99)
# print('tuple with the number  99, 88, 77', tuple)
#
#
# #c
# '''function that recive a tuple and return its length '''
# def tup_length(tuple):
#     return len(tuple)
#

#d
'''function thats recive 2 tuples and retun them combined'''
def comb_tup(tup1, tup2) -> int:
    result = tup1 + tup2
    tup1 = tup1 + tup2
    return result
#e
'''function thats recive 2 tuples and return a tuple thats have the common items'''

def common_tup(tup1, tup2) -> tuple:
    return tuple(set(tup1) & set(tup2))

print("common elements", common_tup((3, 4, 5, 6), (1, 2, 3, 4)))


#f
'''function thats recive 2 tuples and return a tuple thats have the different items'''

def items(tup1, tup2):
    return tuple(set(tup1) ^ set(tup2))

print("איברים שונים:", items((3, 4, 5, 6), (1, 2, 3, 4)))



#g
'''function thats get tuple and index and return the irem in the same index'''

def get_element_by_index(tup, index):
    if 0 <= index < len(tup):
        return tup[index]
    return None

print("element in index 2:", get_element_by_index((1, 2, 3, 4), 2))
print("index out of range", get_element_by_index((1, 2, 3, 4), 5))


#h
'''function thats recive tuple and return it in reverse'''
def reverse_tuple(tup):
    return tup[::-1]

print("Tuple in reverse  :", reverse_tuple((1, 2, 3, 4)))


#i
'''function thats recive tuple and a number and return the tuple multiple by the size it sent'''

def repeat_tuple(tup, n):
    return tup * n

print("Tuple משוכפל:", repeat_tuple((1, 2), 3))


#j
'''function thats recive tuple and a number and return the tuple
without the number'''

def remove_element(tup, value):
    return tuple(x for x in tup if x != value)

print("Tuple without number 10:", remove_element((10, 5, 2, 10, 8), 10))

#k
'''function thats recive tuple and return it without any duplicated items'''
def remove_duplicates(tup):
    unique_list = []
    for x in tup:
        if x not in unique_list:
            unique_list.append(x)
    return tuple(unique_list)

print("Tuple ללא כפילויות:", remove_duplicates((1, 2, 2, 3, 3, 3)))




# l **************************bonus
'''function thats recive tuple and a number and return  the index of the numbers in tuple'''


def get_indices(tup, value):
    return tuple(i for i, x in enumerate(tup) if x == value)

print("אינדקסים של 5:", get_indices((10, 5, 3, 5, 2, 5), 5))



#m
'''input from the user a list of names until done is typed'''

names = []
while True:
    name = input("הכנס שם (או 'done' לסיום): ")
    if name == "done":
        break
    names.append(name)

grades = []
while True:
    grade = int(input("input grade (or 99 to finish): "))
    if grade == -999:
        break
    grades.append(grade)

students = tuple(zip(names, grades))
print("תוצאות:", students)


#2
'''difference between tuple and a list'''

'''Tuple הוא מבנה נתונים שאינו ניתן לשינוי (Immutable). מתאים לנתונים קבועים כמו קואורדינטות.
List ניתן לשינוי (Mutable). מתאים לנתונים דינמיים שצריך לעדכן.'''

#3
'''explenation why tuple is unchangeable'''
data_tuple = (
    {"name": "Alice", "age": 30, "city": "New York"}, 1000, "secret-code"
)
data_tuple[0]["age"] = 31
data_tuple[0].clear()
'''ההסבר: ה-Tuple עצמו אינו ניתן לשינוי, אך אובייקטים בתוך ה-Tuple (כמו מילון) ניתנים לשינוי כי הם Mutable.'''