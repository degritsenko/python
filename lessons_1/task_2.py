seconds = int(input("Input seconds "))
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds / 60
seconds = seconds % 60

#тут подсказали, сам добавить ноль не шмогла
print(f"{hours:02.0f}:{minutes:02.0f}:{seconds:02.0f}")