print('Trip cost calculator.')
print()
print('Use only numbers and "." if necessary... ')
fule_usage = float(input('How much petrol/oil those Your car use for 100km? ->'))
trip_distance = float(input('How far the trip will be in "km"? ->'))
petrol_price = float(input('What is the cost of 1L of fuel? ->'))
trip_cost = (fule_usage * (trip_distance / 100)) * petrol_price
print('The trip will cost You', round(trip_cost, 2), 'zł.')
