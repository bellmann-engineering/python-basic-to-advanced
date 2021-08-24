import re
import utm


class GpsPoint:

    def __init__(self, lat, lng):
        self._lat = lat
        self._lng = lng

    @property
    def latitude(self):
        return self._lat

    @property
    def longitude(self):
        return self._lng

    @classmethod
    def parse(cls, text: str):
        lat, lng = re.findall(r"\d+\.\d+", text)
        return cls(float(lat), float(lng))

    def to_utm(self):
        u = utm.from_latlon(self._lat, self._lng)
        return u

    def get_utm_zone(self):
        u = utm.from_latlon(self._lat, self._lng)
        return str(u[2]) + u[3]
