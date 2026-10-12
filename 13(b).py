# Python Program to Implement Bubble Sort with User Input for Student Marks

def bubble_sort(marks):
    n = len(marks)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
                swapped = True
        # If no two elements were swapped by the inner loop, the list is already sorted
        if not swapped:
            break
    return marks

# Main code with user input
if __name__ == "__main__":
    print("--- School Portal: Student Marks Management ---")
    
    # Taking number of students from user
    n = int(input("Enter the number of students: "))
    
    student_marks = []
    print(f"Enter the marks for {n} students:")
    for i in range(n):
        mark = float(input(f"Student {i + 1} marks: "))
        student_marks.append(mark)
    
    print("\nMarks before sorting :", student_marks)
    
    # Sort the marks using Bubble Sort algorithm
    sorted_marks = bubble_sort(student_marks)
    
    print("Marks in Ascending Order:", sorted_marks)
