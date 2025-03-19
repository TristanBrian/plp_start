list_a = [1,2,3,4,5]
print (list_a)

##changes a value in the list
list_a [0] = 16
print (list_a)
print (len (list_a))

list_a.insert(len(list_a),6)
print (list_a)

list_a.append (7)
print (list_a)

list_a.extend([8,9,10])
print (list_a)

list_a.pop(8)
print (list_a)

del list_a[7]
print (list_a)
