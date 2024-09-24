from typing import Any, Dict, List
from fastapi import FastAPI, status, HTTPException
from course import Course
app = FastAPI()
courses: List[Dict[str, Any]] = [{
    "id": 1,
    "title": "Python Programming",
    "instructor": "Dr. Samuel Johnson",
    "students": 300
}]

@app.get("/hello")
def hello_world():
    return {"message": f"Hello, World!"}



@app.get("/courses")
def get_courses():
    global courses
    return courses


@app.get("/courses/studentsrange")
def get_courses_by_students_range(min_students: int, max_students: int):
    # print(min_students)
    # print(max_students)
    filtered_coures = [course for course in courses if min_students <= course["students"] <= max_students]
    if not filtered_coures:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No courses found with students between {min_students} and {max_students}")
    return filtered_coures

@app.get("/courses/sortedby")
def get_courses_sorted_by_students(field: str):
    print(field)
    sorted_list = sorted(courses, key=lambda x: x[field])
    print(sorted_list)
    # courses.sort(key=lambda x: x["students"])
    return sorted_list

#fetch a single course
@app.get("/courses/{course_id}")
def get_course(course_id: int):
    global courses
    for course in courses:
        if course["id"] == course_id:
            return course
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with id {course_id} not found")

@app.post("/courses", status_code=status.HTTP_201_CREATED)
def create_course(course: Course):
    global courses
    courses.append(course.dict())
    return course

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
   for course in courses:
        if course["id"] == course_id:
            courses.remove(course)
            return {"message": f"Course with id {course_id} deleted"}


@app.patch("/courses/{course_id}")

def update_course(course_id: int, updated_course: Course):
    global courses
    course = next((course for course in courses if course['id'] == course_id), None)
    if course is None:
        return {"error": f"Course with id {course_id} not found"}
    course.update(updated_course.dict(exclude_unset=True))
    return course

@app.get("/courses/bytitle")
def get_courses_by_title(title: str):
    filtered_coures = [course for course in courses if course["title"].lower().startswith(title.lower())]
    if filtered_coures:
        return filtered_coures
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No courses found with title starting with {title}")

