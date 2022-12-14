import pybullet as p
import pybullet_data as pd
import math
import time

p.connect(p.GUI)
p.setGravity(0,0,-9.8)

p.setAdditionalSearchPath(pd.getDataPath())
p.resetDebugVisualizerCamera(cameraDistance=1,cameraYaw=-1000,\
                             cameraPitch=-30,cameraTargetPosition=[0.5,0.4,0.2])

pandaUid=p.loadURDF("franka_panda/panda.urdf",useFixedBase=True)
tableUid=p.loadURDF("table/table.urdf",basePosition=[0.5,0,-0.65])
tableUid2=p.loadURDF("table/table.urdf",basePosition=[0.5,1,-0.65])
trayUid=p.loadURDF("tray/traybox.urdf",basePosition=[0.65,0,0])
trayUid=p.loadURDF("tray/traybox.urdf",basePosition=[0.2,0.7,0])


objectUid=p.loadURDF("random_urdfs/050/050.urdf",basePosition=[0.7,0,0.1])
object1Uid=p.loadURDF("random_urdfs/001/001.urdf",basePosition=[0.7,0.1,0.1])
object2Uid=p.loadURDF("random_urdfs/002/002.urdf",basePosition=[0.6,-0.2,0.1])
object3Uid=p.loadURDF("random_urdfs/003/003.urdf",basePosition=[0.8,0.1,0.1])
# object4Uid=p.loadURDF("random_urdfs/004/004.urdf",basePosition=[0.7,-0.1,0.7])
# object5Uid=p.loadURDF("random_urdfs/005/005.urdf",basePosition=[0.6,0.1,0.3])
# object6Uid=p.loadURDF("random_urdfs/006/006.urdf",basePosition=[0.8,-0.2,0.4])
# object7Uid=p.loadURDF("random_urdfs/007/007.urdf",basePosition=[0.6,0.2,0.4])
# object8Uid=p.loadURDF("random_urdfs/008/008.urdf",basePosition=[0.7,-0.1,0.4])
# object9Uid=p.loadURDF("random_urdfs/009/009.urdf",basePosition=[0.6,0.1,0.4])

state_durations=[0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]
control_dt=1./240.
p.setTimeStep=control_dt
state_t=0.
current_state=0

while True:

    state_t+=control_dt
    p.configureDebugVisualizer(p.COV_ENABLE_SINGLE_STEP_RENDERING)


    if current_state==0:
        p.setJointMotorControl2(pandaUid,0,p.POSITION_CONTROL,0)
        
    if current_state==1:
        p.setJointMotorControl2(pandaUid,0,p.POSITION_CONTROL,0)
        p.setJointMotorControl2(pandaUid,1,p.POSITION_CONTROL,math.pi/4.)
        p.setJointMotorControl2(pandaUid,2,p.POSITION_CONTROL,0)
        p.setJointMotorControl2(pandaUid,3,p.POSITION_CONTROL,-math.pi/2.)
        p.setJointMotorControl2(pandaUid,4,p.POSITION_CONTROL,0)
        p.setJointMotorControl2(pandaUid,5,p.POSITION_CONTROL,3*math.pi/4)
        p.setJointMotorControl2(pandaUid,6,p.POSITION_CONTROL,-math.pi/4.)
        p.setJointMotorControl2(pandaUid,9,p.POSITION_CONTROL,0.08)
        p.setJointMotorControl2(pandaUid,10,p.POSITION_CONTROL,0.08)

    if current_state==2:
        p.setJointMotorControl2(pandaUid,1,p.POSITION_CONTROL,math.pi/4.+.15)
        p.setJointMotorControl2(pandaUid,3,p.POSITION_CONTROL,-math.pi/2.+.15)

    if current_state==3:
        p.setJointMotorControl2(pandaUid,9,p.POSITION_CONTROL,force=150)
        p.setJointMotorControl2(pandaUid,10,p.POSITION_CONTROL,force=150)

    if current_state==4:
        p.setJointMotorControl2(pandaUid,1,p.POSITION_CONTROL,math.pi/4.-1)
        p.setJointMotorControl2(pandaUid,3,p.POSITION_CONTROL,-math.pi/2.-1)
     
    if current_state==5:
        p.setJointMotorControl2(pandaUid,0,p.POSITION_CONTROL,math.pi/2.5)  
        
    if current_state==6: 
        p.setJointMotorControl2(pandaUid,1,p.POSITION_CONTROL,math.pi/4.)
        p.setJointMotorControl2(pandaUid,2,p.POSITION_CONTROL,0)
        p.setJointMotorControl2(pandaUid,3,p.POSITION_CONTROL,-math.pi/2.)
        p.setJointMotorControl2(pandaUid,4,p.POSITION_CONTROL,0)
        p.setJointMotorControl2(pandaUid,5,p.POSITION_CONTROL,3*math.pi/4)
        p.setJointMotorControl2(pandaUid,6,p.POSITION_CONTROL,-math.pi/4.)  
        
    if current_state==7:
        p.setJointMotorControl2(pandaUid,9,p.POSITION_CONTROL,0.08)
        p.setJointMotorControl2(pandaUid,10,p.POSITION_CONTROL,0.08)    
        
    if current_state==8:
        p.setJointMotorControl2(pandaUid,1,p.POSITION_CONTROL,math.pi/4.-1)
        p.setJointMotorControl2(pandaUid,3,p.POSITION_CONTROL,-math.pi/2.-1)  
        
    if current_state==9:
        p.setJointMotorControl2(pandaUid,0,p.POSITION_CONTROL,0)    
     
    if current_state==10:
        p.setJointMotorControl2(pandaUid,0,p.POSITION_CONTROL,math.pi/15.)
        p.setJointMotorControl2(pandaUid,1,p.POSITION_CONTROL,math.pi/4.)
        p.setJointMotorControl2(pandaUid,2,p.POSITION_CONTROL,0)
        p.setJointMotorControl2(pandaUid,3,p.POSITION_CONTROL,-math.pi/2.)
        p.setJointMotorControl2(pandaUid,4,p.POSITION_CONTROL,0)
        p.setJointMotorControl2(pandaUid,5,p.POSITION_CONTROL,3*math.pi/4)
        p.setJointMotorControl2(pandaUid,6,p.POSITION_CONTROL,-math.pi/4.)    
        
    if current_state==11:
        p.setJointMotorControl2(pandaUid,1,p.POSITION_CONTROL,math.pi/4.+.15)
        p.setJointMotorControl2(pandaUid,3,p.POSITION_CONTROL,-math.pi/2.+.15)

    if current_state==12:
        p.setJointMotorControl2(pandaUid,9,p.POSITION_CONTROL,force=200)
        p.setJointMotorControl2(pandaUid,10,p.POSITION_CONTROL,force=200)  
          
    if current_state==13:
        p.setJointMotorControl2(pandaUid,1,p.POSITION_CONTROL,math.pi/4.-1)
        p.setJointMotorControl2(pandaUid,3,p.POSITION_CONTROL,-math.pi/2.-1)    
        
    if current_state==14:
        p.setJointMotorControl2(pandaUid,0,p.POSITION_CONTROL,math.pi/2.7)
        
    if current_state==15: 
        p.setJointMotorControl2(pandaUid,1,p.POSITION_CONTROL,math.pi/4.)
        p.setJointMotorControl2(pandaUid,2,p.POSITION_CONTROL,0)
        p.setJointMotorControl2(pandaUid,3,p.POSITION_CONTROL,-math.pi/2.)
        p.setJointMotorControl2(pandaUid,4,p.POSITION_CONTROL,0)
        p.setJointMotorControl2(pandaUid,5,p.POSITION_CONTROL,3*math.pi/4)
        p.setJointMotorControl2(pandaUid,6,p.POSITION_CONTROL,-math.pi/4.)  
        
    if current_state==16:
        p.setJointMotorControl2(pandaUid,9,p.POSITION_CONTROL,0.08)
        p.setJointMotorControl2(pandaUid,10,p.POSITION_CONTROL,0.08)  
        
    if current_state==17:
        p.setJointMotorControl2(pandaUid,1,p.POSITION_CONTROL,math.pi/4.-1.)
        p.setJointMotorControl2(pandaUid,3,p.POSITION_CONTROL,-math.pi/2.-1.) 
  
    if state_t>state_durations[current_state]:
        current_state+=1
        if current_state>=len(state_durations):
            current_state=0
        state_t=0
        
    p.stepSimulation()
