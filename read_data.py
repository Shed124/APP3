def data_reading(csv):
    if not csv.endswith('.csv'):
        return None
    with open(csv) as f:
        lines = f.readlines()

    headers = lines[0].strip().split(',')
    data = [dict(zip(headers, line.strip().split(','))) for line in lines[1:]]

    return data

a=data_reading("parcoursup_small_10000.csv")
b=data_reading("parcoursup_small_10000.cs")
print(a)
print(b)