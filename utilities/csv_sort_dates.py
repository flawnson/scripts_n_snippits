"""
Fresh off the date converter mission, I was back to cracking away at multiclass AUROC problem. Suddenly it struck me
that there was no point in converting the dates to the correct format if the ros weren't in the right order. So I
quickly drafted the following:
"""

import pandas as pd

file = "/Users/flawnsontong/Documents/Juvenescence/AmgenNeuroTrials.csv"
dataframe = pd.read_csv(file)


def orderer(dataframe):
    dataframe['Record Creation Date'] = pd.to_datetime(dataframe["Record Creation Date"])
    new_dataframe = dataframe.sort_values(by='Record Creation Date', ascending=False)  # Boss wanted newest to oldest

    return new_dataframe


new_df = orderer(dataframe)
new_df.to_csv(r"/Users/flawnsontong/Documents/Juvenescence/FormatedOrderedAmgenNeuroTrials.csv", index=False)
