from datetime import datetime

class VitalSign:
    def __init__(self, heart_rate, blood_pressure, oxygen):
        self.timestamp = datetime.now().strftime("%H:%M:%S")
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.oxygen = oxygen

    def get_health_status(self):
        """Calcula el estado y color de alerta según los signos."""
        if self.heart_rate > 100 or self.oxygen < 90:
            return "Crítico", "#FF4B4B" # Rojo
        if self.heart_rate > 90 or self.oxygen < 94:
            return "Riesgo", "#FFA500"  # Naranja
        return "Estable", "#28A745"      # Verde