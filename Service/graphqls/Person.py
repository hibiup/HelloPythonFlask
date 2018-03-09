import graphene

# Reference from: https://github.com/amitsaha/flask-graphql-demo/blob/master/schema.py

# 1. Define module
class Person(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    age = graphene.Float()
    avatar = graphene.String()

# 1.1 Semulate dataset:
p1 = Person()
p2 = Person()

p1.id = 1
p1.age = 34
p1.name = 'Jack'

p2.id = 2
p2.age = 34
p2.name = 'Adam'

all_persons = [p1, p2]