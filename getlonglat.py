import requests

def get_lat_lon_from_address(address, api_key):
    """
    Converts a given address to latitude and longitude using OpenCage Geocoder API.
    
    Args:
        address (str): The address to be geocoded.
        api_key (str): OpenCage API key.
        
    Returns:
        tuple: Latitude and Longitude of the given address.
    """
    url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        "q": address,
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data["status"]["code"] == 200 and data["results"]:
        latitude = data["results"][0]["geometry"]["lat"]
        longitude = data["results"][0]["geometry"]["lng"]
        return latitude, longitude
    else:
        raise Exception(f"Error: {data['status']['code']} - {data['status']['message']}")

# Example usage
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenCage API key
    api_key = "6d5aea3db46549e69921996c89a099a8"
    address = "650 W. Henry Street, 46225, Indianapolis, Indiana, USA"
    
    try:
        latitude, longitude = get_lat_lon_from_address(address, api_key)
        print(f"Address: {address}")
        print(f"Latitude: {latitude}, Longitude: {longitude}")
    except Exception as e:
        print(e)
