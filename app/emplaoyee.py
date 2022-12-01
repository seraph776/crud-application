#!/usr/bin/env python3
"""
created: 2022-11-28
@author: seraph1001100
project: CRUD Application
"""


class Employee:
    def __init__(self, firstname, lastname, position, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.salary = salary

    @property
    def email(self):
        return f'{self.firstname[0]}{self.lastname}@sheridancollege.ca'

    def __repr__(self):
        return f'{self.__class__.__name__}(firstName={self.firstname},lastName={self.lastname}, email={self.email}, ' \
               f'position={self.position}, salary={self.salary})'


