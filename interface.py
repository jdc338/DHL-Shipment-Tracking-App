import streamlit as st
import env
from dhl_tracking import get_dhl_tracking_info  # Import the tracking function from dhl_tracking

# Set Streamlit page configuration
st.set_page_config(page_title="DHL Tracking App", page_icon="📦")

# Streamlit UI
st.title("DHL Shipment Tracking")

# Input fields
tracking_number = st.text_input("Enter Tracking Number")
api_key = env.DHL_API_KEY  # Use the API key from env.py

# Button to trigger tracking
if st.button("Track Shipment"):
    if tracking_number:
        # Call the DHL tracking function to get tracking information
        tracking_info = get_dhl_tracking_info(tracking_number, api_key)

        if "error" in tracking_info:
            st.error(f"Error: {tracking_info['error']}")
        else:
            # Display formatted tracking information
            st.subheader("Tracking Information")
            for shipment in tracking_info["shipments"]:
                st.write(f"Shipment ID: {shipment['id']}")
                st.write(f"Service: {shipment['service']}")
                st.write(f"Status: {shipment['status']['statusCode']}")
                st.write(f"Timestamp: {shipment['status']['timestamp']}")
                st.write(f"Description: {shipment['status']['description']}")
                st.write("-" * 30)  # Separator for each shipment
    else:
        st.error("Please enter a tracking number.")

# Example usage:
# This block is executed only if the script is run outside Streamlit.
if __name__ == "__main__":
    st.write("To track a shipment, enter the tracking number and click the 'Track Shipment' button.")
