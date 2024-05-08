"""
This program generates printable text 
files of monthly calendars for the month 
and year you enter. Dates and calendars are 
a tricky topic in programming because there 
are so many different rules for determining the number
of days in a month, which years are leap years, 
and which day of the week a particular date falls on. 
Fortunately, Python’s datetime module handles these 
details for you. This program focuses on generating 
the multiline string for the monthly calendar page.
"""

from datetime import datetime, timedelta
from queue import Queue
import calendar
import os


class CalendarMaker:
    def __init__(self, year: int, month: int) -> None:
        self.year = year
        self.month = month
        self.dates = self.__getMonthDates()

    def __getMonthDates(self):
        num_days = calendar.monthrange(self.year, self.month)[1]
        start_date = datetime(self.year, self.month, 1)
        dates = [start_date + timedelta(days=i) for i in range(num_days)]
        return dates
    
    def __saveCalendar(self, cal: str) -> None:
        folder = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(folder, f"calendar_{self.year}_{self.month}.txt")
        with open(filename, "w") as f:
            f.write(cal)
            print(f"\nSaved calendar to {filename}")

    def __formatDates(self) -> list[list[int]]:
        formatted = []
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        firstDateIdx = days.index(self.dates[0].strftime("%A"))
        q = []
        for _ in range(firstDateIdx):
            q.append("  ")
        while self.dates:
            d = self.dates.pop(0).day
            if len(q) < 7:
                q.append(d if len(str(d)) == 2 else f" {d}")
            else:
                formatted.append(q)
                q = []
        if len(q) < 7:
            while len(q) < 7:
                q.append("  ")
            formatted.append(q)
        return formatted

    def drawCalendar(self):
        cal_str = """                                  {} {}
...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..""".format(self.dates[0].strftime("%b"), self.month)
        formatted = self.__formatDates()
        for i in range(len(formatted)):
            cal_str += "\n+----------+----------+----------+----------+----------+----------+----------+"
            cal_str += f"\n|{formatted[i].pop(0)}        |{formatted[i].pop(0)}        |{formatted[i].pop(0)}        "
            cal_str += f"|{formatted[i].pop(0)}        |{formatted[i].pop(0)}        |{formatted[i].pop(0)}        |{formatted[i].pop(0)}        |"
            for _ in range(0, 3):
                cal_str += "\n|          |          |          |          |          |          |          |"
        cal_str += "\n+----------+----------+----------+----------+----------+----------+----------+"
        print(cal_str)
        self.__saveCalendar(cal_str)


def validInput(startRange: int=None, endRange: int=None) -> int:
    try:
        user_input = int(input("> "))
        if startRange is not None and endRange is not None:
            if user_input < startRange or user_input > endRange:
                print(f"Please input a valid number from {startRange} to {endRange}.")
                return validInput(startRange, endRange)
        return user_input
    except:
        print("Please input a valid number.")
        return validInput(startRange, endRange)


if __name__ == "__main__":
    print("Enter the year for the calendar:")
    yearInput = validInput()
    print("Enter the month for the calendar, 1-12")
    monthInput = validInput(1, 12)

    calendarmaker = CalendarMaker(yearInput, monthInput)
    calendarmaker.drawCalendar()