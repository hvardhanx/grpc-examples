
import crawl_server
import unittest

class Test_Crawl(unittest.TestCase):
  def test_true_value(self):
    self.assertTrue(crawl_server.Get_info('GOOG') != '')

  def test_empty_value(self):
    self.assertRaises(AttributeError, crawl_server.Get_info, '')
  
  def test_invalid_value(self):
    self.assertRaises(AttributeError, crawl_server.Get_info, 'Samsung')

if __name__ == '__main__':
  unittest.main(exit=False)
