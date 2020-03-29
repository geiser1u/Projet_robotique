
class NN_evit:
    def __init__(self):
        # Reflexe avant uniquement
#        self.leftWeights = [-0.2,-0.4,-0.6,-0.8,-1.0,-1.2,-1.4,-1.6,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
#        self.rightWeights = [-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        
        # Reflexe avant et arrière (comment calibrer ?)
        self.leftWeights = [-0.2,-0.4,-0.6,-0.8,-1.0,-1.2,-1.4,-1.6,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6]
        self.rightWeights = [-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,1.6,1.4,1.2,1.0,0.8,0.6,0.4,0.2]
        self.gain = 0.1
        
    def runNN(self, command, inputs):
        motors = command
        for i in range(16):
            motors[0] += self.gain * self.leftWeights[i] * inputs[i]
            motors[1] += self.gain * self.rightWeights[i] * inputs[i]
        return motors