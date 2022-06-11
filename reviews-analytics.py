data =[]
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完畢, 總共有', len(data), '筆資料')

print('---------------------------------------------')

sum_len = 0
for d in data:
    sum_len += len(d)
print('平均字數是', sum_len / len(data))