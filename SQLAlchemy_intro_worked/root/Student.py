from sqlalchemy import Column, Integer, String, ForeignKey, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from orm_base import Base
from Enrollment import Enrollment

class Student():
    __tablename__ = 'Student'
    studentID = Column(String, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    enrollments = relationship("Enrollment", back_populates="student")
    table_args = (UniqueConstraint('firstName', 'lastName', name='student_name_uc'),)
    section_list: [Enrollment] = relationship("Enrollment", back_populates="student", viewonly=False)

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.section_list = []

    def add_Student(self, student):
        self.section_list.append(student)

    def del_student(self, student):
        self.section_list.remove(student)

    def __str__(self):
        return f"{self.firstName} {self.lastName} {self.studentID}"