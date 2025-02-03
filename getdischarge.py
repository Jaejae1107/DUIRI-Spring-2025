import requests
import pandas as pd
from datetime import datetime

def download_usgs_discharge_data(site_no, start_date, end_date, output_file):
    """
    Downloads USGS discharge data for a given site and date range.
    :param site_no: USGS site number (e.g., '03353000')
    :param start_date: Start date in 'YYYY-MM-DD' format
    :param end_date: End date in 'YYYY-MM-DD' format
    :param output_file: Path to save the CSV file
    """
    base_url = "https://waterservices.usgs.gov/nwis/dv/"
    params = {
        "format": "json",
        "sites": site_no,
        "startDT": start_date,
        "endDT": end_date,
        "parameterCd": "00060",  # Discharge (flow rate)
        "siteStatus": "all"
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print("Error fetching data:", response.status_code)
        return
    
    data = response.json()
    
    try:
        time_series = data["value"].get("timeSeries", [])
        if not time_series:
            print("No data found for the given site and date range.")
            return
        
        records = []
        for entry in time_series[0]["values"][0]["value"]:
            records.append({
                "Date": entry["dateTime"].split("T")[0],
                "Discharge (cfs)": entry["value"]
            })
        
        df = pd.DataFrame(records)
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")
    except Exception as e:
        print("Error processing data:", e)

# Example usage
site_number = "03353000"
start_date = "2024-01-01"
end_date = "2025-01-01"
output_filename = "usgs_discharge_data.csv"

download_usgs_discharge_data(site_number, start_date, end_date, output_filename)
