# Script calculate pension based on gross income.
# gross income = 7716.90 for september 2022 y
# after 16y 6m of service (43.9%)
# gross pension = 3669,6 = 47,55% of gross income
# net pension = 3199,34 = 87,18% of gross pension

# after 16y 6m of service + 15% (58.9%)
# gross pension = 4923,45 = 63,8% of gross income
# net pension = 4189,34 = 85,09% of gross pension

gross_income = 7716.90
# gross_income = float(input('What is Your gross income ->'))
gross_pension = round(gross_income * 0.4755, 2)
net_pension = round(gross_pension * 0.8718, 2)
print('Your gross pension without extra 15% would be =', gross_pension, 'PLN')
print('And Your net pension would be =', net_pension, 'PLN')
print()
print('But if You will have 15% extra...')
gross_pension_15 = round(gross_income * 0.638, 2)
net_pension_15 = round(gross_pension_15 * 0.8509, 2)
print('Your gross pension with extra 15% would be =', gross_pension_15, 'PLN')
print('And Your net pension would be =', net_pension_15, 'PLN')

print('Now You can assume % of valorization of Your gross income...')
val_percent = float(input('What would it be -> '))
gross_income_val = gross_income + (gross_income * val_percent / 100)
gross_pension = round(gross_income_val * 0.4755, 2)
net_pension = round(gross_pension * 0.8718, 2)
print('Your gross pension without extra 15% would be =', gross_pension, 'PLN')
print('And Your net pension would be =', net_pension, 'PLN')
print()
print('But if You will have 15% extra...')
gross_pension_15 = round(gross_income_val * 0.638, 2)
net_pension_15 = round(gross_pension_15 * 0.8509, 2)
print('Your gross pension with extra 15% would be =', gross_pension_15, 'PLN')
print('And Your net pension would be =', net_pension_15, 'PLN')
print('Now You can assume % of valorization of Your gross pension...')

pension_val_percent = float(input('What would it be -> '))
gross_pension = round(gross_pension + (gross_pension * pension_val_percent / 100), 2)
net_pension = round(gross_pension * 0.8718, 2)
print('Your gross pension without extra 15% would be =', gross_pension, 'PLN')
print('And Your net pension would be =', net_pension, 'PLN')
print()
print('But if You will have 15% extra...')
gross_pension_15 = round(gross_pension_15 + (gross_pension_15 * pension_val_percent / 100), 2)
net_pension_15 = round(gross_pension_15 * 0.8509, 2)
print('Your gross pension with extra 15% would be =', gross_pension_15, 'PLN')
print('And Your net pension would be =', net_pension_15, 'PLN')
