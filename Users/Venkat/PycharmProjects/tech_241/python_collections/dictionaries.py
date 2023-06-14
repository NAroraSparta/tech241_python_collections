# Dictionaries

# Key - Value pairs

# Key is the name/reference, value is the data stored.

# Makinga a dictionary

student_1 = {
    "name": "Neha",
    "stream": "devops",
    "completed_lessons": 4,
    "completed_lessons_names": ["variables", "git", "data_types", "collections"]
}

print(type(student_1))

#How to access parts of a dictionary
print((student_1["stream"]))

print((student_1["completed_lessons_names"][:2]))

#Changing a value

student_1["completed_lessons_names"] = "data_analytics"
print(student_1["stream"])

# Dictionary methods

print(student_1.keys())
print(student_1.values())