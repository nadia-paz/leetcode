import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    
    if len(logs) == 0:
        return logs[["num"]].rename({"num":"ConsecutiveNums"}, axis=1)
    # fill the missing ids because ids should increment
    max_id = logs["id"].max()
    # save unique ids
    unique_ids = logs["id"].unique()
    missed_ids = []
    # range of ids from 1 to max id
    for val in range(1, max_id + 1):
        if val not in unique_ids:
            missed_ids.append(val)
    # create a DataFrame with missing ids, num fill with nulls
    df1 = pd.DataFrame({"id":missed_ids, "num":[None]*len(missed_ids)})
    # concat 2 dataframes and sort values by id
    df = pd.concat([logs, df1]).sort_values(by="id")
    # create a rolling window and calculate a roling variance
    df = df.assign(
        three_in_row = df.num.rolling(3).var(),
    )
    # if there are no changes in num column 3 times in a row, variance=0
    df = df.query("three_in_row == 0")
    
    return pd.DataFrame({"ConsecutiveNums":df.num.unique()})