import http.client
import urllib.parse
import json
import env
import ssl

def get_dhl_tracking_info(tracking_number, api_key):
    params = urllib.parse.urlencode({
        'trackingNumber': tracking_number,
        'service': 'express'
    })

    headers = {
        'Accept': 'application/json',
        'DHL-API-Key': api_key
    }

    try:
        # Create an HTTPS connection (manually specifying the HTTPS scheme)
        connection = http.client.HTTPSConnection("api-eu.dhl.com", context=ssl._create_unverified_context())

        connection.request("GET", "/track/shipments?" + params, headers=headers)
        response = connection.getresponse()

        status = response.status
        reason = response.reason

        if status == 200:
            data = json.loads(response.read())
            connection.close()
            return data
        else:
            connection.close()
            return f"Error: Status {status} - {reason}"

    except Exception as e:
        return f"Request error: {str(e)}"

# Example usage:
if __name__ == "__main__":
    tracking_number = "7777777770"  # Replace with your tracking number
    api_key = env.DHL_API_KEY  # Use the API key from env.py

    tracking_info = get_dhl_tracking_info(tracking_number, api_key)
    print(json.dumps(tracking_info, indent=2))
