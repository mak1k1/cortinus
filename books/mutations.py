import graphene

from .types import AuthorType, BookType, CategoryType
from .models import Author, Book, Category


class CreateAuthorMutation(graphene.Mutation):
    class Arguments:
        """Input arguments for editing Author"""
        name = graphene.String()
        description = graphene.String()

    author = graphene.Field(AuthorType)

    def mutate(self, info, name, description):
        author = Author.objects.create(
            name=name,
            description=description
        )

        author.save()
        return CreateAuthorMutation(author=author)


class UpdateAuthorMutation(graphene.Mutation):
    class Arguments:
        """Input arguments for editing Author"""
        id = graphene.ID()
        name = graphene.String()
        description = graphene.String()

    author = graphene.Field(AuthorType)

    def mutate(self, info, id, name, description):
        author = Author.objects.get(pk=id)

        author.name = name
        author.description = description

        author.save()
        return UpdateAuthorMutation(author=author)


class CreateCategoryMutation(graphene.Mutation):
    class Arguments:
        """Input arguments for editing Category"""
        name = graphene.String()
        description = graphene.String()

    category = graphene.Field(CategoryType)

    def mutate(self, info, name, description):
        category = Category.objects.create(
            name=name,
            description=description
        )

        category.save()
        return CreateCategoryMutation(category=category)


class UpdateCategoryMutation(graphene.Mutation):
    class Arguments:
        """Input arguments for editing Category"""
        id = graphene.ID()
        name = graphene.String()
        description = graphene.String()

    category = graphene.Field(CategoryType)

    def mutate(self, info, id, name, description):
        category = Category.objects.get(pk=id)

        category.name = name
        category.description = description

        category.save()
        return UpdateCategoryMutation(category=category)


class CreateBookMutation(graphene.Mutation):
    class Arguments:
        """Input arguments for creating Book"""
        title = graphene.String()
        isbn = graphene.String()
        pages = graphene.Int()
        description = graphene.String()
        authors = graphene.List(graphene.ID)
        categories = graphene.List(graphene.ID)

    book = graphene.Field(BookType)

    def mutate(self, info, title, isbn, pages, description,
               authors, categories):
        book = Book.objects.create(
            title=title,
            isbn=isbn,
            pages=pages,
            description=description
        )

        if authors is not None:
            author_set = []
            for author_id in authors:
                author = Author.objects.get(pk=author_id)
                author_set.append(author)
            book.authors.set(author_set)

        if categories is not None:
            category_set = []
            for category_id in categories:
                category = Category.objects.get(pk=category_id)
                category_set.append(category)
            book.categories.set(category_set)

        book.save()
        return CreateBookMutation(book=book)

    
class UpdateBookMutation(graphene.Mutation):
    class Arguments:
        """Input arguments for creating Book"""
        id = graphene.ID()
        title = graphene.String(required=False)
        isbn = graphene.String(required=False)
        pages = graphene.Int(required=False)
        description = graphene.String(required=False)
        authors = graphene.List(graphene.ID, required=False)
        categories = graphene.List(graphene.ID, required=False)

    book = graphene.Field(BookType)

    def mutate(self, info, id, **kwargs):
        title = kwargs.get('title', None)
        isbn = kwargs.get('isbn', None)
        pages = kwargs.get('pages', None)
        description = kwargs.get('description', None)
        author_set = kwargs.get('authors', None)
        category_set = kwargs.get('categories', None)


        book = Book.objects.get(pk=id)

        if title is not None:
            book.title = title

        if isbn is not None:
            book.isbn = isbn

        if pages is not None:
            book.pages = pages

        if description is not None:
            book.description = description

        if author_set is not None:
            authors = []
            for author_id in author_set:
                author = Author.objects.get(pk=author_id)
                authors.append(author)
            book.authors.set(authors)

        if category_set is not None:
            categories = []
            for category_id in category_set:
                category = Category.objects.get(pk=category_id)
                categories.append(category)
            book.categories.set(categories)

        book.save()
        return UpdateBookMutation(book=book)