data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10 == 0: #every 10 review
			print(len(data)) #show reading progress

#print('reading completed, total', len(data), 'data')

#print(data[0])

wc = {} #word count
for d in data: #每一個data清單中的留言
	words = d.strip().split() #split的預設值就是空格 且連續空格也會一起拿掉 
	for word in words: #每一個留言words中的單字
		if word in wc: #詞已經出現在字典裡
			wc[word] += 1
		else: 
			wc[word] = 1 #沒有出現過，把新的字加入字

for word in wc: #每一個key
	#if wc[word] > 100
		print(word, wc[word])

print(len(wc))

while True:
	word = input('what word you want to look for:')
	if word == 'q':
		break
	if word in wc:
		print(word, 'showed', wc[word], 'times') 
	else:
		print('there is no such word')