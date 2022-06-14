class Speed():
    def __init__(self, selectedSpeed):
        self.selection = {
            "fast" : 0.1,
            "medium" : 0.2,
            "low" : 0.3
        }

        self.localSpeed = self.selection[selectedSpeed]
        self.speed = self.localSpeed
        self.calibrationFast = 0.01
        self.calibrationMedium = 0.02
        self.calibrationLow = 0.03

    
    def calibrate(self, flag):
        pass # dummy implementation

    