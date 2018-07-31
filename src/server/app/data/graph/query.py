# http://graphql.github.io/learn/queries/
# Avoid select * | Use IDs, let the child resolve its fields |
# https://weblogs.asp.net/jongalloway/the-real-reason-select-queries-are-bad-index-coverage

import graphene

from app.data.db import DB
from app.data.graph.user import User

db = DB()

class Query(graphene.ObjectType):
    users = graphene.List(User, prefix=graphene.String())

    def resolve_users(self, info, prefix):
        return db.get_users_all(prefix=prefix)

schema = graphene.Schema(query=Query)

if __name__ == "__main__":
    query = '''
        query SummonTheHeroes($prefix: String = "Bra") {
            heroes: users(prefix: $prefix){
                __typename
                ...userNameFra
            }
        }
    
        fragment userNameFra on User{
                name
                email
            }     
    '''

    result = schema.execute(query)
    print(result.data)

    iQuery = '''
        {
            __schema {
                types {
                    name
                }
            }
        }
    '''
    result = schema.execute(iQuery)
    print(result.data)