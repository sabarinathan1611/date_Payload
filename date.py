from datetime import date, timedelta

def print_dates(start_year, end_year):
    start_date = date(start_year, 1, 1)
    end_date = date(end_year, 12, 31)

    current_date = start_date
    output = ""
    while current_date <= end_date:
        output += current_date.strftime("%d/%m/%Y") + "\n"
        current_date += timedelta(days=1)

    with open("years.txt", "w") as file:
        file.write(output)


start_year = int(input("Starting Year: "))

end_year = int(input("Ending Year: "))
if start_year <= end_year:
    print_dates(start_year, end_year)




