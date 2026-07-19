# This function reverses an array using recursion and a two-pointer approach.
# It modifies the array in-place, meaning it does not create a new array.
def reverse_arr(arr, first, last):
  # Base Case: This is the most important condition in a recursive function.
  # It tells the function when to stop. Here, we stop when the 'first' index
  # is greater than or equal to the 'last' index. This means we have either
  # processed the whole array or we are at the middle element.
  if first >= last:
    return

  # The main logic: Swap the elements at the 'first' and 'last' positions.
  # This is how the reversal happens, from the outside in.
  arr[first], arr[last] = arr[last], arr[first]

  # Recursive Step: Call the function again, but move the pointers closer together.
  # We increment 'first' and decrement 'last' to work on the next pair of elements.
  # ***CORRECTION***: You were missing `arr` in your recursive call.
  reverse_arr(arr, first + 1, last - 1)

# This block of code runs only when you execute this script directly.
if __name__ == "__main__":
  arr = [10, 20, 30, 40]
  
  # ***CORRECTION***: The function modifies the array in-place and returns nothing (None).
  # So, we first call the function to reverse the array.
  reverse_arr(arr, 0, len(arr)-1)
  
  # Then, we print the modified array to see the result.
  print(arr)