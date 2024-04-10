"""
[dictionary comprehension] Given a dictionary with students' names as keys and their respective scores as values, create a new dictionary that contains only the students who scored more than 80 using dictionary comprehension.
"""

def topStudents(students_dict):
    return {name:score for name, score in students_dict.items() if score>80}

print(topStudents({"RAM":76, "Shyam":82, "Hari":83,"Gita":80}))
