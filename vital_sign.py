from datetime import datetime

class VitalSign:
    def __init__(self, heart_rate, blood_pressure, oxygen):
        self.timestamp = datetime.now().strftime("%H:%M:%S")
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.oxygen = oxygen

    def __str__(self):
        return f"[{self.timestamp}] FC: {self.heart_rate} bpm | PA: {self.blood_pressure} | SpO2: {self.oxygen}%"