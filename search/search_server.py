
import time
import json
import search_pb2
from six.moves import urllib
from grpc.beta import implementations


class GoogleServicer(search_pb2.BetaGoogleServicer):

  def Search(self, request, context):
    query = request.query
    query = urllib.urlencode({'q': query})
    response = urllib.urlopen(
        'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query)
    .read()
    _json = json.loads(response)
    results = _json['responseData']['results']
    for result in results:
      yield result


def serve():
  key_cert = [(open('../../../key.pem').read(),
              open('../../../cert.pem').read())]
  creds = implementations.ssl_server_credentials(key_cert, None,
                                                 False)
  server = search_pb2.beta_create_Google_server(GoogleServicer())
  server.add_secure_port('[::]:8000', creds)
  server.start()
  try:
    while True:
      time.sleep(86400)
  except KeyboardInterrupt:
    server.stop(0)


if __name__ == '__main__':
  serve()

            