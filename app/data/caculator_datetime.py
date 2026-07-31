from datetime import datetime

print(1785504380/86400)


year_1972 = 1972
year_1970 = 1970

# if (year%4 ==0 and year% 100 != 0) or (year%100 == 0 and year% 400 ==0):
#     print("nam nhuan")

# else: 
#     print("kh nhuan")


# print(year_1972)

so_nam_nhuan = (datetime.now().year - year_1972)//4 + 1


so_nam_goc = (datetime.now().year - year_1970) + 1

print(so_nam_goc)