mid=int(input('請輸入期中考成績'))
final=int(input('請輸入期末考成績'))
average=mid*.4+final*0.6
score=(average**0.5)*10
print('平均是'+str(round(score, 1)))
