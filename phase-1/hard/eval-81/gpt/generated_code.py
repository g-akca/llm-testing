from typing import List

def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:

             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E

    Example:
        numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])
        ➞ ['A+', 'B', 'C-', 'C', 'A-']
    """
    letter_grades = []
    for gpa in grades:
        if gpa == 4.0:
            letter = "A+"
        elif gpa > 3.7:
            letter = "A"
        elif gpa > 3.3:
            letter = "A-"
        elif gpa > 3.0:
            letter = "B+"
        elif gpa > 2.7:
            letter = "B"
        elif gpa > 2.3:
            letter = "B-"
        elif gpa > 2.0:
            letter = "C+"
        elif gpa > 1.7:
            letter = "C"
        elif gpa > 1.3:
            letter = "C-"
        elif gpa > 1.0:
            letter = "D+"
        elif gpa > 0.7:
            letter = "D"
        elif gpa > 0.0:
            letter = "D-"
        else:            # gpa == 0.0 or invalid/negative values
            letter = "E"
        letter_grades.append(letter)
    return letter_grades

# Example usage
if __name__ == "__main__":
    sample_gpas = [4.0, 3, 1.7, 2, 3.5]
    print(numerical_letter_grade(sample_gpas))
    # Output: ['A+', 'B', 'C-', 'C', 'A-']
