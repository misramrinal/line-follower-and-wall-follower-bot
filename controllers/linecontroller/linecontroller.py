"""first_robo_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot


# create the Robot instance.
robot = Robot()


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

ds_left = robot.getDevice('ir_left')
ds_right = robot.getDevice('ir_right')

ds_left.enable(timestep)
ds_right.enable(timestep)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    val_left = ds_left.getValue()
    val_right = ds_right.getValue()
    if val_left >= 400 and val_right >= 400:
    #forward
        motorRR.setVelocity(5.0)
        motorRL.setVelocity(5.0)
        motorFR.setVelocity(5.0)
        motorFL.setVelocity(5.0)
    if val_left < 400 and val_right >= 400:
    #right
        motorRR.setVelocity(-5.0)
        motorRL.setVelocity(5.0)
        motorFR.setVelocity(-5.0)
        motorFL.setVelocity(5.0)
    if val_left >= 400 and val_right < 400:
    #left
        motorRR.setVelocity(5.0)
        motorRL.setVelocity(-5.0)
        motorFR.setVelocity(5.0)
        motorFL.setVelocity(-5.0)
    if val_left < 400 and val_right < 400:
    #stop
        motorFR.setVelocity(0.0)
        motorFL.setVelocity(0.0)
        motorRR.setVelocity(0.0)
        motorRL.setVelocity(0.0)
    pass

# Enter here exit cleanup code.
