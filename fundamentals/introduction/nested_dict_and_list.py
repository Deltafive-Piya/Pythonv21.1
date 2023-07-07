#Update Values in Dictionaries and Lists
print("Update Values in Dictionaries and Lists----------------------------------------------------------------------")

x = [ [5,2,3], [10,8,9]
]
print(x)        #Control
x[1][0] = 15    #Changing the first element of the second element of the list x
print(x)        #proving it worked


students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(students[0])                      #Control
students[0]['last_name'] = 'Bryant'     #Changing the last name section of the first entry in students list
print(students[0])                      #proving it worked


sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print(sports_directory['soccer'])       #Control
sports_directory['soccer'][0] = 'Andres'#Changing the 0th index of soccer entry in sports_directory
print(sports_directory['soccer'])       #Proving it worked


z = [ {'x': 10, 'y': 20}
]
print(z[0]['y'])                #Control
z[0]['y'] = 30                  #Changing the y section in the first entry of z
print(z[0]['y'])                #Proving it worked
print('\n')

#Iterate Through a List of Dictionaries
print("Iterate Through a List of Dictionaries----------------------------------------------------------------------")
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#Multi Line responses
print("iterateDictMulti")
def iterateDictionaryMulti(students):
    for student in students:
            for key, value in student.items():
                print(f'{key} - {value}')
iterateDictionaryMulti(students)
print('\n')


#Single Line responses WITH COMMAS
print("iterateDictSingle")
def iterateDictionarySingle(students):
    for student in students:
        for key, value in student.items():
            print(f'{key} - {value}', end=', ')
        print()  # Print a newline after each student's names
iterateDictionarySingle(students)
print('\n')

# Get Values From a List of Dictionaries
print("Get Values From a List of Dictionaries----------------------------------------------------------------------")
def iterateDictionary2(key_name, students):
    for item in students:
        if key_name in item:
            print(item[key_name])

print("Selected first names:")
iterateDictionary2('first_name', students)
print('\n')
print("Selected last names:")
iterateDictionary2('last_name', students)
print('\n')

# Iterate Through a Dictionary with List Values
print("Iterate Through a Dictionary with List Values----------------------------------------------------------------------")

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key, value in dojo.items():
        print(f'{len(value)} {key}')
        for item in value:
            print(item)
        print()
printInfo(dojo)