import graphene

# Reference from: 
#     https://github.com/amitsaha/flask-graphql-demo/blob/master/schema.py
#     https://www.howtographql.com/graphql-python/1-getting-started/

# 1. Define module for general usage
class PersonModel(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    age = graphene.Float()
    avatar = graphene.String()
    def __init__(self, id=None, name=None, age=None, avatar=None):
        self.id = id
        self.name = name
        self.age = age
        self.avatar = avatar

#  Semulate dataset:
p1 = PersonModel()
p1.id = 1
p1.age = 34
p1.name = 'Jack'

p2 = PersonModel()
p2.id = 2
p2.age = 15
p2.name = 'Adam'

p3 = PersonModel()
p3.id = 3
p3.age = 34
p3.name = 'Bob'

all_persons = [p1, p2, p3]

# 1.1 Define mutation class for update operation
class CreatePersonModel(graphene.Mutation, PersonModel):
    # Define accepted arguments
    class Arguments:
        age = graphene.Int()
        name = graphene.String()
        avatar = graphene.String()
    
    # mutation class must be defined with a mutate() method with above accepted arguments.
    def mutate(self, info, name, age, avatar):
        newPerson = CreatePersonModel(len(all_persons)+1, name, age, avatar)
        all_persons.append(newPerson)
        return newPerson