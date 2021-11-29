wualgeup = 0
while True:
    startTime = float(input('시작 시간 : '))
    if startTime < 0: break
    endTime = float(input('끝난 시간 : '))
    n = endTime - startTime
    wualgeup += n * 10000

wualgeup = format(int(wualgeup), ',')
print('이번달 월급 : ', wualgeup, '원')