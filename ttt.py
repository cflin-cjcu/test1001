data = []
b = []
with open("read.txt", 'r') as file:
    data = file.readlines()
    file.close()
for s in data:
    print(s)
    a = s.split()
    a[1] = eval(a[1])
    a[2] = eval(a[2])
    b.append(a)

hs = 0
ws = 0
h_max = b[0][1]
h_name = b[0][0]
w_max = b[0][2]
w_name = b[0][0]
for i in b:
    hs += i[1]
    ws += i[2]
    if i[1] > h_max:
        h_max = i[1]
        h_name = i[0]
    if i[2] > w_max:
        w_max = i[2]
        w_name = i[0]
print('Average height: %.2f' % (hs/len(b)))
print('Average weight: %.2f' % (ws/len(b)))
print('The tallest is %s with %.2fcm' % (h_name, h_max))
print('The heaviest is %s with %.2fkg' % (w_name, w_max))
