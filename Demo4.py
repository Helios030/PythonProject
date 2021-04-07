year = int(input("pls input year: \n"))
month = int(input("pls input month: \n"))
day = int(input("pls input day: \n"))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month < 12:
    sum = months[month - 1]
else:
    print("input date error")

sum += day

leap = 0

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("闰年加一天")
    leap = 1
if leap == 1 and (month > 2):
    sum += 1

print("this date in year {}th day".format(str(sum)))
