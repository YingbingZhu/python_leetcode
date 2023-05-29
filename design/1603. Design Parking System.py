class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.small_slots = small
        self.medium_slots = medium
        self.big_slots = big
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1 and self.big_slots > 0:
            self.big_slots -= 1
            return True
        elif carType == 2 and self.medium_slots > 0:
            self.medium_slots -= 1
            return True
        elif carType == 3 and self.small_slots > 0:
            self.small_slots -= 1
            return True   
        return False   



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)