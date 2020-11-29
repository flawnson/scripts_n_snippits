"""
There I was, working on the multiclass AUROC code with Clayton for our upcoming publication when suddenly, I get an email. Golly,
it's from Benjamin! Ben never emails me at this time... he only ever pops in to ask how many drugs I've found and to
steal my gum (jk Ben you're the best :) Ben just got handed over a spreadsheet of juicy information, but alas, the dates
were in an inappropriate format. And so my mission, as I have chosen to accept it, is to format the dates correctly.
"""

import datetime
import pandas as pd
import numpy as np

file = "/Users/flawnsontong/Documents/Juvenescence/AmgenNeuroTrials.csv"
dataframe = pd.read_csv(file)


def datatime_converter(dataframe, col_name):
    data_list = dataframe[col_name].tolist()
    new_format = []

    for data in data_list:
        if type(data) == str:
            new_data = datetime.datetime.strptime(data, '%b %d, %Y').strftime('%m/%d/%Y')  # Modify formats here
            new_format.append(new_data)
        elif type(data == float):
            new_format.append(np.nan)  # Redundant but just in case data has NaN (automatically detected as floats)
        else:
            continue

    return new_format


dataframe["Last Updated Date"] = datatime_converter(dataframe, "Last Updated Date")
dataframe["Record Creation Date"] = datatime_converter(dataframe, "Record Creation Date")

dataframe.to_csv(r"/Users/flawnsontong/Documents/Juvenescence/FormatedAmgenNeuroTrials.csv", index=False)
