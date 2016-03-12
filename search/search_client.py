
from grpc.beta import implementations

import search_pb2
import curses

_TIMEOUT_ = 30


def run():
  creds = implementations.ssl_channel_credentials(open('../../../cert.pem'
                                                       ).read(), None, None)
  channel = implementations.secure_channel('localhost', 8000, creds)
  stub = search_pb2.beta_create_Google_stub(channel)
  search = raw_input('Google: ')
  query = search_pb2.Request(query=search)
  results = stub.Search.future(query, _TIMEOUT_)
  for result in results:
    print result.title + '\n' + result.url + '\n' + result.content

if __name__ == '__main__':
  run()
