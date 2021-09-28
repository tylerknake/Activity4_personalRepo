# Tyler Knake
# ISQA 3900 - 9/26/2021
# Program 4b - Asks the user for multiple integers between 0 and 100 (grade scores) as input, storing them in a list.
# When input is quit (inputting -1) the list is presented along with the total, the average, and the letter grade.

# Requests the input of grades between 0 and 100, storing them in a list. Entering -1 ends the loop and finalizes
# the list. Includes exception handling.
def inputGrades():
    global gradeList
    gradeList = []
    while True:
        try:
            score = int(input("Enter test score (-1 to quit): "))
            if (score < 0 or score > 100 or score == str) and score != -1:
                raise ValueError()
        except ValueError:
            print("You must enter integer values >= 0 and <= 100 or -1 to quit. Try again.")
            continue
        else:
            if 0 <= score <= 100:
                gradeList.append(score)
            elif score == -1:
                return gradeList

# Takes a list of grades and adds them, returning the sum.
def summedGrades(list):
    global gradeSum
    gradeSum = 0
    for x in list:
        gradeSum += x
    return gradeSum

# Takes a list of grades and the sum of those grades and returns the average grade
def gradeAverage(list, total):
    global averageGrade
    averageGrade = 0
    count = 0
    for x in list:
        count = count + 1
    averageGrade = total / count
    return averageGrade

# Takes the average score and returns the letter grade
def letterGrade(average):
    global letter
    letter = 'none'
    if average >= 92.5:
        letter = 'A'
    elif average >= 88.5:
        letter = 'B+'
    elif average >= 82.5:
        letter = 'B'
    elif average >= 77.5:
        letter = 'C+'
    elif average >= 72.5:
        letter = 'C'
    elif average >= 59.5:
        letter = 'D'
    else:
        letter = 'F'
    return letter


# Runs all Program functions and prints their results.
def main():
    inputGrades()
    print()
    print("Scores: \t\t\t" + str(gradeList))
    summedGrades(gradeList)
    print("Total: \t\t\t\t" + str(gradeSum))
    gradeAverage(gradeList, gradeSum)
    print("Average Score: \t\t" + str(averageGrade))
    letterGrade(averageGrade)
    print("Letter Grade: \t\t" + letter)

# Run Main
main()


