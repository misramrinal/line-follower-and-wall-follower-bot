"""first_robo_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot


# create the Robot instance.
robot = Robot()


# get the time step of the current world.
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
    pass

# Enter here exit cleanup code.
