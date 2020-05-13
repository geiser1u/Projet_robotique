
class NN_evit:
    def __init__(self):
        # Reflexe avant uniquement
#        self.leftWeights = [-0.2,-0.4,-0.6,-0.8,-1.0,-1.2,-1.4,-1.6,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
#        self.rightWeights = [-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        
         # Reflexe arrière uniquement
#        self.rightWeights = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6]
#        self.leftWeights = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.6,1.4,1.2,1.0,0.8,0.6,0.4,0.2]
#        self.leftWeights = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-0.2,-0.4,-0.6,-0.8,-1.0,-1.2,-1.4,-1.6]
#        self.rightWeights = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2]
         
        # Marche
#        self.rightWeights = [-0.2,-0.3,-0.4,-0.5,-0.6,-0.7,-0.8,-0.9,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
#        self.leftWeights = [-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2]
#        self.rightWeights = [-0.2,-0.4,-0.6,-0.8,-1.0,-1.2,-1.4,-1.6,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6]
#        self.leftWeights = [-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,1.6,1.4,1.2,1.0,0.8,0.6,0.4,0.2]
#        self.rightWeights = [0.5,0.4,0.3,0.2,-0.2,-0.3,-0.4,-0.5,-0.5,-0.4,-0.3,-0.2,0.2,0.3,0.4,0.5]
#        self.leftWeights = [-0.5,-0.4,-0.3,-0.2,0.2,0.3,0.4,0.5,0.5,0.4,0.3,0.2,-0.2,-0.3,-0.4,-0.5]
        
        # Meilleur pour l'instant pour 1 et 2 osbtacles perpendiculaires, ne marche pas avec le cul-de-sac et le labyrinthe
#        self.rightWeights = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0, -0.5,-0.4,-0.3,-0.2,0.2,0.3,0.4,0.5]
#        self.leftWeights = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0, 0.5,0.4,0.3,0.2,-0.2,-0.3,-0.4,-0.5]
     
        self.rightWeights = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0, 0.5,0.4,0.3,0.2, -0.2,-0.3,-0.4,-0.5]
        self.leftWeights = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0, -0.5,-0.4,-0.3,-0.2, 0.2,0.3,0.4,0.5]
        
#        self.rightWeights = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0, -0.2,-0.3,-0.4,-0.5,0.5,0.4,0.3,0.2]
#        self.leftWeights = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0, 0.2,0.3,0.4,0.5,-0.5,-0.4,-0.3,-0.2]

        
        # Comportement d'évitement avec les capteurs latéraux et de contournement avec les capteurs frontaux
#        self.rightWeights = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0, 0.3,0.2,-0.2,-0.3,0.3,0.2,-0.2,-0.3]
#        self.leftWeights = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0, -0.3,-0.2,0.2,0.3,-0.3,-0.2,0.2,0.3]
        
#        self.rightWeights = [-0.2,-0.2,-0.2,-0.2,0.2,0.2,0.2,0.2, -0.2,-0.2,-0.2,-0.2,0.2,0.2,0.2,0.2]
#        self.leftWeights = [0.2,0.2,0.2,0.2,-0.2,-0.2,-0.2,-0.2, 0.2,0.2,0.2,0.2,-0.2,-0.2,-0.2,-0.2]
        self.gain = 1
        
        # Pour passer entre les osbstacles au lieu de tous les contourner
#        self.rightWeights = [0.0,0.0,0.0,0.0,-0.6,-0.7,-0.8,-0.9,0.2,0.3,0.4,0.5,0.0,0.0,0.0,0.0]
#        self.leftWeights = [0.0,0.0,0.0,0.0,-0.5,-0.4,-0.3,-0.2,0.9,0.8,0.7,0.6,0.0,0.0,0.0,0.0]
        
        # Reflexe avant et arrière (comment calibrer ?)
#        self.leftWeights = [-0.2,-0.4,-0.6,-0.8,-1.0,-1.2,-1.4,-1.6,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6]
#        self.rightWeights = [-1.6,-1.4,-1.2,-1.0,-0.8,-0.6,-0.4,-0.2,1.6,1.4,1.2,1.0,0.8,0.6,0.4,0.2]
        
        
    def runNN(self, command, inputs):
        motors = command
#        print(command)
#        print(inputs)
        for i in range(16):
            motors[0] += self.gain * self.leftWeights[i] * inputs[i]
            motors[1] += self.gain * self.rightWeights[i] * inputs[i]
        return motors