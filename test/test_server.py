
import time

import test_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Address(test_pb2.BetaAddressServicer):

    def get_addrs(self, request, context):
        return test_pb2.AddressBook(person='Hello, %s!' % request.name)


def serve():
    server = test_pb2.beta_create_Address_server(Address())
    server.add_insecure_port('[::]:2000')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

      