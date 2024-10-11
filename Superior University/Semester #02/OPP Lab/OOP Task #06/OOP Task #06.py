# MULTIPLE INHERITENCE

class Course:
    def __init__(self,course_name,course_code):
        self.course_name = course_name
        self.course_code = course_code

    def display_info(self):
      return f"Course_name: {self.course_name}\n Course_code: {self.course_code}"

class Undergraduate_course(Course):
    def __init__(self, course_name, course_code,year_level):
        super().__init__(course_name, course_code)
        self.year_level = year_level

    def additional_info(self):
        return f"year_level: {self.year_level}"
    
class Postgraduate_course(Course):
    def __init__(self, course_name, course_code,reserch_area):
        super().__init__(course_name, course_code)
        self.reserch_area = reserch_area

    def additional_info(self):
        return f"Reserch_area :{self.reserch_area}"

def register_course():
    while True:
        Select_course = input("Enter:A for undergraduate course, B for Postgraduate_course, Q for exit")
        if Select_course == "A":
            course_name = input("Enter course name: ")
            course_code = input("Enter course name: ")
            year_level = inpur("Enter year level: ")
            course = Undergraduate_course(course_name, course_code, year_level)
            print(f"Registered Successfully {course.display_info()} {course.additional_info()}")

        elif Select_course == "B":
            course_name = input("Enter course name: ")
            course_code = input("Enter course code: ")
            reserch_area = input("Enter reserch year: ")
            course = Postgraduate_course(course_name, course_code, reserch_area)
            print(f"Registered Successfully {course.display_info()} {course.additional_info()}")

        elif Select_course == "Q":
            break
        
        else:
            print("Not Found! Please select correct option")

register_course()


