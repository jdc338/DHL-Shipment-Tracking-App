import requests
import env

def get_dhl_service_point_locations(country_code, city, radius=None):
    # Define the API endpoint
    api_url = "https://api.dhl.com/location-finder/v1"

    # Construct the query parameters
    params = {
        "countryCode": country_code,
        "city": city,
        "radius": radius
    }

    headers = {
        "DHL-API-Key": env.DHL_API_KEY
    }

    try:
        # Send a GET request to the DHL Service Point API
        response = requests.get(api_url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            locations = [point["name"] for point in data]
            return locations
        else:
            return f"Error: {response.status_code} - {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Request error: {str(e)}"

# Example usage:
if __name__ == "__main__":
    country_code = "UK"  # Replace with the desired country code
    city = "London"  # Replace with the city name
    radius = 10  # Replace with the desired radius (or set to None)

    service_point_locations = get_dhl_service_point_locations(country_code, city, radius)
    print("Service Point Locations:")
    for location in service_point_locations:
        print(location)
