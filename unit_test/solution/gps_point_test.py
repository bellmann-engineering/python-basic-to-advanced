import unittest

from gps_point import GpsPoint


class GpsPointTest(unittest.TestCase):

    def basic_test_lat(self):
        point = GpsPoint(52.372625, 10.734866)
        self.assertEqual(point.latitude, 52.372625)

    def basic_test_lng(self):
        point = GpsPoint(52.372625, 10.734866)
        self.assertEqual(point.longitude, 10.734866)

    def testParsing_lat(self):
        point = GpsPoint.parse("RoutingReponse: 49.460983,...ds.##äää,,, 11.061859")
        self.assertEqual(point.latitude, 49.460983)

    def testParsing_lng(self):
        point = GpsPoint.parse("RoutingReponse: 49.460983,...ds.##äää,,, 11.061859")
        self.assertEqual(point.longitude, 11.061859)

    def testUtm_zone(self):
        point = GpsPoint(52.372625, 10.734866)
        self.assertEqual(point.get_utm_zone(), "32U")


if __name__ == '__main__':
    unittest.main()
