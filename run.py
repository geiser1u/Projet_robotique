from BackProp_Python_v2 import NN
from Braitenberg import NN_evit
from vrep_pioneer_simulation import VrepPioneerSimulation
#from rdn import Pioneer # rdn pour ROS avec le pioneer
#import rospy
from online_trainer import OnlineTrainer
from online_traine_with_Braitenberg import OnlineTrainerWithBraitenberg
import json
import threading


robot = VrepPioneerSimulation()
#robot = Pioneer(rospy)
HL_size = 10 # nbre neurons of Hiden layer
network = NN(3, HL_size, 2)
braitenberg = NN_evit()

choice = input('Do you want to load previous network? (y/n) --> ')
if choice == 'y':
    with open('last_w.json') as fp:
        json_obj = json.load(fp)

    for i in range(3):
        for j in range(HL_size):
            network.wi[i][j] = json_obj["input_weights"][i][j]
    for i in range(HL_size):
        for j in range(2):
            network.wo[i][j] = json_obj["output_weights"][i][j]

trainer1 = OnlineTrainer(robot, network)
trainer2 = OnlineTrainerWithBraitenberg(robot, network, braitenberg)

choice = ''
while choice!='y' and choice !='n':
    choice = input('Do you want to learn? (y/n) --> ')

if choice == 'y':
    trainer = trainer1
    trainer.training = True
elif choice == 'n':
    trainer = trainer2
    trainer.training = False

target = input("Enter the first target : x y radian --> ")
target = target.split()
for i in range(len(target)):
    target[i] = float(target[i])
print('New target : [%d, %d, %d]'%(target[0], target[1], target[2]))

continue_running = True
while(continue_running):

    thread = threading.Thread(target=trainer.train, args=(target,))
    trainer.running = True
    thread.start()

    #Ask for stop running
    input("Press Enter to stop the current training")
    trainer.running = False

    #Log
    name = input("Give a name to the log file (default to last) --> ")
    
    if name=='':
        name='last'
    with open("logs/"+ name + ".json", 'w') as f:
        json.dump(trainer.log_file, f)
        f.close()
        print('Graph values have been saved in ' + name +'.json file')

    choice = ''
    while choice!='y' and choice !='n':
        choice = input("Do you want to continue ? (y/n) --> ")

    if choice == 'y':
        choice_learning = ''
        while choice_learning != 'y' and choice_learning !='n':
            choice_learning = input('Do you want to learn ? (y/n) --> ')
        if choice_learning =='y':
            trainer = trainer1
            trainer.training = True
        elif choice_learning == 'n':
            trainer = trainer2
            trainer.training = False
        target = input("Move the robot to the initial point and enter the new target : x y radian --> ")
        target = target.split()
        for i in range(len(target)):
            target[i] = float(target[i])
        print('New target : [%d, %d, %d]'%(target[0], target[1], target[2]))
    elif choice == 'n':
        continue_running = False


json_obj = {"input_weights": network.wi, "output_weights": network.wo}
with open('last_w.json', 'w') as fp:
    json.dump(json_obj, fp)

print("The last weights have been stored in last_w.json")
