# Steps:
# 1. Get current Date
# 2. Determine all dates in a weekspan.
# 3. Call MyFitnessPal for all

from enum import Enum
import datetime as DT
import myfitnesspal

client = myfitnesspal.Client('', '')

# Input: Date object
# Output: Year
def getYear(date): 
    return date.year

# Input: Date object
# Output: Month
def getMonth(date): 
    return date.month

# Input: Date object
# Output: Day
def getDay(date):
    return date.day

# Input: Date object
# Output: MFP Day Object
def dayFromMFP(date):
    year = getYear(date)
    month = getMonth(date)
    day = getDay(date)
    return client.get_date(year, month, day)

# https://stackoverflow.com/questions/20573459/getting-the-date-of-7-days-ago-from-current-date-in-python
for x in range(8, 0, -1):
    today = DT.date.today()
    aDate = today - DT.timedelta(days=x)
    mfpDay = dayFromMFP(aDate)
    print(mfpDay.totals)
    print("Protein" + format(mfpDay.totals['protein']))
    print(mfpDay.goals)
