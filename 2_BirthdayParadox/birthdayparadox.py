import random
import calendar
import datetime as dt


MONTHS = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}


def printDates(dates: list[dt.date]) -> None:
    print(", ".join([f"{MONTHS[d.month]} {d.day}" for d in dates]))


# https://stackoverflow.com/questions/45833559/generate-random-date-in-a-particular-month-and-year#:~:text=In%20short%2C%20use%20calendar%20lib%3A%20import%20calendar%2C%20random,month%5D%29%20This%20function%20will%20return%20a%20datetime.date%20object.
def randomDate(year: int, month: int) -> dt.date:
    d = calendar.Calendar().itermonthdates(year, month)
    return random.choice([date for date in d if date.month == month])


def commonBirthday(dates: list[dt.date]) -> dt.date:
    return max(set(dates), key=dates.count)


def generateBirthdays(gen_count: int) -> list:
    def helperGen() -> list[dt.date]:
        lst = []
        for _ in range(gen_count):
            lst.append(randomDate(1999, random.randint(1, 12)))
        return lst

    bday_list = helperGen()
    print(f"\nHere are the {gen_count} birthdays:")
    printDates(bday_list)

    common = max(set(bday_list), key=bday_list.count)
    if bday_list.count(common) > 1:
        print("In this simulation, multiple people have a birthday on: ", end="")
        printDates([common])
    else: 
        print("Sadly there are no shared birthdays on this simulation.")

    count = 0
    print("\nLet's run another 100,000 simulations.")
    for i in range(100001):
        if i % 10000 == 0:
            print(f"{i} simulations...")
        new_bday_list = helperGen()
        for d in new_bday_list:
            if new_bday_list.count(d) > 1:
                count += 1
                break

    percentage = float("{:.2f}".format((count / 100000) * 100))
    print(f"""\nOut of 100,000 simulations of {gen_count} people, there was a
matching birthday in that group {count} times. This means
that {gen_count} people have a {percentage}% chance of having
a matching birthday in their group.
          """)
    if percentage > 50:
        print("That's more than you would think!")


def getUserInput() -> int:
    print("How many birthdays shall I generate? (Range 2-100)")
    validInput = False
    while not validInput:
        try:
            user_input = input("> ")
            user_input = int(user_input)
            if user_input > 1 and user_input <= 100:
                validInput = True
            else:
                raise Exception()
        except:
            print("Please enter a valid number from 2 to 100.")
    return user_input


if __name__ == "__main__":
    user_input = getUserInput()
    generateBirthdays(user_input)