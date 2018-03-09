from .Person import Person, all_persons
import graphene


# 2. Define Query class
class Query(graphene.ObjectType):
    # Init return object
    person = graphene.Field(Person, id=graphene.Int())
    persons = graphene.List(Person)
    #persons_with_condition = graphene.List(lambda: Character)

    # 2.1 Semulate database query operation.
    #    * query method name must matches pattern `resolve_<obect_name>`
    #    * return object type must matches to above defination
    def resolve_person(self, info, **args):
        for p in all_persons:
            if p.id == args.get("id"):
                return p

    def resolve_persons(self, info):
        return all_persons

    #def reslove_persons_with_condition(self, info):

# 3. Generate Schema
#        Schema convert internal Query defination to User interface
#        It must be register to http interace, such like Flask in this case.
schema = graphene.Schema(query=Query)
