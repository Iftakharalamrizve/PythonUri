salary = float(input())

if(salary > 4500.00):
    taxes = ((salary - 4500.00) * 0.28) + 350.00
    print('R$ %.2f' %taxes)

if(salary > 3000.00 and salary <= 4500.00):
    taxes = ((salary - 3000.00) * 0.18) + 80.00
    print('R$ %.2f' %taxes)

if(salary > 2000.00 and salary <= 3000.00):
    taxes = ((salary - 2000.00) * 0.08)
    print('R$ %.2f' %taxes)
    
if(salary <= 2000.00):
    print('Isento')