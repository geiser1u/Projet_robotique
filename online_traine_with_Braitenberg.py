import time
import math


def theta_s(x,y):
    if x>0:
        return 1*math.atan(1*y)
    if x<=0:
        return 1*math.atan(-1*y)

class OnlineTrainerWithBraitenberg:
    def __init__(self, robot, NN, NN_evit):
        """
        Args:
            robot (Robot): a robot instance following the pattern of
                VrepPioneerSimulation
            target (list): the target position [x,y,theta]
        """
        self.robot = robot
        self.network = NN
        self.braitenberg = NN_evit
        self.log_file = {}
        self.alpha = [1/6,1/6,1.0/math.pi]  # normalition avec limite du monde cartesien = -3m à + 3m
        # alpha_x = 1 / (x_max - x_min)
        
    def train(self, target):
        position = self.robot.get_position()

        network_input = [0, 0, 0]
        network_input[0] = (position[0]-target[0])*self.alpha[0]
        network_input[1] = (position[1]-target[1])*self.alpha[1]
        network_input[2] = (position[2]-target[2]-theta_s(position[0], position[1]))*self.alpha[2]
        #Teta_t = 0

        #Set up logging
        t0 = time.time()
        times = []
        Q1s = []
        positions = []
        theta_shifts = []
        criterions = []
        commands = []

        while self.running:
            debut = time.time()
            command = self.network.runNN(network_input) # propage erreur et calcul vitesses roues instant t
            
                      
            alpha_x = 1/6
            alpha_y = 1/6
            alpha_teta = 1.0/math.pi
                        
            crit_av= alpha_x*alpha_x*(position[0]-target[0])*(position[0]-target[0]) + alpha_y*alpha_y*(position[1]-target[1])*(position[1]-target[1]) + alpha_teta*alpha_teta*(position[2]-target[2]-theta_s(position[0], position[1]))*(position[2]-target[2]-theta_s(position[0], position[1]))  
            
            if not self.training:
                distances = self.robot.get_distances()
                command = self.braitenberg.runNN(command, distances)
            
            self.robot.set_motor_velocity(command) # applique vitesses roues instant t,                     
            time.sleep(0.050) # attend delta t
            # Choix arbitraire ?
            position = self.robot.get_position() #  obtient nvlle pos robot instant t+1       
            
            network_input[0] = (position[0]-target[0])*self.alpha[0]
            network_input[1] = (position[1]-target[1])*self.alpha[1]
            network_input[2] = (position[2]-target[2]-theta_s(position[0], position[1]))*self.alpha[2]
            
            crit_ap= alpha_x*alpha_x*(position[0]-target[0])*(position[0]-target[0]) + alpha_y*alpha_y*(position[1]-target[1])*(position[1]-target[1]) + alpha_teta*alpha_teta*(position[2]-target[2]-theta_s(position[0], position[1]))*(position[2]-target[2]-theta_s(position[0], position[1])) 

            #Logs
            times.append(debut - t0)
            # Save the current state of the lesson
            positions.append(self.robot.get_position()) # This function takes 50 ms to compute
            commands.append(self.robot.get_motor_velocity())
            theta_shifts.append(theta_s(position[0]-target[0], position[1]-target[1]))
            criterions.append(crit_ap)

            if self.training:
                delta_t = (time.time()-debut) # Pas le temps de simulation ! Pourquoi différent de 0.050 ?

                grad = [
                    (-2/delta_t)*(alpha_x*alpha_x*(position[0]-target[0])*delta_t*self.robot.r*math.cos(position[2])
                    +alpha_y*alpha_y*(position[1]-target[1])*delta_t*self.robot.r*math.sin(position[2])
                    -alpha_teta*alpha_teta*(position[2]-target[2]-theta_s(position[0], position[1]))*delta_t*self.robot.r/(2*self.robot.R)),

                    (-2/delta_t)*(alpha_x*alpha_x*(position[0]-target[0])*delta_t*self.robot.r*math.cos(position[2])
                    +alpha_y*alpha_y*(position[1]-target[1])*delta_t*self.robot.r*math.sin(position[2])
                    +alpha_teta*alpha_teta*(position[2]-target[2]-theta_s(position[0], position[1]))*delta_t*self.robot.r/(2*self.robot.R))
                    ]

                # The two args after grad are the gradient learning steps for t+1 and t
                # si critere augmente on BP un bruit fction randon_update, sion on BP le gradient
                
                if (crit_ap <= crit_av) :
                    self.network.backPropagate(grad, 0.2, 0) # grad, pas d'app, moment
                    # Pas d'apprentissage = gain de l'erreur (coef multiplicateur)
                else :
                    #self.network.random_update(0.001)
                    self.network.backPropagate(grad, 0.2, 0)
                
        self.robot.set_motor_velocity([0,0]) # stop  apres arret  du prog d'app
        #position = self.robot.get_position() #  obtient nvlle pos robot instant t+1
                #Teta_t=position[2]
             
        #Logs
        duration = time.time()-t0
        self.log_file = {"size":12, "target":target, "duration":duration,
                         "times":times, "positions":positions, "theta_shifts":theta_shifts,
                         "criterions":criterions, "commands":commands}
        
        self.running = False
