# Q 1 

# Task 1

from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define database connection string (replace with your details)
engine = create_engine('postgresql://username:password@host:port/database_name')

# Create a base class for table models
Base = declarative_base()

# Define table models based on the schema
class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    isbn = Column(String(13), unique=True)
    publication_year = Column(Integer)
    price = Column(Float(10, 2))
    in_stock = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.author_id'))

class Author(Base):
    __tablename__ = 'authors'

    author_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

# Additional classes for Genres, Book_Genres (if implemented), Customers, and Transactions can be defined similarly

# Create database tables (if they don't already exist)
Base.metadata.create_all(engine)

# Create a session object for interacting with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example: Adding a new book
new_book = Book(title="The Hitchhiker's Guide to the Galaxy", isbn="9780345502577", publication_year=1979, price=12.99, in_stock=10, author_id=1)  # Replace author_id with actual ID
session.add(new_book)
session.commit()

# Example: Querying for books by title
books = session.query(Book).filter(Book.title.like("%Galaxy%")).all()
for book in books:
    print(f"Title: {book.title}, ISBN: {book.isbn}")

# Remember to close the session
session.close()

# Task 2

import matplotlib.pyplot as plt

entities = {"Books": [], "Authors": [], "Customers": [], "Transactions": []}  # List to store entities
relationships = [("Books", "Authors", "one-to-many"), ("Customers", "Transactions", "one-to-many")]  # List of relationships (entity1, entity2, cardinality)

plt.figure(figsize=(10, 6))  # Adjust figure size as needed

# Draw entities as circles
for entity, data in entities.items():
    plt.plot([], [], 'o', label=entity, markersize=20)

# Draw relationships as lines with labels
for rel in relationships:
    entity1, entity2, cardinality = rel
    x1, y1 = entities[entity1][0], entities[entity1][1]  # Get positions (replace with layout calculation if used)
    x2, y2 = entities[entity2][0], entities[entity2][1]
    plt.plot([x1, x2], [y1, y2], 'b-', alpha=0.7)
    plt.text((x1 + x2) / 2, (y1 + y2) / 2, cardinality, ha='center', va='center', fontsize=12)

plt.legend()
plt.title("BookHaven Database ERD")
plt.axis('off')
plt.show()

