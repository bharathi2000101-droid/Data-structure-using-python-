# Function to implement Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index if found
    return -1

# Function to implement Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Main program implementation
if __name__ == "__main__":
    print("--- School Portal: Exam Registration Verification ---")
    
    # 1. Take list of registered roll numbers from the user
    n = int(input("Enter the total number of registered students: "))
    registered_students = []
    
    print(f"Enter the roll numbers of the {n} registered students:")
    for i in range(n):
        roll = int(input(f"Student {i + 1} roll number: "))
        registered_students.append(roll)
        
    print("\nRegistered Student Roll Numbers:", registered_students)
    
    # Take roll number input from the user to search[span_1](start_span)[span_1](end_span)
    target_roll = int(input("\nEnter the roll number to search/verify: "))
    
    # 2. Use Linear Search to check if the roll number exists[span_2](start_span)[span_2](end_span)
    linear_result = linear_search(registered_students, target_roll)
    
    # 3. Use Binary Search (on a sorted version of the list) to check if the roll number exists[span_3](start_span)[span_3](end_span)
    sorted_students = sorted(registered_students)
    binary_result = binary_search(sorted_students, target_roll)
    
    # 4. Print the result for both searches, indicating whether found or not[span_4](start_span)[span_4](end_span)
    print("\n--- Search Results ---")
    if linear_result != -1:
        print(f"Linear Search: Roll number {target_roll} found at index {linear_result}.")
    else:
        print(f"Linear Search: Roll number {target_roll} not found.")
        
    if binary_result != -1:
        print(f"Binary Search: Roll number {target_roll} found at index {binary_result} (in sorted order).")
    else:
        print(f"Binary Search: Roll number {target_roll} not found.")
