# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def withCutOff(total, possible):
    denominator = int(possible * 0.75)
    percent = total/denominator
    if percent > 1:
        percent=1.0
    return percent

if __name__ == '__main__':
    total = 75
    possible = 100
    print(withCutOff(total, possible))