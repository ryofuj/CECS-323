from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base


class Enrollment(Base):
    __tablename__ = 'Enrollment'
    studentID = Column(String, ForeignKey('Student.studentID'), primary_key=True)
    sectionID = Column(Integer, ForeignKey('Section.sectionID'), primary_key=True)

    student = relationship("Student", back_populates="enrollments")
    section = relationship("Section", back_populates="enrollments")

    '''create instance of the junction table
    @param  student: Student
    @param  section: Section'''
    def __init__(self, student, section):
        self.student = student
        self.section = section
        self.student.sections.append(self.section)

    def __str__(self):
        return f"{self.student} {self.section}"