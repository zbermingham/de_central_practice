import requests
import os
import zipfile
import io

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip"
    ,"https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip"
    ,"https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip"
    ,"https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip"
    ,"https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip"
    ,"https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip"
    ,"https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip"
]


def main():
    # Step 1: Check if downloads path exists
    path = "downloads"
    if os.path.exists(path):
        print(f"{path} already exists.")
    else:
        print(f"Making path: {path}")
        os.mkdir(path)

    # Step 2: Download zip files from uris
    for u in download_uris:
        # Make get request to uri
        response = requests.request(method="GET", url=u)

        # If response is good, save zip file to downloads folder
        if response.status_code == 200:
            file_name = u.split('.com/')[-1]
            zip = zipfile.ZipFile(io.BytesIO(response.content))
            print(zip.namelist())
            for file in zip.namelist():
                if file_name.strip('.zip') == file.strip('.csv'):
                    zip.extract(file, path=path)

if __name__ == "__main__":
    main()