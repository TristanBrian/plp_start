capital_city ={"Nepal":"Kathmandu","India":"New Delhi","China":"Beijing"}
print("initial dictionary: ",capital_city)
 
 ## adding to dictionary
capital_city["japan"]= "tokyo"
print("updated dictionary:",capital_city)

##delete dictionary
del capital_city["China"]
print("updated dictionary:",capital_city)

## prints the total number of items
print(len(capital_city))

# my_dict = set(): This creates an empty set, not a dictionary.
# my_dict = (): This creates an empty tuple, not a dictionary.
# my_dict = []: This creates an empty list, not a dictionary.
# my_dict = {} : creates empty dictionary.