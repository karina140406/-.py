student = {"name": "Igor", "notes": [4, 5, 4]}
result = {
    "name": student.get("name", ""),
    "max_note": max(student.get("notes", [])) if student.get("notes") else 0
}
print(result)