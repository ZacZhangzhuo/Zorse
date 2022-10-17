__author__ = ["Zac Zhuo Zhang"]
__copyright__ = "Copyright 2022"
__license__ = "MIT License"
__email__ = ["<Arch.Z@outlook.com>"]



class zVector:
    """A vector object constructed by X, Y and Z"""
    def __init__(self, x=0, y=0, z=0):
        self.X = x
        self.Y = y
        self.Z = z


def Remap(numberToBeMapped, min0, max0, min1, max1):
    """Map a number from domain (min0, max0) into (min1, max1)"""
    return (numberToBeMapped - min0) / (max0 - min0) * (max1 - min1) + min1