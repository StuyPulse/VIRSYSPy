import client

class Victor:
    def __init__(self, channel, slot=4):
        self.channel = channel
        self.kMaxOut = 200
    
    def set(self, speed, syncGroup=0):
        a = abs(speed)
        if a > 1:
            speed /= a
        client.s.update_output("PWMOut", self.channel, speed * self.kMaxOut)
        pass

    def get(self):
        pass

    def pidWrite(self, output):
        pass
