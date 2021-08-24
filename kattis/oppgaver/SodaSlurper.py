import sys

def sodaslurper(lines):
    # Deler tall inn i variabler ved å splitte på space og hente hvert tall som en int
    nums = [int(x) for x in lines[0].split(" ")]
    start = nums[0]
    found = nums[1]
    cost = nums[2]

    # 
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