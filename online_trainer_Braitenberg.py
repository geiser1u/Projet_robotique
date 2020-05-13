import time 

class OnlineTrainerBraitenberg:
    def __init__(self, robot, NN):
        self.robot = robot
        self.network = NN
        
    def train(self):

        while self.running:
            distances = self.robot.get_distances()
            command = self.network.runNN([-2,-2], distances)
            self.robot.set_motor_velocity(command)                 
            time.sleep(0.050)
                
        self.robot.set_motor_velocity([0,0])
        self.running = False
