#!/usr/bin/env python3
"""
created: 2022-11-29
@author: seraph1001100
project: 
"""
from book import Book
from database import Database


def main():
    database = Database('books.txt')
    # CRUD - Create
    database.create_record('The Art of War', 'Sun Tzŭ', 40.00)
    database.create_record('The Prince', 'Niccolò Machiavelli', 20.0)
    database.create_record('Dracula', 'Bram Stoker', 18.25)
    database.create_record('Paradise Lost', 'John Milton', 10.75)
    # CRUD - Read
    database.view_database()
    # CRUD - Update
    database.update_record('The Wizard of Oz', ('Foo', 'Bar', 10000.00))  # Record not found!
    database.update_record('The Prince', ('Foo', 'Bar', 10000.00))  # Record updated
    # correcting record:
    database.update_record('Foo', ('The Odyssey', 'Homer', 75.25))  # Record will update!
    # View DB
    # database.view_database()
    # CRUD - Delete
    database.delete_record('Foobar')  # Record will  not delete
    database.delete_record('The Wizard of Oz')
    database.view_database()
    # Save Data:
    database.save_records()
    # Load data
    database.load_record()
    database.view_database()


if __name__ == '__main__':
    main()
