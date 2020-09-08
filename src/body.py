class Body:
    def __init__(self, name, bodyparts):
        self.name = name
        self.parts = bodyparts


class BodyPart:
    def __init__(self, name, partType, size, canWear, canWield):
        self.name = name
        self.partType = partType
        self.size = size
        self.canWear = canWear
        self.canWield = canWield


def movezeroes(nums):

    for i in range(len(nums)):
        if nums[i] == 0:

            zeroes += 1

    for i, num in enumerate(nums):
