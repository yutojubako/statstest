import stats_test as st
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("./statistic_dataset.csv")
    st.stats_test(df,val_col="impressions", group_col="Media", result=True)