import graphene
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations

# query user model
class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

# User Registration
class UserRegistration(graphene.ObjectType):
   register = mutations.Register.Field()
   verify_account = mutations.VerifyAccount.Field()
   token_auth = mutations.ObtainJSONWebToken.Field()


# define the mutations
class Mutation(UserRegistration, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)