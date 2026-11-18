# GeoPy Reverse Geocoding Practice

A small Python example that converts latitude and longitude into a readable address with GeoPy and OpenStreetMap Nominatim.

## Example

The script uses sample coordinates in Tashkent:

```bash
python geo.py
```

To try another place, change the two numbers in the `__main__` block of `geo.py`. The function returns an address, or `None` when no result is found.

## Setup

```bash
python -m venv .venv
```

Activate the environment, then install the dependency:

**Windows PowerShell**
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Linux / macOS**
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage policy

This example calls the public Nominatim service. It sets a project-specific User-Agent and a request timeout. Keep requests user-triggered and below one request per second; do not use the public service for bulk or repeated automated lookups. See the [Nominatim Usage Policy](https://operations.osmfoundation.org/policies/nominatim/) and [GeoPy Nominatim documentation](https://geopy.readthedocs.io/en/stable/#geopy.geocoders.Nominatim).

## Technology

- Python
- GeoPy
- OpenStreetMap Nominatim
