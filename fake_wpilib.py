import client
import configparser

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
