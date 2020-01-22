from fitparse import FitFile
import pandas as pd


def parse(file_name):
    fitfile = FitFile(file_name)
    data = []

    # Get all data messages that are of type record
    for record in fitfile.get_messages('record'):
        data_record = {}
        # Go through all the data entries in this record
        for record_data in record:

            data_record[record_data.name] = record_data.value

        data.append(data_record)

    df = pd.DataFrame(data)
    return df
