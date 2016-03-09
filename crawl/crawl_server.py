
import time
import re
import crawl_pb2
from six.moves import urllib
from grpc.beta import implementations

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

# Get data from the web


def Get_info(name):
	url = "https://www.google.com/finance?q="
	url = url + name
	data = urllib.request.urlopen(url).read()
	data1 = data.decode("utf-8")
	search_ = re.search('meta itemprop="price"', data1)
	start = search_.start()
	end = start + 50
	new_data = data1[start:end]
	search_ = re.search('content="', new_data)
	start = search_.end()
	new_data1 = new_data[start:]
	search_ = re.search("/", new_data1)
	start = 0
	end = search_.end()-3
	final = new_data1[0:end]
	return final


class Crawl(crawl_pb2.BetaCrawlServicer):

    def GetData(self, request, context):
		res = Get_info(request.name)
		return crawl_pb2.StockPrice(result=res)


def serve():
	priv = [(open('../../../key.pem').read(), open('../../../cert.pem').read())]
	creds = implementations.ssl_server_credentials(priv, None, False)
	server = crawl_pb2.beta_create_Crawl_server(Crawl())
	server.add_secure_port('[::]:8000', creds)
	server.start()
	try:
		while True:
			time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		server.stop(0)


if __name__ == '__main__':
	serve()
