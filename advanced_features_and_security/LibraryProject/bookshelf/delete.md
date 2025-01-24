# Delete Command

```python
from bookshelf.models import Book

# Assuming the book instance was created earlier
book = Book.objects.get(title="1984")
book.delete()

# Confirm deletion
Book.objects.all()  # This should return an empty queryset if the book was deleted.
```
