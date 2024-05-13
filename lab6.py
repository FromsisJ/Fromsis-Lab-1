def delete_element(array, index):
    # Check if index is valid
    if index < 0 or index >= len(array):
        print("Invalid index.")
        return array  # Return the original array unchanged

    # Create a new list with elements except the one at the specified index
    new_array = array[:index] + array[index+1:]

    return new_array

# Test the function
array = [3, 7, 1, 9, 4]
index_to_delete = 2

# Call the delete_element function
modified_array = delete_element(array, index_to_delete)

# Print the modified array
print("Modified Array:", modified_array)
