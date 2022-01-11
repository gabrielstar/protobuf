import addressbook_pb2

person = addressbook_pb2.Person()
person.id = 1234
person.name = "Joe Doe"
person.email = "x@wp.pl"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME
print(person)
print(person.SerializeToString()) #string ready to be send over network
data = b'\n\x07Joe Doe\x10\xd2\t\x1a\x07x@wp.pl"\x0c\n\x08555-4321\x10\x01'
new_person = None
new_person.ParseFromString(data)

