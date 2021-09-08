import sys

def sodaslurper(lines):
    # Deler tall inn i variabler ved å splitte på space og hente hvert tall som en int

    # start,found,cost = [int(x) for x in lines[0].split()]

    nums = lines[0].split()
    start = int(nums[0])
    found = int(nums[1])
    cost = int(nums[2])

    # Det har ingenting å si om man starter med bottles eller om man finner de i løpet av
    # dagen, summen er totalen flasker du har ved start uansett
    current = start + found

    bought = 0
    while (current >= cost):
        # Trekker fra antall tomflasker for å kjøpe en ny flaske
        current -= cost

        # Vi kjøper en flaske
        bought += 1

        # Drikker flasken og får en ny tomflaske
        current += 1

    return bought


def main():
    lines = [line.strip() for line in sys.stdin]
    print(sodaslurper(lines))
main()
