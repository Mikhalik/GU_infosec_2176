# 5) Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма. 
#    Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
earn = int(input("Какая у Вас выручка за сегодня: "))
cost = int(input("Какие у Вас сегодня затраты: "))
profit = 0
if earn > cost:
    profit = earn - cost
    print(f'Вы молодец, прибыль: {profit} руб')
elif earn < cost:
    profit =  cost - earn
    print(f'Батенька, да Вы банкрот, убыток: {profit} руб')
else:
    print ('По нулям')
