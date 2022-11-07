from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base
from Enrollment import Enrollment

class Section():
    __tablename__ = 'Section'
    sectionID = Column(Integer, primary_key=True)
    departmentName = Column(String)
    courseName = Column(String)
    sectionNumber = Column(Integer)
    semester = Column(String)
    year = Column(Integer)

    enrollments = relationship("Enrollment", back_populates="section")

    def __init__(self, departmentName, courseName, sectionNumber, semester, year):
        self.departmentName = departmentName
        self.courseName = courseName
        self.sectionNumber = sectionNumber
        self.semester = semester
        self.year = year
        self.enrollments = []

    def add_section(self, section):
        self.enrollments.append(section)

    def del_section(self, section):
        self.enrollments.remove(section)

    def __str__(self):
        return f"{self.departmentName} {self.courseName} {self.sectionNumber} {self.semester} {self.year}"