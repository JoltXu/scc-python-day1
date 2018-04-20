#test1 BMI   A 身高 175cm, 体重 80 kg。计算 A 的 BMI 指数，并根据 BMI 指数： < 18.5: 过轻，18.5-25: 正常，25-28：过重，28-32：肥胖，> 32：严重肥胖。
H = float(input("Please enter the height: "))
W = float(input("Please enter the weight: "))
BMI = W/((H/100)**2)
if BMI<0:
    print("Error")
elif BMI< 18.5:
    print("too light")
elif BMI<25:
    print("Normal")
elif BMI<28:
    print("a bit heavy")
elif BMI<32:
    print("obesity")
else:
    print("Severe obesity")
