def max_product(arr):
    # Solution 1: sort and reverse the array, return the product of first and second element
    # arr.sort(reverse=True)
    # return arr[0] * arr[1]

    # Solution 2: Using for loop
    max_element1, max_element2 = 0, 0

    for number in arr:
        if number > max_element1:
            max_element2 = max_element1
            max_element1 = number
        elif number > max_element2:
            max_element2 = number

    return max_element1 * max_element2


my_array = [1, 7, 3, 4, 9, 5]
print(max_product(my_array))