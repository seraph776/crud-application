#!/usr/bin/env python3
"""
created: 2022-11-28
@author: seraph1001100
project: CRUD Application
"""
import csv
from book import Book


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.records = []

    def add_to_records(self, record):
        """Adds record to database"""
        print('Record added!')
        self.records.append(record)

    def view_database(self):
        """Views all records in database"""
        print('Viewing records:')
        for i, row in enumerate(self.records, start=1):
            print(f' • idx={i}, title={row.title}, author={row.author}, price={row.price}')
        print()

    def save_records(self):
        """Saves records to Database"""
        headers = ['title', 'author', 'price']
        with open(self.filename, mode='w', encoding='utf8', newline='') as file:
            dictWriter = csv.DictWriter(file, fieldnames=headers)
            dictWriter.writeheader()
            for item in self.records:
                title = item.title
                author = item.author
                price = item.price

                record = {'title': title, 'author': author, 'price': price}
                dictWriter.writerow(record)
        self.records.clear()
        print('Records have been saved!')

    def load_record(self):
        """Loads record from text file and loads them into records"""
        with open(self.filename, mode='r', encoding='utf8') as file:
            writer = csv.reader(file)
            next(writer)
            for item in writer:
                title, author, price = item[0], item[1], item[2]
                book = Book(title, author, float(price))
                self.records.append(book)
        print('Records loaded!')
        return self.records

    def create_record(self, title, author, price):
        """Creates a book class object and loads it into records"""
        book = Book(title, author, price)
        print('Record created!')
        self.records.append(book)

    def update_record(self, title, corrections: tuple):
        """Updates a record in teh database"""
        if title not in [i.title for i in self.records]:
            print(f'Record not found!')
        else:
            for i, item in enumerate(self.records):
                if title == item.title:
                    self.records[i] = Book(corrections[0], corrections[1], corrections[2])
                    print('Record update!')

    def delete_record(self, title):
        """Deletes a record from the database.,"""
        if title not in [i.title for i in self.records]:
            print(f'Record not found!')
        else:
            for i, item in enumerate(self.records):
                if title == item.title:
                    del self.records[i]
                    print('Record deleted!')
