
from grpc.beta import implementations
import crawl_pb2

_TIMEOUT_SECONDS = 5


def run():
  creds = implementations.ssl_channel_credentials(open('../../../cert.pem'
                                                       ).read(), None, None)
  channel = implementations.secure_channel('localhost', 8000, creds)
  stub = crawl_pb2.beta_create_Crawl_stub(channel)
  stock = crawl_pb2.StockName()
  stock.name = raw_input('Enter your stock(e.g. FB, GOOG): ')
  response = stub.GetData.future(crawl_pb2.StockName(name=stock.name),
                                 _TIMEOUT_SECONDS)
  for res in response:
  	print 'The value of ' + stock.name.upper() + ' is ' + res.result


if __name__ == '__main__':
	run()
