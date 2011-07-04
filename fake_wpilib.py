import client

class Victor:

    # Largest amount of torque to output
    kMaxOut = 200

    def __init__(self, channel, slot=4):
        self.channel = channel
    
    def Set(self, speed, syncGroup=0):
        a = abs(speed)
        if a > 1:
            speed /= a
        client.s.update_output("PWMOut", self.channel, speed * Victor.kMaxOut)
        pass

    def Get(self):
        pass

    def PIDWrite(self, output):
        pass

Jaguar = Victor    # They basically do the same thing
