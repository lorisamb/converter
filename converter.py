# 18.5 degrees Celsius are 65.3 degrees Farenheit

def temp_converter(celsius):
    msg_1 = " degrees Celsius are "
    msg_2 = " degrees Farenheit "
    result = (celsius * 9/5) + 32
    return str(celsius) + msg_1 + str(result) + msg_2

user_input = input("Enter a temperature in degrees Celsius: ")
farenheit_result = temp_converter(float(user_input))

print(farenheit_result)

if (float(user_input) * 9/5  + 32) > 38:
    print("It's really hot")
