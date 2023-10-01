import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

rating_df=pd.read_csv("rating11.csv")


only_rating=rating_df.drop(['userId', 'movieId','timestamp'], axis=1)

bar_data=only_rating.value_counts()
bar_data=bar_data.to_frame()
bar_data=bar_data.reset_index()

bar_data.columns =['Rating', 'Movie Count']
sns.barplot(x = 'Rating', y = 'Movie Count', data = bar_data)

plt.show()














