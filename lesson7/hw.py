class ORM:

    @classmethod
    def create_table(cls, fields: list):
        print(cls.__name__.lower())
        raise NotImplemented

    def update(self):
        raise NotImplemented

    def delete(self):
        raise NotImplemented

    @classmethod
    def m2m_relationship(cls, other_cls):
        raise NotImplemented

    @classmethod
    def foreign_key(cls, other_cls):
        raise NotImplemented

    @classmethod
    def get_data_from_m2m(cls, rel):
        raise NotImplemented

    @classmethod
    def get_data_from_foreign(cls, rel):
        raise NotImplemented

    def set_data_to_m2m(self, rel):
        raise NotImplemented

    def set_data_to_foreign(self, rel):
        raise NotImplemented


class Student(ORM):
    pass


class Course(ORM):
    pass


class Laptop(ORM):
    pass


Student.create_table()
Course.create_table()

course = Course(1, "sdasd")
student = Student(1, " asdf,asd,f a,sdf,a,sdf,as")
student.update()
student.delete()
Student.m2m_relationship(Course)
Student.foreign_key(Laptop)

Student.get_data_from_m2m(course)
Student.get_data_from_foreign(course)

student.set_data_to_foreign(course)
student.set_data_to_m2m(course)
