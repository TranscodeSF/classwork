fruits = ["apple", "banana", "orange", "cherry", "tomato"]

quantities = {}
for fruit in fruits:
    if fruit[-1] == 'y':
        inflected_fruit = fruit[0:-1]+"ies"
    elif fruit[-1] == 's' or fruit[-1] == 'o':
        inflected_fruit = fruit + "es"
    else:
        inflected_fruit = fruit + "s"
    qty = int(raw_input("How many %s? " % inflected_fruit))
    quantities[fruit] = qty

for fruit in fruits:
    qty = quantities[fruit]
    if qty == 1:
        inflected_fruit = fruit
    else:
        if fruit[-1] == 'y':
            inflected_fruit = fruit[0:-1]+"ies"
        elif fruit[-1] == 's' or fruit[-1] == 'o':
            inflected_fruit = fruit + "es"
        else:
            inflected_fruit = fruit + "s"
    print "You should buy %d %s" % (quantities[fruit], inflected_fruit)
