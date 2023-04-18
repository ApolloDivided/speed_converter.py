speed = float(input("Введите скорость: "))
unit = input("Введите единицу измерения (км/ч, м/с, миль/ч, футов/сек): ")

if unit == "км/ч":
    mps = speed / 3.6
    mph = speed / 1.609
    fps = speed / 1.097
    print("Скорость в м/с:", mps)
    print("Скорость в миль/ч:", mph)
    print("Скорость в футов/сек:", fps)
elif unit == "м/с":
    kph = speed * 3.6
    mph = kph / 1.609
    fps = kph / 1.097
    print("Скорость в км/ч:", kph)
    print("Скорость в миль/ч:", mph)
    print("Скорость в футов/сек:", fps)
elif unit == "миль/ч":
    kph = speed * 1.609
    mps = kph / 3.6
    fps = kph / 1.097
    print("Скорость в км/ч:", kph)
    print("Скорость в м/с:", mps)
    print("Скорость в футов/сек:", fps)
elif unit == "футов/сек":
    kph = speed * 1.097
    mps = kph / 3.6
    mph = kph / 1.609
    print("Скорость в км/ч:", kph)
    print("Скорость в м/с:", mps)
    print("Скорость в миль/ч:", mph)
else:
    print("Некорректная единица измерения.")
