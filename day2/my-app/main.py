from fastapi import FastAPI
from course import Course
app = FastAPI()

courses: Course = [{
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
    return courses

#fetch a single course

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    course = next((course for course in courses if course.id == course_id), None)
    if course is None:
        return {"error": f"Course with id {course_id} not found"}

@app.post("/courses")
def create_course(course: Course):
    courses.append(course)
    return course

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    global courses
    print( course_id)
    #filter courses to remove the course with the given id
    filtered_list = list(filter(lambda course: course['id']!= course_id, courses))
    courses = filtered_list
    return courses


@app.patch("/courses/{course_id}")

def update_course(course_id: int, updated_course: Course):
    global courses
    course = next((course for course in courses if course['id'] == course_id), None)
    if course is None:
        return {"error": f"Course with id {course_id} not found"}
    course.update(updated_course.dict(exclude_unset=True))
    return course