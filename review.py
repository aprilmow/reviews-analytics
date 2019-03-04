data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10 == 0: #every 10 review
			print(len(data)) #show reading progress

print('reading completed, total', len(data), 'data')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('average is', sum_len / len(data))