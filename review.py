data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10 == 0: #every 10 review
			print(len(data)) #show reading progress

print('reading completed, total', len(data), 'data')

sum_len = 0 #sum一開始為0
for d in data:
	sum_len = sum_len + len(d) #使sum累計
print('average is', sum_len / len(data))

new = [] #create new
for d in data: #每一筆留言
	if len(d) < 100:
		new.append(d) #加到new這個集合
print('there are', len(new), 'reviews which lenth are shorter than 100')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('there are', len(good), 'reviews that mention good')