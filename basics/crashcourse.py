#!/usr/bin/python3

string_var = "Hallo Robert"
integer_var = 42
float_var = 12.5
list_var = [string_var, integer_var, float_var]

# Ausgabe: print
print(list_var)
print(list_var[1])

# Bedingungen: if/elif/else
if integer_var > 42: # == != < <= > >=
    print("Um Gottes Willen, wir wollen aber nur 42!")
elif integer_var < 42:
    print("das ist zu wenig :(")
#elif ...
else:
    print("so muss das sein!")

# Funktionen
def add(var, step = 1):
    print('...') #
    return var + step

# Schleifen: for/while
count = 1
max = 10

while count <= max:
    print(count)
    count = add(count, 1)

for value in list_var:
    print(value)