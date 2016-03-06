
from grpc.beta import implementations
import re
import crawl_pb2
from six.moves import urllib
_TIMEOUT_SECONDS = 5


def run():
    channel = implementations.insecure_channel('localhost', 8000)
    stub = crawl_pb2.beta_create_Crawl_stub(channel)
    stock = crawl_pb2.StockName()
    stock.name = raw_input("Enter your stock(e.g. FB, GOOG): ")
    response = stub.GetData(crawl_pb2.StockName(name=stock.name), _TIMEOUT_SECONDS)
    print "The value of " + stock.name.upper() + " is " + response.result


if __name__ == '__main__':
	run()
