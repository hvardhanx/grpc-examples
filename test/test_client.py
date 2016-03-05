from grpc.beta import implementations

import test_pb2

_TIMEOUT_SECONDS = 5

def run():
	channel = implementations.insecure_channel('localhost', 2000)
	stub = test_pb2.beta_create_Address_stub(channel)
	person = test_pb2.Person()
	person.id = int(raw_input("Enter your ID: "))
	person.name = raw_input("Enter your name: ")
	person.email = raw_input("Enter your email: ")
	phone = person.phone.add()
	phone.number = raw_input("Enter your phone-number: ")
	phone.type = test_pb2.Person.HOME
	response = stub.get_addrs(test_pb2.Person(name=person.name), _TIMEOUT_SECONDS)
	print "Test: " + response.person
	print person


if __name__ == '__main__':
	run()