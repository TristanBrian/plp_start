def main():
    # 1.create an empty list called my_list
    my_list = []

    # 2.Append Elements to a list
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    print("After appending elements: ", my_list)

    # 3. insert Value 15 at the second position in list
    my_list.insert(1, 15)
    print("After inserting 15 at second position :", my_list)

    # 4. extend list
    my_list.extend ([50,60,70])
    print("After extending elements: ", my_list)

    # 5. Remove elements
    my_list.pop()
    print("After removing elements:", my_list)

    # 6.A sort list in ascending order
    my_list.sort()
    print("After sorting elements in ascending order:", my_list)

    # 6.B sort list in descending order
    my_list.sort(reverse=True)
    print("After sorting in descending order:", my_list)

    # 7. find index
    index_of_30 = my_list.index(30)
    print("Index of 30 is:" , index_of_30)

if __name__ == "__main__":
    main()