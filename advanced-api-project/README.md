# Advanced API Project

This project is designed to demonstrate advanced API development using Django REST Framework. Below are the details of the views implemented in this project.

## Endpoints and Views

### 1. `/api/books/` (Book List View)

- **HTTP Method:** GET
- **Description:** Retrieves a list of all books in the database.
- **View Class:** `BookListView`
- **Behavior:**
  - Uses the `ListAPIView` class.
  - Serializes data using `BookSerializer`.

### 2. `/api/books/<int:pk>/` (Book Detail View)

- **HTTP Method:** GET
- **Description:** Retrieves the details of a single book identified by its ID.
- **View Class:** `BookDetailView`

### 3. `/api/books/create/` (Book Create View)

- **HTTP Method:** POST
- **Description:** Allows authenticated users to add a new book.
- **View Class:** `BookCreateView`
- **Custom Behavior:**
  - **Validation:** Ensures `publication_year` is not in the future.

### 4. `/api/books/<int:pk>/update/` (Book Update View)

- **HTTP Method:** PUT/PATCH
- **Description:** Allows authenticated users to update an existing book.
- **View Class:** `BookUpdateView`

### 5. `/api/books/<int:pk>/delete/` (Book Delete View)

- **HTTP Method:** DELETE
- **Description:** Allows authenticated users to delete a book.
- **View Class:** `BookDeleteView`

## Permissions

- **ListView and DetailView:** Accessible to all users.
- **Create, Update, Delete Views:** Restricted to authenticated users only.

## Customizations

- **Custom Validation:**
  - Implemented in `BookCreateView` to validate that `publication_year` is not in the future.

## Testing

To test these views, use tools like Postman or curl to send requests to the API endpoints.

## Running the Project

1. Start the server: `python manage.py runserver`
2. Visit the admin panel at `/admin/` to manage data manually.
3. Use `/api/books/` endpoints to interact with the API.

## Filtering, Searching, and Ordering in Book API

### Features

#### Filtering

- Filter by `title`, `author`, and `publication_year`.
- Example:

#### Searching

- Search by `title` and `author`.
- Example:

#### Ordering

- Order results by `title` or `publication_year`.
- Default ordering is by `title`.
- Example:

### Implementation Details

- Added `DjangoFilterBackend` for filtering.
- Configured `SearchFilter` for text-based search.
- Set up `OrderingFilter` for result sorting.

## API Unit Testing

### Testing Strategy

The following aspects of the Book API have been tested:

- **CRUD Operations:**
  - Create: Verify that books can be created successfully by authenticated users.
  - Read: Ensure book details and lists are retrieved correctly.
  - Update: Validate updates to book details.
  - Delete: Check that books are deleted properly with the correct permissions.
- **Advanced Features:**
  - Filtering: Test filtering by `title`, `author`, and `publication_year`.
  - Searching: Test full-text search on `title` and `author`.
  - Ordering: Test sorting by `title` and `publication_year`.
- **Authentication and Permissions:**
  - Ensure endpoints enforce authentication for restricted actions.

### Running Tests

1. Run the test suite:
   ```bash
   python manage.py test api
   ```
