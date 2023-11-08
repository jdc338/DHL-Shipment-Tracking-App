import streamlit as st
import env
from dhl_tracking import get_dhl_tracking_info

st.set_page_config(page_title="DHL Tracking App", page_icon="📦")

st.title("DHL Shipment Tracking")

tracking_number = st.text_input("Enter Tracking Number")
api_key = env.DHL_API_KEY

if st.button("Track Shipment"):
    if tracking_number:
        tracking_info = get_dhl_tracking_info(tracking_number, api_key)

        if "error" in tracking_info:
            st.error(f"Error: {tracking_info['error']}")
        else:
            # Display formatted tracking information
            st.subheader("Tracking Information:")
            for shipment in tracking_info["shipments"]:
                st.write(f"Shipment ID: {shipment['id']}")
                st.write(f"Service: {shipment['service']}")
                st.write(f"Status: {shipment['status']['statusCode']}")
                st.write(f"Timestamp: {shipment['status']['timestamp']}")
                st.write(f"Description: {shipment['status']['description']}")
                st.write("-" * 30)  # Separator for each shipment
    else:
        st.error("Please enter a tracking number.")

if __name__ == "__main__":
    st.write("To track a shipment, enter the tracking number and click the 'Track Shipment' button.")
