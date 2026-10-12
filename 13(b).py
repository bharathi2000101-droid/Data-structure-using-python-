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

Output 
--- School Portal: Student Marks Management ---
Enter the number of students: 5
Enter the marks for 5 students:
Student 1 marks: 78
Student 2 marks: 45
Student 3 marks: 92
Student 4 marks: 56
Student 5 marks: 88

Marks before sorting : [78.0, 45.0, 92.0, 56.0, 88.0]
Marks in Ascending Order: [45.0, 56.0, 78.0, 88.0, 92.0]
