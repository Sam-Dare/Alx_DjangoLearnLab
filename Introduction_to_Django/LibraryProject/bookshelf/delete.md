# Delete Operation

```python
# Delete the book instance
book.delete()
# Output: (1, {'bookshelf.Book': 1})

# Verify the deletion by attempting to retrieve all books
Book.objects.all()
# Output: <QuerySet []>
```
