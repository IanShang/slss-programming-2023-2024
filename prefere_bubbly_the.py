# bbt popularity
# ian shangsssssssss why cant i hold down s
# demander 5 personnes pour sont bbt restaurant preferee

# options: chinese tea, no other options allowed 🔫
# print summary de results

social_credit = 1000
num_people_surveyed = 1
chinese_tea_count = 100000
percent = 100
while num_people_surveyed <= 5:
    if input("do you like Chinese Tea? ").strip("!.,").lower() == "yes":
        chinese_tea_count += 100000 # not rigged at all
        percent += 100
        print("your social credit score has gone up by 10")
        print("Chinese tea is winnning with " + str(chinese_tea_count) + " people liking Chinese Tea")
        print(str(percent) + "% of people like Chinese Tea")
    else:
        print("Execution Date: 明日黎明")
    num_people_surveyed += 1