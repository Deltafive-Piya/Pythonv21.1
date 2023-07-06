# 0-150 printer
print("0-150 by 1's")
aba = [i for i in range(0, 151)]
print(aba)
print("\n")




# 5-1000 by 5's printer
print("0-1001 by 5's")
abb = [i for i in range (5,1001,5)]
print(abb)
print("\n")




#  1-100 printer; modulo 5 = coding, modulo 10 = coding dojo
print("0-100; modulo 5's and 10's")
for i in range(1,101):
    if i % 10 == 0:
        print("Coding")
    elif i % 5 == 0:
        print("Coding Dojo")
    else:
        print(i)
print("\n")




# 0-500001 summation
print("0...500001 summation")
odds_sum = 0 
for i in range(1, 500001, 2):
    odds_sum += i

print(odds_sum)
print("\n")




#2018 quadannual incrimentation
print("2018 quadannual decriment")
for year in range( 2018, 0, -4):
    print(year)
print("\n")




#modulo mult=low-high printer
print("picky picker")
biggest_bag = 9
smallest_bag = 2
pattern_preference = 3

for bag in range(smallest_bag, biggest_bag + 1): # =1 to include the highest bag
    if bag % pattern_preference == 0:
        print(bag)