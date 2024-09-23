# decision making and flow control
def check_tempreture(temp):
    if temp > 25:
        return "It's too hot!"
    elif temp < 18:
        return "It's too cold!"
    else:
        return "It's just right!"
    
result: str = check_tempreture(28)
print(result)

print(type(result))