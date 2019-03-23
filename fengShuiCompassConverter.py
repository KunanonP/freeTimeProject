import datetime
from datetime import date
from datetime import timedelta

class compassConverter:
    def __init__(self, direction):

        self.direction = direction
        self.result = 0
        self.compassDirection = ""
        self.zodiac = ""

    def degree(self):
        degree = self.direction
        result = 0

        if (degree >= 0) and (degree <= 180):
            result = 180 - degree
        elif (degree > 180) and (degree <= 270):
            result = 360 - (degree - 180)
        elif (degree > 270) and (degree < 360):
            result = (360 - degree) + 180
        self.result = str(result)

        return self.result

    def myDirection(self):
        result = int(self.result)

        if (result > 330) and (result < 360) or (result < 30):
            compassDirection = "South"
        elif (result >= 30) and (result <= 60):
            compassDirection = "South East"
        elif (result > 60) and result < 120:
            compassDirection = "East"
        elif (result >= 120) and (result <= 150):
            compassDirection = "North East"
        elif (result > 150) and (result < 210):
            compassDirection = "North"
        elif (result >= 210) and (result <= 240):
            compassDirection = "North West"
        elif (result > 240) and (result < 300):
            compassDirection = "West"
        elif (result >= 300) and (result <= 330):
            compassDirection = "South West"
        else:
            compassDirection = "error"
        self.compassDirection = compassDirection

        return self.compassDirection

    def myZodiac(self):
        myDegree = int(self.result)

        if (myDegree > 345) and (myDegree < 360) or (myDegree < 15) and (myDegree > 0):
            zodiac = "Rat"
        elif (myDegree > 15) and (myDegree < 45):
            zodiac = "Cow"
        elif (myDegree > 45) and (myDegree < 75):
            zodiac = "Tiger"
        elif (myDegree > 75) and (myDegree < 105):
            zodiac = "Rabbit"
        elif (myDegree > 105) and (myDegree < 135):
            zodiac = "Dragon"
        elif (myDegree > 135) and (myDegree < 165):
            zodiac = "Snake"
        elif (myDegree > 165) and (myDegree < 195):
            zodiac = "Horse"
        elif (myDegree > 196) and (myDegree < 225):
            zodiac = "Goat"
        elif (myDegree > 225) and (myDegree < 255):
            zodiac = "Monkey"
        elif (myDegree > 255) and (myDegree < 285):
            zodiac = "Rooster"
        elif (myDegree > 285) and (myDegree < 315):
            zodiac = "Dog"
        elif (myDegree > 315) and (myDegree < 345):
            zodiac = "Pig"
        else:
            zodiac = "error"
        self.zodiac = zodiac

        return self.zodiac


def fourPillarCalculator(min,h,d, m, y):

    inputMin = min
    inputHour = h
    inputDate = d
    inputMonth = m
    inputYear = y

    element = ["+Wood", "-Wood", "+Fire", "-Fire", "+Earth", "-Earth", "+Metal", "-Metal", "+Water", "-Water"]
    zodiac = ["-Rat", "-Cow", "+Tiger", "-Rabbit", "+Dragon", "+Snake", "-Horse", "-Goat", "+Monkey", "-Rooster", "+Dog", "+Pig"]

    # Base year 1900
    baseCalendar = datetime.datetime(1900, 12, 22, 01)
    dateInput = datetime.datetime(inputYear, inputMonth, inputDate, inputHour, inputMin)
    print(dateInput)

    # Day calculation
    baseElementD = element.index("-Earth")
    baseZodiacD = zodiac.index("+Snake")
    if inputDate > 0 and inputDate <= 31:
        if dateInput > baseCalendar:
            resultDay = dateInput - baseCalendar
        elif dateInput < baseCalendar:
            resultDay = baseCalendar - dateInput
        else:
            resultDay = baseCalendar - dateInput
        newHour = (resultDay.seconds)/3600
        newDay = (resultDay.days) * 24
        diff = (newHour + newDay)/2
        resultDay = resultDay.days

        for i in range(0, resultDay):
            baseElementD = baseElementD + 1
            if baseElementD == 10:
                baseElementD = 0
        resultDayE = element[baseElementD]

        for j in range(0, resultDay):
            baseZodiacD = baseZodiacD + 1
            if baseZodiacD == 12:
                baseZodiacD = 0
        resultDayZ = zodiac[baseZodiacD]

    # Hour calculation
    baseElementH = element.index("-Wood")
    baseZodiacH = zodiac.index("-Cow")
    dayToHour = diff
    for i in range(0, dayToHour):
        baseElementH = baseElementH + 1
        if baseElementH == 10:
            baseElementH = 0
    resultHourE = element[baseElementH]
    for j in range(0, dayToHour):
        baseZodiacH = baseZodiacH + 1
        if baseZodiacH == 12:
            baseZodiacH = 0
    resultHourZ = zodiac[baseZodiacH]

    # Month calculation
    baseElementM = element.index("+Earth")
    baseZodiacM = zodiac.index("-Rat")

    # calculate different months
    diffMonth = (dateInput.year - baseCalendar.year) * 12 + dateInput.month - baseCalendar.month
    for i in range(0, diffMonth):
        baseElementM = baseElementM + 1
        if baseElementM == 10:
            baseElementM = 0
    resultMonthE = element[baseElementM]

    for j in range(0, diffMonth):
        baseZodiacM = baseZodiacM + 1
        if baseZodiacM == 12:
            baseZodiacM = 0
    resultMonthZ = zodiac[baseZodiacM]

    # Year calculation
    baseElementY = element.index("+Metal")
    baseZodiacY = zodiac.index("-Rat")
    if inputYear > 0:
        if inputYear >= baseCalendar.year:
            if inputMonth < 12:
                resultYear = inputYear - baseCalendar.year
            elif inputMonth == 12 and inputDate >= 22:
                resultYear = inputYear - baseCalendar.year + 1

            for i in range(0,resultYear):
                baseElementY = baseElementY + 1
                if baseElementY == 10:
                    baseElementY = 0
            resultYearE = element[baseElementY]

            for j in range(0, resultYear):
                baseZodiacY = baseZodiacY + 1
                if baseZodiacY == 12:
                    baseZodiacY = 0
            resultYearZ = zodiac[baseZodiacY]

        elif inputYear < baseCalendar.year:
            if baseCalendar.month < 12:
                resultYear = baseCalendar.year - inputYear
            elif baseCalendar.month == 12 and baseCalendar.day >= 22:
                resultYear = baseCalendar.year - inputYear - 1
                print(resultYear)

            for i in range(0, resultYear):
                baseElementY = baseElementY - 1
                if baseElementY < 0:
                    baseElementY = 9
            resultYearE = element[baseElementY]

            for j in range(0, resultYear):
                baseZodiacY = baseZodiacY - 1
                if baseZodiacY  < 0:
                    baseZodiacY = 11
            resultYearZ = zodiac[baseZodiacY]
    result = resultHourE,resultHourZ,resultDayE,resultDayZ,resultMonthE,resultMonthZ,resultYearE,resultYearZ

    return "Hour Element: %s Zodiac: %s\n Day Element: %s Zodiac: %s\n Month Element: %s Zodiac: %s\n Year Element: %s Zodiac: %s" % \
           (result)



# converter = compassConverter(127)
# newDegree = converter.degree()
# newDirection = converter.myDirection()
# newZodiac = converter.myZodiac()
# print(newDegree + "\n" + newDirection + "\n" + newZodiac)

# calculator



x = datetime.datetime.now()
d = x.day
m = x.month
y = x.year

z = datetime.datetime(1900, 12, 22)
zx = datetime.datetime(1900, 12, 23)

print(fourPillarCalculator(59,18,07, 06, 1992))


# print(x.year)
# print(x.strftime("%A"))
