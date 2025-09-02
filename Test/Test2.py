def weather_suggestion(temp):
    if temp > 35:
        return"very hot, stay indoor"
    elif 25 <= temp <= 35:
        return"nice weather"
    elif 20 <= temp <= 24:
        return"quite cool"
    else:  #temp < 20
        return"cool,wear jacket"
    #ทดสอบฟังก์ชัน
    test_temps= [38,30,22,18]
    for t in test_temp:
        print(f" Temp{t} {weather_suggestion(t)}")