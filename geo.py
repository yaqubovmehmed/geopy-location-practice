from typing import Optional

from geopy.geocoders import Nominatim


def get_location_name(latitude: float, longitude: float) -> Optional[str]:
    """Return a human-readable address for a latitude/longitude pair."""
    geolocator = Nominatim(
        user_agent="yaqubovmehmed-geopy-location-practice",
        timeout=10,
    )
    location = geolocator.reverse(
        (latitude, longitude),
        exactly_one=True,
    )
    return location.address if location else None


if __name__ == "__main__":
    # Example coordinates for Tashkent, Uzbekistan.
    address = get_location_name(41.2995, 69.2401)
    print(address or "No address found for these coordinates.")
    print("Geocoding data © OpenStreetMap contributors: https://www.openstreetmap.org/copyright")
