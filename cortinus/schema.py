import graphene
import users.schema
import store.schema
import books.schema


class Query(books.schema.Query, store.schema.Query, users.schema.Query):
    pass


class Mutation(books.schema.Mutation, store.schema.Mutation, users.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
