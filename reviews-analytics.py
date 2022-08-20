import time
import progressbar

data =[]
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        bar.update(count)
print('檔案讀取完畢, 總共有', len(data), '筆資料')

print('---------------------------------------------')

sum_len = 0
for d in data:
    sum_len += len(d)
print('每筆留言平均長度', sum_len / len(data))

print('---------------------------------------------')

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')

print('---------------------------------------------')

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到good')

print('---------------------------------------------')

# 文字計數
start_time = time.time()
wc = {} # word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1    # 新增新的key進wc字典

for word in wc:
    if wc[word] > 10000000:
        print(word, wc[word])   # 顥示超過10000000次出現的字
end_time = time.time()
print('花了',end_time - start_time, '秒')

print('總共有', len(wc), '個字詞加入')  # 印出字典長度

while True:
    word = input('請問你想查什麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('查無此字, 請重新輸入')

print('感謝使用本查詢功能')