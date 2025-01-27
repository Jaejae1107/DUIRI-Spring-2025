import utm

def latlong_to_utm(latitude, longitude):
    """
    Converts latitude and longitude to UTM coordinates.
    
    Args:
        latitude (float): Latitude in decimal degrees.
        longitude (float): Longitude in decimal degrees.
        
    Returns:
        dict: A dictionary containing UTM coordinates and zone information.
    """
    easting, northing, zone_number, zone_letter = utm.from_latlon(latitude, longitude)
    return {
        "Easting": easting,
        "Northing": northing,
        "Zone Number": zone_number,
        "Zone Letter": zone_letter
    }

# Example: Convert latitude and longitude to UTM
latitude = 39.7565
longitude = -86.1710

utm_result = latlong_to_utm(latitude, longitude)
print(f"Latitude: {latitude}, Longitude: {longitude}")
print(f"UTM Coordinates: Easting: {utm_result['Easting']}, Northing: {utm_result['Northing']}")
print(f"Zone: {utm_result['Zone Number']}{utm_result['Zone Letter']}")
