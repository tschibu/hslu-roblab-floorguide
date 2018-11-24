import os

class PepperConfiguration(object):
    Name = None
    Ip = None
    Port = 0
    Username = None
    Password = None


    def __init__(self, name, ip="", port= 0):
        self.Name = name
        self.Username = "nao"
        self.Port = 9559
        if name == "Amber":
            self.Ip = "192.168.1.101"
            self.Password = "i1-p2e3p"
        elif name == "Porter":
            self.Ip = "192.168.1.102"
            self.Password = "i2-p2e3p"
        else:
            self.Ip = ip
            self.Port = port

    @property
    def IpPort(self):
        return self.Ip + ":" + str(self.Port)

    def isAvailable(self):
        response = os.system("ping -c 1 -w2 " + self.Ip + " > /dev/null 2>&1")
        if(response == 0):
            return True
        else:
            return False
