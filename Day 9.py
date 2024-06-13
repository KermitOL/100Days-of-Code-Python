Year = int(input("Enter your birth year: "))
if Year >= 1925 and Year <= 1946:
    print("You are a Traditionalist")
elif Year >= 1947 and Year <= 1964:
    print("You are a Baby Boomer")
elif Year >= 1965 and Year <= 1981:
    print("You are a Generation X")
elif Year >= 1982 and Year <= 1995:
    print("You are a Millenial")
elif Year >= 1996 and Year <= 2015:
    print("You are a Generation Z")
else:
    print("You are not a part of any generation")
