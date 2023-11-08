import requests
import env

def get_dhl_service_point_locations(country_code, city, radius=None):
    api_url = "https://api.dhl.com/location-finder/v1"
    
    params = {
        "countryCode": country_code,
        "city": city,
        "radius": radius
    }

    headers = {
        "DHL-API-Key": env.DHL_API_KEY
    }

    try:
        response = requests.get(api_url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            locations = [point["name"] for point in data]
            return locations
        else:
            return f"Error: {response.status_code} - {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Request error: {str(e)}"

if __name__ == "__main__":
    country_code = "UK"  
    city = "London"  
    radius = 10  

    service_point_locations = get_dhl_service_point_locations(country_code, city, radius)
    print("Service Point Locations:")
    for location in service_point_locations:
        print(location)
