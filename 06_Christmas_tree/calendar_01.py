# Print a calendar for each month.
# Start from the function which prints days of 1 month.
# Repeat it for every month. Remember, week has 7 days.
def print_month(month, days):
    print('\n', month)

    for day in days:
        day += 1
        if day < 10:
            day = '0' + str(day)
        if int(day) % 7 == 0:
            print(day)
        else:
            print(day, end=' ')


def main():
    data = [
        ('January', range(31)),
        ('February', range(28)),
        ('March', range(31)),
        ('April', range(30)),
        ('May', range(31)),
        ('June', range(30)),
        ('July', range(31)),
        ('August', range(31)),
        ('September', range(30)),
        ('October', range(31)),
        ('November', range(30)),
        ('December', range(31)),
          ]

    data = dict(data)
    for name, days in data.items():
        print_month(name, days)


main()
