def month_to_season(n): 
   if n in [12,1,2]:
      return "Зима"
   elif n in [3,4,5]:
      return "Весна"
   elif n in [6,7,8]:
      return "Лето"
   elif n in [9,10,11]:
      return "Осень"

n=int(input("Введите номер месяца(1-12):"))
print(month_to_season(n))
