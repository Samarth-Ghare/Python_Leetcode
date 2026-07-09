class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.availableSpots = [0,big,medium,small]

    def addCar(self, carType: int) -> bool:
        if self.availableSpots[carType] > 0: 
            self.availableSpots[carType] -=1
            return True 
        else: 
            return False
    

