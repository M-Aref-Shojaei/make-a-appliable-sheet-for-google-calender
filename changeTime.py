import pandas as pd

df = pd.read_csv(
    r'/Users/arefshojaei/Downloads/data science.csv')
times = df[df.columns[5]].values.tolist()
# print(times)
fixed_times_s = []
fixed_times_e = []
for i in times:
    if type(i) == str:
        fixed_times_s.append(i[:5])
        fixed_times_e.append(i[-5:])
    else:
        fixed_times_s.append(None)
        fixed_times_e.append(None)

df['s'] = fixed_times_s
df['e'] = fixed_times_e

df.to_csv(r'/Users/arefshojaei/Downloads/data science fixed.csv')
