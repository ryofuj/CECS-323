-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-08-27 23:16:34.497

-- tables
-- Table: students
CREATE TABLE students (
    student_id int  NOT NULL,
    first_name varchar(40)  NOT NULL,
    last_name varchar(40)  NOT NULL,
    grade_point_average decimal(3,2)  NULL,
    major varchar(20)  NULL,
    year_of_study varchar(20)  NOT NULL,
    CONSTRAINT grade_point_average_range CHECK (grade_point_average > 0 and grade_point_average < 5) NOT DEFERRABLE INITIALLY IMMEDIATE,
    CONSTRAINT students_pk PRIMARY KEY (student_id)
);

-- End of file.

