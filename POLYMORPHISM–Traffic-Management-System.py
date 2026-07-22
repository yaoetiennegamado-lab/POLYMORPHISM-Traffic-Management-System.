class TrafficDevice:
    def activate(self):
        print('Activating traffic devices')

class TrafficLight(TrafficDevice):
    def activate(self):
        print('TrafficLight: Redlight, CARS STOP')
        
class SpeedCamera(TrafficDevice):
    def activate(self):
        print('SpeedCamera: Recording vehicle speed and capturing license plates')
        
class PedestrianSignal(TrafficDevice):
    def activate(self):
        print('Pedestrian signal: People can cross the road safely')

class EmergencySiren(TrafficDevice):
    def activate(self):
        print('Emergency siren: High pitch sound')

traffic_light = TrafficLight()
speed_camera = SpeedCamera()
pedestrian_signal = PedestrianSignal()

objs = [traffic_light, speed_camera, pedestrian_signal]

for obj in objs:
    obj.activate()

