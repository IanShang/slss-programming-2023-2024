# no skill issue sem w
# ian shanks
# 5/11/2023

courses = [1, 2, 3, 4]
total_rt = 0
for course in courses:
    rating = input("comment as tu dans classe numero " + str(course) + ", 1-5: ").strip(",.?!").lower()
    total_rt += int(rating)
if total_rt != 20:
    print("skill issue fr")
else: print("il n'ya pas une skill issue")