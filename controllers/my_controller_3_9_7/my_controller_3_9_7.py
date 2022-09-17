"""first_robo_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.


# get the time step of the current world.
a = 0

if a == 0:
    
    robot = Robot()
    
    timestep = int(robot.getBasicTimeStep())
    
    motorFR = robot.getDevice('fr_motor')
    motorFL = robot.getDevice('fl_motor')
    motorRR = robot.getDevice('rr_motor')
    motorRL = robot.getDevice('rl_motor')
    
    
    
    motorFR.setPosition(float('inf'))
    motorFL.setPosition(float('inf'))
    motorRR.setPosition(float('inf'))
    motorRL.setPosition(float('inf'))
    
    
    motorFR.setVelocity(0.0)
    motorFL.setVelocity(0.0)
    motorRR.setVelocity(0.0)
    motorRL.setVelocity(0.0)
    
    ds_front_left = robot.getDevice('ir_front_left')
    ds_front_right = robot.getDevice('ir_front_right')
    ds_rear_right = robot.getDevice('ir_rear_right')
    
    ds_front_left.enable(timestep)
    ds_front_right.enable(timestep)
    ds_rear_right.enable(timestep)



# Main loop:
# - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        val_front_left = ds_front_left.getValue()
        val_front_right = ds_front_right.getValue()
        val_rear_right = ds_rear_right.getValue()
        
        if val_front_right <= 450 and val_rear_right <= 450:
        #forward
            motorRR.setVelocity(5.0)
            motorRL.setVelocity(5.0)
            motorFR.setVelocity(5.0)
            motorFL.setVelocity(5.0)
        if val_front_right > 450 and val_rear_right > 450:
        #right
            motorRR.setVelocity(-5.0)
            motorRL.setVelocity(5.0)
            motorFR.setVelocity(-5.0)
            motorFL.setVelocity(5.0)
        if val_front_right <= 450 and val_rear_right > 450:
        
            motorRR.setVelocity(5.0)
            motorRL.setVelocity(5.0)
            motorFR.setVelocity(5.0)
            motorFL.setVelocity(5.0)
        if val_front_left < 1000:
        #stop
            motorFR.setVelocity(0.0)
            motorFL.setVelocity(0.0)
            motorRR.setVelocity(0.0)
            motorRL.setVelocity(0.0)
            #a=a+1
        
    #a=a+1
    
if a == 0:
    robot = Robot()
        
    timestep = int(robot.getBasicTimeStep())
        
    motorFRc = robot.getDevice('front_right_motor')
    motorFLc = robot.getDevice('front_left_motor')
    motorRRc = robot.getDevice('rear_right_motor')
    motorRLc = robot.getDevice('rear_left_motor')
        
    motorFRc.setPosition(float('inf'))
    motorFLc.setPosition(float('inf'))
    motorRRc.setPosition(float('inf'))
    motorRLc.setPosition(float('inf'))
        
    motorFRc.setVelocity(0.0)
    motorFLc.setVelocity(0.0)
    motorRRc.setVelocity(0.0)
    motorRLc.setVelocity(0.0)
        
    ds_left = robot.getDevice('ir_left')
    ds_right = robot.getDevice('ir_right')
        
    ds_left.enable(timestep)
    ds_right.enable(timestep)
    while robot.step(timestep) != -1:
        val_left = ds_left.getValue()
        val_right = ds_right.getValue()
        if val_left >= 400 and val_right >= 400:
            #forward
            motorRRc.setVelocity(5.0)
            motorRLc.setVelocity(5.0)
            motorFRc.setVelocity(5.0)
            motorFLc.setVelocity(5.0)
        if val_left < 400 and val_right >= 400:
            #right
            motorRRc.setVelocity(-5.0)
            motorRLc.setVelocity(5.0)
            motorFRc.setVelocity(-5.0)
            motorFLc.setVelocity(5.0)
        if val_left >= 400 and val_right < 400:
            #left
            motorRRc.setVelocity(5.0)
            motorRLc.setVelocity(-5.0)
            motorFRc.setVelocity(5.0)
            motorFLc.setVelocity(-5.0)
        if val_left < 400 and val_right < 400:
            #stop
            motorFRc.setVelocity(0.0)
            motorFLc.setVelocity(0.0)
            motorRRc.setVelocity(0.0)
            motorRLc.setVelocity(0.0)
        pass


