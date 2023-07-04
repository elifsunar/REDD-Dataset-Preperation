import pandas as pd

# veri dosyasını yükle
df = pd.read_csv('house_2chanel_7_commadelimited.csv', sep=',', header=None, names=['timestamp', 'power'])

# 10 dakikalık rulo hareketli ortalamayı hesapla
rolling_mean = df['power'].rolling(window=600).mean()

# threshold değerinden büyük olan indeksleri bul
indexes = rolling_mean[rolling_mean > 4].index

# aralıkları bul
threshold = 4
start_end_pairs = []
start_index = None
for index in indexes:
    if start_index is None:
        start_index = index
    elif index > start_index + 600:
        # end_index = sonraki index - 1
        end_index = index - 1
        start_end_pairs.append((start_index, end_index))
        start_index = None

# bulunan aralıkları ekrana yazdır
for start, end in start_end_pairs:
    print(f'start: {start}, end: {end}')
