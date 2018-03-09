from .Person import PersonModel, all_persons, CreatePersonModel
import graphene


# 2. Define Query class
class PersonQuery(graphene.ObjectType):
    # Define return fields
    person = graphene.Field(lambda: PersonModel, id=graphene.Int())
    # 2.1 Simulate database query operation.
    #    * query method name must matches pattern `resolve_<field_name>`
    #    * return object type must matches to field's type
    def resolve_person(self, info, **args):
        for p in all_persons:
            if p.id == args.get("id"):    # Argument "id" must be defined with return field.
                return p

    #   List all possible conditions for field
    personsWithCondition = graphene.List(lambda: PersonModel, 
                                         id=graphene.Int(),
                                         age=graphene.Int(),
                                         name=graphene.String())
    def resolve_personsWithCondition(self, info, **args):
        print(info.context)    # Contents has been stored in info.
        args.get("age")
        return [p for p in all_persons if p.age==args.get("age")]

    #   Return all records
    persons = graphene.List(lambda: PersonModel)
    def resolve_persons(self, info):
        return all_persons


# 3. Define mutation query class for Update operation
#    https://www.howtographql.com/graphql-python/3-mutations/ 
class CreatePersonMutation(graphene.ObjectType):
    # Return field for CreatePersonMutation
    createdPerson = CreatePersonModel.Field()  # Field() method will triger CreatePersonModel construction

# 4. Generate Schema
#   Schema convert internal PersonQuery defination to User interface
#   Schema must be registered to http interace, such like Flask in this case.(See ws_server.py)
schema = graphene.Schema(query=PersonQuery, mutation=CreatePersonMutation)
