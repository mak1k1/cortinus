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


class EditAuthorMutation(graphene.Mutation):
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
        return EditAuthorMutation(author=author)
