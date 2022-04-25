import graphene
import graphql_jwt
import users.schema
import store.schema
import books.schema


class Query(books.schema.Query, store.schema.Query, users.schema.Query):
    pass


class AuthenticationMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Mutation(AuthenticationMutation, books.schema.Mutation, store.schema.Mutation, users.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
