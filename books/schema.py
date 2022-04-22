import graphene

from .models import Author, Book, Category
from .types import AuthorType, BookType, CategoryType
from .mutations import CreateAuthorMutation, EditAuthorMutation


class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    author = graphene.Field(AuthorType, author_id=graphene.Int())

    books = graphene.List(BookType)
    book = graphene.Field(BookType, book_id=graphene.Int())

    categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, category_id=graphene.Int())

    def resolve_authors(self, info, **kwargs):
        return Author.objects.all().order_by('-name')

    def resolve_author(self, info, author_id):
        return Author.objects.get(pk=author_id)

    def resolve_books(self, info, **kwargs):
        return Book.objects.all().order_by('-title')

    def resolve_book(self, info, book_id):
        return Book.objects.get(pk=book_id)

    def resolve_categories(self, info, **kwargs):
        return Category.objects.all().order_by('-name')

    def resolve_category(self, info, category_id):
        return Category.objects.get(pk=category_id)


class Mutation(graphene.ObjectType):
    create_author = graphene.Field(CreateAuthorMutation)
    update_author = graphene.Field(EditAuthorMutation)


schema = graphene.Schema(query=Query, mutation=Mutation)
