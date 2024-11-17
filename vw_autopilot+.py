import random

class InCarAI:
    def __init__(self):
        self.sensors = {
            "heart_rate": random.randint(60, 100),
            "stress_level": random.uniform(0, 1),
            "oxygen_level": random.uniform(90, 100),
            "mood": random.choice(["happy", "sad", "stressed", "calm"]),
            "temperature": random.randint(15, 35),
            "noise_level": random.randint(30, 80),
        }
        self.emergency = False

    def detect_presence(self):
        print("Detecting presence in the car...")
        return True

    def adjust_environment(self):
        print("\nAdjusting environment based on sensor data...")
        self.adjust_temperature()
        self.adjust_lighting()
        self.adjust_music()
        self.adjust_seating()

    def adjust_temperature(self):
        temp = self.sensors["temperature"]
        if temp < 18:
            print("Temperature is too cold. Increasing heat.")
        elif temp > 28:
            print("Temperature is too warm. Increasing air conditioning.")
        else:
            print("Temperature is optimal.")

    def adjust_lighting(self):
        mood = self.sensors["mood"]
        if mood == "happy":
            print("Setting lighting to bright and warm tones.")
        elif mood == "sad":
            print("Setting lighting to soft and calming tones.")
        elif mood == "stressed":
            print("Setting lighting to cool and relaxing tones.")
        elif mood == "calm":
            print("Setting lighting to neutral tones.")
    
    def adjust_music(self):
        mood = self.sensors["mood"]
        if mood == "happy":
            print("Playing upbeat music.")
        elif mood == "sad":
            print("Playing soothing music.")
        elif mood == "stressed":
            print("Playing instrumental music.")
        elif mood == "calm":
            print("Playing nature sounds.")
        # Additional music suggestions based on health conditions
        heart_rate = self.sensors["heart_rate"]
        if heart_rate > 100:
            print("Heart rate elevated. Playing calming instrumental music to help lower it.")
        elif self.sensors["stress_level"] > 0.7:
            print("Stress level high. Playing relaxing sounds to reduce stress.")

    def adjust_seating(self):
        heart_rate = self.sensors["heart_rate"]
        mood = self.sensors["mood"]
        temp = self.sensors["temperature"]

        if heart_rate > 90 or self.sensors["stress_level"] > 0.7:
            print("Reclining seat slightly for stress relief.")
        elif mood == "happy":
            print("Adjusting seat for a more upright position for energy.")
        elif temp < 18:
            print("Adjusting seat to a warmer posture setting.")
        elif temp > 28:
            print("Cooling seat activated for better comfort.")
        else:
            print("Seat position remains neutral.")

    def monitor_health(self):
        print("\nMonitoring health...")
        if self.sensors["heart_rate"] > 100 or self.sensors["oxygen_level"] < 92:
            print("Emergency detected! Heart rate or oxygen level is critical.")
            self.trigger_sos()
        else:
            print("Health readings are normal.")
            self.suggest_health_exercises()

    def trigger_sos(self):
        self.emergency = True
        print("SOS triggered! Connecting to a medical professional...")
        # Simulate connecting to emergency services
        print("Doctor connected. Emergency services on the way!")

    def suggest_health_exercises(self):
        heart_rate = self.sensors["heart_rate"]
        oxygen_level = self.sensors["oxygen_level"]
        stress_level = self.sensors["stress_level"]

        if heart_rate > 100:
            print("Suggesting deep breathing exercises to calm the heart rate.")
        elif oxygen_level < 92:
            print("Suggesting deep breathing exercises to increase oxygen levels.")
        elif stress_level > 0.7:
            print("Suggesting guided meditation to reduce stress.")
        else:
            print("No immediate health concerns. Enjoy the ride comfortably!")

    def simulate(self):
        if self.detect_presence():
            self.monitor_health()
            self.adjust_environment()

# Main execution
if __name__ == "__main__":
    car_ai = InCarAI()
    car_ai.simulate()
