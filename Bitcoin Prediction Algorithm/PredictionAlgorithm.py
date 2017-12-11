# Takes a sqlite3 database with fields timestamp (unix time) and weighted_price at timestamp for Bitcoin
# Predicts price per day for an provided number of days

import sqlite3
import datetime

numDaysPredictionBasis = 7*14  # The number of days historical data upon which to base our predictions

# Take in user input (how many days to predict)
print("\n\tInput the number of day's predictions you want to make:", end="\n\t")
while 1:
    try:
        numDaysPredict = int(input())  # How many days worth of prices to predict
        if numDaysPredict < 1:
            print("\n\tInvalid entry. Try again:", end='\n\t')
            continue
        print()
        break
    except ValueError:
        print("\n\tNot a number. Try again:", end='\n\t')

# Open the database and set up a means to execute commands on it
db = sqlite3.connect("mydb.db")
exc = db.cursor()

# Find last data point
exc.execute("SELECT timestamp, weighted_price FROM data ORDER BY timestamp DESC LIMIT 1")
initialValues = exc.fetchone()
initDate = datetime.datetime.fromtimestamp(initialValues[0]).strftime('%Y-%m-%d %H:%M')
initWeekday = datetime.datetime.fromtimestamp(initialValues[0]).strftime('%a')
startNote = "\tThe starting value (from " + initWeekday + " " + initDate + ") is $" + str(round(initialValues[1], 2))

# Grab data and count data points
earliestPoint = (initialValues[0]-(numDaysPredictionBasis*24*60*60), )
exc.execute('select COUNT(*) from data where timestamp > ? and timestamp % 86400 = 0', earliestPoint)
numEntries = exc.fetchone()[0]
print("\tThere are " + str(numEntries) + " data points.")

# Retrieve data points for each day
exc.execute("SELECT timestamp, weighted_price FROM data WHERE timestamp > ? and timestamp % 86400 = 0", earliestPoint)

# Declare variables to store average growths, both daily (deprecated) and per-weekday, and also the previous day's value
previous = 0
count = 0
dayGrowth = [0, 0, 0, 0, 0, 0, 0]
dayCount = [0, 0, 0, 0, 0, 0, 0]

# Check daily values and store relevant deltas
for val in exc.fetchmany(numEntries):
    if count == 0:
        count += 1
        previous = val[1]
        continue
    count += 1
    dayNum = int(datetime.datetime.fromtimestamp(val[0]).strftime('%w'))
    dayCount[dayNum] += 1
    dayGrowth[dayNum] += val[1] / previous
    previous = val[1]

# Calculate average per-weekday growth
for i in range(0, len(dayGrowth)):
    if dayCount[i] != 0:
        dayGrowth[i] = dayGrowth[i]/dayCount[i]

lastDay = initialValues[1]
print("\n" + startNote + "\n")
for i in range(numDaysPredict):
    # Calculate and print day-by-day answers
    date = datetime.datetime.fromtimestamp(initialValues[0]+((i+1)*86400)).strftime('%Y-%m-%d %H:%M')
    dayNum = int(datetime.datetime.fromtimestamp(initialValues[0] + ((i + 1) * 86400)).strftime('%w'))
    weekday = datetime.datetime.fromtimestamp(initialValues[0] + ((i + 1) * 86400)).strftime('%a')
    lastDay = lastDay * dayGrowth[dayNum]
    print("\tDay " + str(i + 1) + ":\t" + weekday + " " + date + "\t" + str(round(lastDay, 2)))

print()
db.close()
