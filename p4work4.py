anton_courses = {"Mathematica'": 56, "Python": 87, "BD": 140}
HardML = {"HardML": 120}
anton_courses.update(HardML)
courses = anton_courses.keys()
print(courses)
Python = anton_courses.get("Python")
print(Python)