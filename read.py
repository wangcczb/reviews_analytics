#讀取資料
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1   # count = count + 1
		if count % 50000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data),'筆資料')

#計算留言平均長度
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度為',sum_len/len(data),'字')

#留言篩選(len<100)
# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
new = [d for d in data if len(d) < 100]
print('一共有', len(new),'筆留言長度小於100字')



#留言篩選(good)
# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)	
good = [d for d in data if 'good' in d]
print('一共有', len(good),'筆留言有good')


#留言篩選(bad,T/F)
bad = ['bad' in d for d in data]
print(bad)