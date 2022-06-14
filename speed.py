class Speed():
    def __init__(self, selectedSpeed):
        self.selection = {
            "fast" : 0.1,
            "medium" : 0.2,
            "low" : 0.3,
            "max" : 0.03
        }

        self.localSpeed = self.selection[selectedSpeed]
        self.speed = self.localSpeed
        self.calibrationFast = 0.01
        self.calibrationMedium = 0.02
        self.calibrationLow = 0.03

    
    def calibrate(self, flag):
        if self.speed == 0.1:
            self.localSpeed -= self.calibrationFast
            flag = True

        elif self.speed == 0.2:
            self.localSpeed -= self.calibrationMedium
            flag = True
        
        elif self.speed == 0.3:
            self.localSpeed -= self.calibrationLow
            flag = True
        
        return flag

    def checkMaxSpeed(self):
        if self.selection["max"] >= self.localSpeed:
            self.localSpeed = self.selection["max"]
            return True
        else:
            return False