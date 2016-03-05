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
	for contact in xrange(3):
		phone = person.phone.add()
		if contact == 0:
			phone.number = raw_input("Enter mobile-number: ")
			phone.type = test_pb2.Person.MOBILE
		elif contact == 1:
			phone.number = raw_input("Enter home-number: ")
			phone.type = test_pb2.Person.HOME
		elif contact == 2:
			phone.number = raw_input("Enter work-number: ")
			phone.type = test_pb2.Person.WORK				

	response = stub.get_addrs(test_pb2.Person(name=person.name), _TIMEOUT_SECONDS)
	print "Test: " + response.person  		# Test: Hello, Harsh Vardhan!
	print person           					
	print len(person.phone)                 # Total phone-numbers added


if __name__ == '__main__':
	run()