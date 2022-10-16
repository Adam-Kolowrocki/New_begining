# Print a calendar for each month.
# Start from the function which prints days of 1 month.
# Repeat it for every month. Remember, week has 7 days.
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


def print_month():
    print(data[0])


print_month()
