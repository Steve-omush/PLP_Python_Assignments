# Function to perform list operations

def list_operations():
    # Step 1: Create an empty list
    my_list = []

    # Step 2: Add elements to the list
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    print(f"List after appending elements(Initial list): {my_list}")

    # Step 3: Insert an element at a specific index
    my_list.insert(1, 15)
    print(f"List after inserting(15) element at index 1(position 2): {my_list}")

    # Step 4: Extend the list with another list
    another_list = [50, 60, 70]
    my_list.extend(another_list)
    print(f"List after extending with another list ({another_list}): {my_list}")

    # Step 5: Remove an element from the list (Last element)
    removed_element = my_list.pop()
    print(f"Removed last element: {removed_element}: New list: {my_list}")

    # Step 6: Sort the list in ascending order
    my_list.sort()
    print(f"List after sorting(ascending order): {my_list}")

    # Step 7: Find the index of an element in the list
    index_of_30 = my_list.index(30)
    print(f"Index of 30: {index_of_30}")

#Program starts here
list_operations()