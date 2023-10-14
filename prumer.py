import sys


def prumer(nums: list) -> float:
    return sum(nums)/len(nums)


if __name__ == "__main__":
    print(prumer(nums=[float(i) for i in sys.argv[1:]]))
