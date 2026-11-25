import unittest
from app import get_data


class TestApp(unittest.TestCase):
    def test_data(self):
        data = get_data()
        self.assertEqual(data["app"], "telemetry")
        self.assertIn("version", data)


if __name__ == "__main__":
    unittest.main()