# Script calculate pension based on gross income.
# gross income = 7716.90 for september 2022 y
# after 16y 6m of service (43.9%)
# gross pension = 3669,6 = 47,55% of gross income
# net pension = 3199,34 = 87,18% of gross pension

# after 16y 6m of service + 15% (58.9%)
# gross pension = 4923,45 = 63,8% of gross income
# net pension = 4189,34 = 85,09% of gross pension

# gross_income = 7716.90
gross_income = float(input('What is Your gross income ->'))
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
print()
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
print()
print('Now You can assume % of valorization of Your gross pension...')
pension_val_percent = float(input('What would it be -> '))
gross_pension_val = round(gross_pension + (gross_pension * pension_val_percent / 100), 2)
net_pension_val = round(gross_pension_val * 0.8718, 2)
print('Your gross pension without extra 15% would be =', gross_pension_val, 'PLN')
print('And Your net pension would be =', net_pension_val, 'PLN')
print()
print('But if You will have 15% extra...')
gross_pension_15_val = round(gross_pension_15 + (gross_pension_15 * pension_val_percent / 100), 2)
net_pension_15_val = round(gross_pension_15_val * 0.8509, 2)
print('Your gross pension with extra 15% would be =', gross_pension_15_val, 'PLN')
print('And Your net pension would be =', net_pension_15_val, 'PLN')
print()
print(f'So, after valorization Your gross income is {round(gross_income_val, 2)}PLN and Your net pension after valorization of \
pension would be {net_pension_val}PLN, without extra 15%')
print(f'But if You retirement after 1 of march 2022 Your net_pension would be only {net_pension}PLN.')
print()
year_percent = 0.0021
new_net_pension = net_pension
while new_net_pension < net_pension_val:
    new_gross_pension = round(gross_income_val * (0.4755 + year_percent))
    new_net_pension = round(new_gross_pension * 0.8509, 2)
    year_percent += 0.0021
extra_month = round(year_percent / 0.00216667, 0)
print(f'To have pension at least {net_pension_val} You will have to serv for {extra_month} months more...')
extra_years = extra_month // 12
rest_month = extra_month % 12
print(f'And it would be {new_net_pension}PLN.')
print()
print(f'It is extra {extra_years} years and {rest_month} months...')
print(f'Is it worth of it ??')
