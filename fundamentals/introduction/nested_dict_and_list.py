#Update Values in Dictionaries and Lists
print("Update Values in Dictionaries and Lists")#----------------------------------------------------------------------

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

#Iterate Through a List of Dictionaries
print("Iterate Through a List of Dictionaries")#----------------------------------------------------------------------