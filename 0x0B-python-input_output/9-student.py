#!/usr/bin/python3
"""defines a class student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """intialize a new student.

        Args:
            first_name (str): The first name of student.
            last_name (str): The last name of student.
            age (int): the age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get dictionary rep of student"""
        return self.__dict__
