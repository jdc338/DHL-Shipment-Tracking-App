# DHL Shipment Tracking App

This application allows you to track the status of shipments using the DHL Shipment Tracking API. This has been built using Python to create the script and configure the API settings and Streamlit for building out an interface. The user inferface allows you to search for a tracking number before returning the tracking information in an easy to read format (this currently only works for 7777777770 as per brief). As a secondary function, the application contains a script that gets and returns the list of all DHL service point locations within the specified radius from the given address.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)

## Getting Started

### Prerequisites

- Python 3.7 or higher
- [DHL API Key](https://developer.dhl.com/) - I have provided in this instance!
- [Streamlit](https://www.streamlit.io/)

### Installation

1. Clone the repository.

    ```bash
    git clone git@github.com:jdc338/DHL-Shipment-Tracking-App.git
    ```

2. Navigate into the directory.

    ```bash
    cd DHL-Shipment-Tracking-App
    ```

3. Install the required packages.

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit Interface (Search for 7777777770).

    ```bash
    streamlit run interface.py
    ```

2. Run the Python Tracking Script 

    ```bash
    python dhl_tracking.py
    ```

3. Run the Python Locations Script 

    ```bash
    python dhl_locations.py
    ```

## Contributors

- James Corfe [@jdc338](https://github.com/jdc338)
