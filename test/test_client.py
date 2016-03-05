from grpc.beta import implementations

import test_pb2

_TIMEOUT_SECONDS = 5

def run():
	channel = implementations.insecure_channel('localhost', 2000)
	stub = test_pb2.beta_create_Address_stub(channel)
	person = test_pb2.Person()
	person.id = 1234
	person.name = "Harsh Vardhan"
	person.email = "harsh@vardhan.com"
	phone = person.phone.add()
	phone.number = "888-888-888"
	phone.type = test_pb2.Person.HOME
	response = stub.get_addrs(test_pb2.Person(name=person.name), _TIMEOUT_SECONDS)
	print "Test: " + response.person
	print phone


if __name__ == '__main__':
	run()