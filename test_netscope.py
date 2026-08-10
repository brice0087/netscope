import unittest
from unittest.mock import patch

import netscope


class TestNetScope(unittest.TestCase):

    def test_dns_lookup_valid_domain(self):
        result = netscope.dns_lookup("localhost")
        self.assertIsNotNone(result)

    def test_dns_lookup_invalid_domain(self):
        result = netscope.dns_lookup("this-domain-should-not-exist.invalid")
        self.assertIsNone(result)

    @patch("netscope.socket.create_connection")
    def test_check_port_open(self, mock_connection):
        mock_connection.return_value.__enter__.return_value = True
        result = netscope.check_port("example.com", 443)
        self.assertTrue(result)

    @patch("netscope.socket.create_connection")
    def test_check_port_closed(self, mock_connection):
        mock_connection.side_effect = ConnectionRefusedError
        result = netscope.check_port("example.com", 443)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()