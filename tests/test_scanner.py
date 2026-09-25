import unittest
from unittest.mock import patch

from scanner import scan_port, scan_ports, validate_ip


class ScannerTests(unittest.TestCase):
    def test_valid_ipv4(self):
        self.assertTrue(validate_ip("127.0.0.1"))
        self.assertTrue(validate_ip("192.168.1.10"))

    def test_invalid_ipv4(self):
        self.assertFalse(validate_ip("999.1.1.1"))
        self.assertFalse(validate_ip("not-an-ip"))
        self.assertFalse(validate_ip("2001:db8::1"))

    @patch("scanner.socket.socket")
    def test_scan_port_open(self, mock_socket):
        instance = mock_socket.return_value.__enter__.return_value
        instance.connect_ex.return_value = 0

        self.assertTrue(scan_port("127.0.0.1", 80))

    @patch("scanner.socket.socket")
    def test_scan_port_closed(self, mock_socket):
        instance = mock_socket.return_value.__enter__.return_value
        instance.connect_ex.return_value = 111

        self.assertFalse(scan_port("127.0.0.1", 80))

    @patch("scanner.scan_port", side_effect=[True, False])
    def test_scan_ports(self, mock_scan):
        result = scan_ports("127.0.0.1", [22, 80])

        self.assertEqual(result[0]["status"], "open")
        self.assertEqual(result[1]["status"], "closed")


if __name__ == "__main__":
    unittest.main()
