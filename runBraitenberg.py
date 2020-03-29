from Braitenberg import NN_evit
from vrep_pioneer_simulation import VrepPioneerSimulation
from online_trainer_Braitenberg import OnlineTrainerBraitenberg

import threading


robot = VrepPioneerSimulation()
network = NN_evit()

trainer = OnlineTrainerBraitenberg(robot, network)

continue_running = True
while(continue_running):

    thread = threading.Thread(target=trainer.train)
    trainer.running = True
    thread.start()

    #Ask for stop running
    input("Press Enter to stop the current training")
    trainer.running = False
    continue_running = False
