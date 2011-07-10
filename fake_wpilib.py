import client
import configparser
import time

torque_cfg = configparser.ConfigParser()
torque_cfg.read("motorTorques.conf")

torques = {}
for motor in torque_cfg.options("Torques"):
    torques[motor] = torque_cfg.getfloat("Torques", motor)
print(torques)

class Victor:

    out_type = "PWMOut"

    def __init__(self, channel, slot=4):
        self.channel = channel
        name = client.ports[Victor.out_type][self.channel]
        self.kMaxOut = torques[name]
    
    def Set(self, speed, syncGroup=0):
        a = abs(speed)
        if a > 1:
            speed /= a
        client.s.update_output(Victor.out_type, self.channel, speed * self.kMaxOut)
        pass

    def Get(self):
        pass

    def PIDWrite(self, output):
        pass

Jaguar = Victor    # They basically do the same thing

class Gyro:
    def __init__(self, channel):
        self.channel = channel

    def Reset(self):
        pass

    def GetAngle(self):
        return client.r.get_value("InPorts", self.channel)

    def PIDGet(self):
        return self.GetAngle()

    def SetSensitivity(self, voltsPerDegreePerSecond):
        pass

class Encoder:
    def __init__(self, channel_a, channel_b):
        # Hardware encoders use two input channels
        # VIRSYS provides wheel rate (instantaneous) and angle (cumulative?)
	# so we use the two channels for that instead.

        self.channel_a = channel_a  # rate
        self.channel_b = channel_b  # distance
    
    def GetRate(self):
        return client.r.get_value("InPorts", self.channel_a)

    def GetDistance(self):
        return client.r.get_value("InPorts", self.channel_b)

class Timer(object):
    def __init__(self):
        self.start_time = 0
        self.accumulated_time = 0
        self.running = False
        self.Reset()
        
    def Get(self):
        if self.running:
            return (time.time() - self.start_time) + self.accumulated_time
        else:
            return self.accumulated_time
        
    def Reset(self):
        self.accumulated_time = 0
        self.start_time = time.time()
        
    def Start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
        
    def Stop(self):
        if self.running:
            self.accumulated_time += self.Get()
            self.running = False
        
    def HasPeriodPassed(self, period):
        if self.Get() > period:
            self.start_time += period
            return True
        return False

    def Wait(seconds):
        t = Timer()
        t.Start()
        while not t.HasPeriodPassed(seconds):
            pass

    def GetClock():
        return time.time()
