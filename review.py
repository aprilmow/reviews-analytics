data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10 == 0: #every 10 review
			print(len(data)) #show reading progress

print(len(data))
print(data[0])