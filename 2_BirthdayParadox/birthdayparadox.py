"""
The Birthday Paradox, also called the 
Birthday Problem, is the surprisingly high 
probability that two people will have the 
same birthday even in a small group of people. 
In a group of 70 people, there's a 99.9 percent chance 
of two people having a matching birthday. But even 
in a group as small as 23 people, there's a 50 percent 
chance of a matching birthday. This program performs several probability experiments to determine 
the percentages for groups of different sizes. We call these types of experiments, in which we conduct multiple random trials to understand the 
likely outcomes, Monte Carlo experiments.
You can find out more about the Birthday Paradox at https://en.wikipedia.org/wiki/Birthday_problem.
"""


import random
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


def generateBirthdays(gen_count: int) -> list:
    def helperGen() -> list[dt.date]:
        lst = []
        start_date = dt.date(1999, 1, 1)
        for _ in range(gen_count):
            lst.append(start_date +  dt.timedelta(random.randint(0, 364)))
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