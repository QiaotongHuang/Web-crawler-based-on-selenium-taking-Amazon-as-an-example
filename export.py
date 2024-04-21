import os
import csv
import time
from settings import current_dir

def write_to_csv(data):
    # Create the output directory if it doesn't exist
    isExists = os.path.exists(current_dir+'/outputs')
    if not isExists:
        os.makedirs(current_dir+'/outputs')

    file_name = current_dir+"/outputs/{}-amazon-crawl.csv".format(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    # Write the data to csv file
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

    return file_name


if __name__ == '__main__':
    # Test data will overwrite the file!!!
    data = [
        ["Name", "Price", "URL"],
        ["Apple iPhone 6", "$399.00", "http://www.amazon.com/dp/B00NQGP42Y"],
        ["Samsung Galaxy S6", "$579.00", "http://www.amazon.com/dp/B00V7FW1G6"],
        ["LG G4", "$459.00", "http://www.amazon.com/dp/B00YD547Q6"],
    ]
    file_name = write_to_csv(data)
    print("Data written to {}".format(os.path.abspath(file_name)))
