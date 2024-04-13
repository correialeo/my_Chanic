from dataclasses import dataclass

@dataclass
class Localizacao:
    _latitude: float
    _longitude: float

    def __str__(self):
        return f"Latitude: {self._latitude}, Longitude: {self._longitude}"