import pandas as pd


df = pd.read_csv('input1', skiprows=1, sep='\s+')
df['Used'] = df['Used'].str.replace('T', '').astype(int)
df['Avail'] = df['Avail'].str.replace('T', '').astype(int)
df['Size'] = df['Size'].str.replace('T', '').astype(int)
df['Filesystem'] = df['Filesystem'].str.replace('/dev/grid/node-', '')
df = df.set_index('Filesystem')

# Part one
viable = 0
used = df.Used.values
avail = df.Avail.values
for i in range(len(df)):
    if used[i] == 0:
        continue
    for j in range(len(df)):
        if i != j and used[i] <= avail[j]:
            viable += 1

print(viable)

# Part two
ss = []
for y in range(30):
    s = [str(y).zfill(2), ' ']
    for x in range(34):
        if x == 0 and y == 0:
            s.append('F')
        elif x == 33 and y == 0:
            s.append('G')
        elif df.loc[f'x{x}-y{y}'].Used == 0:
            s.append('_')
        elif df.loc[f'x{x}-y{y}'].Used > 90:
            s.append('#')
        else:
            s.append('.')
    ss.append(s)

print('\n'.join(''.join(s) for s in ss))
print(3 + 25 + 31 + 1 + 5*32)