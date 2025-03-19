## collection of unique data

student_id = {112, 114, 117, 113}
print ("Student ID: ", student_id)

##initialize an empty set
emptyset = set ()
print ("empty set:", emptyset)

##adding to a set
student_id.add(120)
print ("Student ID:" , student_id)

## removing from set
student_id.discard (117)
print ("Student ID:" , student_id)

##

##intersection of sets
A = {1,3,5}
B = {1,2,3}
print ("Intersection of A and B:", A & B)

##unions of sets
A = {1,3,5}
B = {0,2,4}
print ("Union of A and B:", A | B)


##difference of sets
A = {1,3,5}
B = {0,2,4}
print ("Difference of A and B:", A - B)

##symetric difference
A = {1,3,5}
B = {0,2,4}
print ("Symetric difference of A and B:", A ^ B)



