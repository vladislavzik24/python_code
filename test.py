x = int(input())
y = int(input())
if x > 0:
    if y > 0:               # x>0, y>0
        print("Первая четверть")
    else:                   # x>0, y<0
        print("Четвертая четверть")
else:
    if y > 0:               # x<0, y>0
        print("Вторая четверть")
    else:                   # x<0, y<0
        print("Третья четверть")