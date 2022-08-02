Aclass = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in Aclass:
    total += score #total = total + score 의 반복이기 때문에 결국 다 더한 값이 나옴.

average = total / len(Aclass) #리스트의 갯수를 리스트의 길이 len 으로 활용.
print(average)

