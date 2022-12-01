#!/usr/bin/env python3
"""
created: 2022-11-29
@author: seraph1001100
project: 
"""
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    price: float
