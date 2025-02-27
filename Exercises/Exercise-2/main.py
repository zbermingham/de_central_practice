import requests
import pandas as pd 
from bs4 import BeautifulSoup
import io


def main():
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    r = requests.request("GET", url=url)

    # Parse html with pandas
    html_df = pd.read_html(r.content)[0]

    # Filter pandas dataframe last modified on 2024-01-19 10:27
    filter_df = html_df.loc[(html_df['Last modified'] == '2024-01-19 10:27')]

    # Create unique list of files to download
    files_to_download = []
    for index, row in filter_df.iterrows():
        if row['Name'] not in files_to_download:
            files_to_download.append(row['Name'])

    # Download csv files from specified date
    for file in files_to_download:
        sub_r = requests.request("GET", url = url + file)
        df = pd.read_csv(io.BytesIO(sub_r.content), sep=',')
        
        # Save file content
        # df.to_csv(file, index=False)

        # Find max value, filter for values matching max value
        max_values = df['HourlyDryBulbTemperature'].max()
        filter_df = df.loc[(df["HourlyDryBulbTemperature"] == max_values)]
        print(filter_df)

if __name__ == "__main__":
    main()