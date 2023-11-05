import pandas as pd

df = pd.read_csv(
    r'C:\Users\Aref\Desktop\برنامه زمانی بوتکمپ Data science&Machine learning - برنامه کلاسی.csv')
times = df[df.columns[5]].values.tolist()
# print(times)
fixed_times = []
for i in times:
    if type(i) == str:
        fixed_times.append({'s': i[:5], 'e': i[-5:]})
    else:
        fixed_times.append(None)

changed_times = pd.DataFrame(fixed_times, columns=[df.columns[5]])

# df[df.columns[5]] = changed_times

# df.to_csv(r'C:\Users\Aref\Desktop\class sheet fixed.csv')
