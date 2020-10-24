print("過輕 BMI < 18.5")
print("正常 18.5 <= BMI < 24")
print("過重 24 <= BMI < 27")
print("輕度肥胖 27 <= BMI < 30")
print("中度肥胖 30 <= BMI < 35")
print("重度肥胖 35 <= BMI")

height = input("輸入你的身高(cm):")
height = float(height)
h = height/100
weight = input("輸入你的體重(kg):")
weight = float(weight)
w = 24*(h**2)
bmi = weight / h**2
print("你的BMI是:", round(bmi, 2))

if bmi < 18.5:
    print("你過輕，如果要變正常")
    print("你至少還要增重", round(18.5*(h**2) - weight, 2), "公斤")
    print("也就是到", round(18.5*(h**2), 2), "公斤")
elif 18.5 <= bmi <24:
    print("你很正常ㄛ，繼續保持")
elif 24 <= bmi < 27:
    print("你過重，如果要變正常")
    print("你至少還需要減重", round(weight - w, 2), "公斤")
    print("也就是到", round(w, 2), "公斤")
elif 27 <= bmi < 30:
    print("你輕度肥胖，如果要變正常")
    print("你至少還需要減重", round(weight - w, 2), "公斤")
    print("也就是到", round(w, 2), "公斤")
elif 30 <= bmi < 35:
    print("你中度肥胖，如果要變正常")
    print("你至少還需要減重", round(weight - w, 2), "公斤")
    print("也就是到", round(w, 2), "公斤")
else:
    print("你重度肥胖，如果要變正常")
    print("你至少還需要減重", round(weight - w, 2), "公斤")
    print("也就是到", round(w, 2), "公斤")





