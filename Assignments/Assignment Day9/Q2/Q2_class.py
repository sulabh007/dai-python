class student:
    count = 0

    def __init__(self, name="", m1=0, m2=0, m3=0, gpa=0):
        student.count = student.count + 1
        self.__sid = "S" + str(student.count)
        self.__name = name
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
        self.__gpa = student.gpa(self)

    def __str__(self):
        str1 = f"""
        Student Details
        __________________
        
        Student id : {self.__sid}
        Name: {self.__name}
        M1 : {self.__m1}
        M2 : {self.__m2}
        M3 : {self.__m3}
        GPA : {self.__gpa}"""

        return str1
    
    def gpa(self):
        gpa=format(((1/3)*self.__m1)+((1/2)*self.__m2)+((1/4)*self.__m3),".2f")
        return gpa

    # getter methods
    def get_sid(self):
        return self.__sid

    def get_name(self):
        return self.__name

    def get_m1(self):
        return self.__m1

    def get_m2(self):
        return self.__m2

    def get_m3(self):
        return self.__m3
    
    def get_gpa(self):
        return self.__gpa

    # setter methods
    def set_name(self, name):
        self.__name = name

    def set_m1(self, m1):
        self.__m1 = m1

    def set_m2(self, m2):
        self.__m1 = m2

    def set_m3(self, m3):
        self.__m1 = m3
