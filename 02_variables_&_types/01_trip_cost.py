fule_usage = float(6.4)
trip_distance = float(120)
petrol_price = float(5.04)
trip_cost = (fule_usage * (trip_distance / 100)) * petrol_price
print('The trip will cost You', round(trip_cost, 2), 'zł.')
