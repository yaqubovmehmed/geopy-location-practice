# GeoPy Reverse Geocoding Practice

A small Python example that converts latitude and longitude into a readable address with GeoPy and OpenStreetMap Nominatim.

## Example

The script uses sample coordinates in Tashkent:

\x60\x60\x60bash
python geo.py
\x60\x60\x60

To try another place, change the two numbers in the \x60__main__\x60 block of \x60geo.py\x60. The function returns an address, or \x60None\x60 when no result is found.

## Setup

\x60\x60\x60bash
python -m venv .venv
\x60\x60\x60

Activate the environment, then install the dependency:

**Windows PowerShell**
\x60\x60\x60powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
\x60\x60\x60

**Linux / macOS**
\x60\x60\x60bash
source .venv/bin/activate
pip install -r requirements.txt
\x60\x60\x60

## Usage policy

This example calls the public Nominatim service. It sets a project-specific User-Agent and a request timeout. Keep requests user-triggered and below one request per second; do not use the public service for bulk or repeated automated lookups. See the [Nominatim Usage Policy](https://operations.osmfoundation.org/policies/nominatim/) and [GeoPy Nominatim documentation](https://geopy.readthedocs.io/en/stable/#geopy.geocoders.Nominatim).

## Technology

- Python
- GeoPy
- OpenStreetMap Nominatim
