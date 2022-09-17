from controller import Robot
from controller import Keyboard
# create the Robot instance.
robot = Robot()
kb = Keyboard()
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

motorFR = robot.getDevice('front_right_motor')
motorFL = robot.getDevice('front_left_motor')
motorRR = robot.getDevice('rear_right_motor')
motorRL = robot.getDevice('rear_left_motor')

motorFR.setPosition(float('inf'))
motorFL.setPosition(float('inf'))
motorRR.setPosition(float('inf'))
motorRL.setPosition(float('inf'))

motorFR.setVelocity(0.0)
motorFL.setVelocity(0.0)
motorRR.setVelocity(0.0)
motorRL.setVelocity(0.0)

ir_left = robot.getDevice('ir_left')
ir_right = robot.getDevice('ir_right')

ir_left.enable(timestep)
ir_right.enable(timestep)
kb.enable(timestep)

# Main loop:
while robot.step(timestep) != -1:
    # val_left = ir_left.getValue()
    # val_right = ir_right.getValue()
    # #print('a')
    # print(val_left, val_right)
    
    key=kb.getKey()
    if key==315:
        motorRR.setVelocity(5.0)
        motorRL.setVelocity(5.0)
        motorFR.setVelocity(5.0)
        motorFL.setVelocity(5.0)
    if key==316:
        motorRR.setVelocity(5.0)
        motorRL.setVelocity(-5.0)
        motorFR.setVelocity(5.0)
        motorFL.setVelocity(-5.0)
    if key==314:
        motorRR.setVelocity(-5.0)
        motorRL.setVelocity(5.0)
        motorFR.setVelocity(-5.0)
        motorFL.setVelocity(5.0)
      
    pass