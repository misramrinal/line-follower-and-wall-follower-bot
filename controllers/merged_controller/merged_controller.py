"""first_robo_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

class controller(Robot):
    def __init__(self):
        
# create the Robot instance.

# get the time step of the current world.
        timestep = int(self.getBasicTimeStep())
        
        motorFR = self.getDevice('fr_motor')
        motorFL = self.getDevice('fl_motor')
        motorRR = self.getDevice('rr_motor')
        motorRL = self.getDevice('rl_motor')
        
        motorFR.setPosition(float('inf'))
        motorFL.setPosition(float('inf'))
        motorRR.setPosition(float('inf'))
        motorRL.setPosition(float('inf'))
        
        motorFR.setVelocity(0.0)
        motorFL.setVelocity(0.0)
        motorRR.setVelocity(0.0)
        motorRL.setVelocity(0.0)
        
        ds_front_left = self.getDevice('ir_front_left')
        ds_front_right = self.getDevice('ir_front_right')
        ds_rear_right = self.getDevice('ir_rear_right')
        
        ds_front_left.enable(timestep)
        ds_front_right.enable(timestep)
        ds_rear_right.enable(timestep)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
    def run(self):

        while self.step(timestep) != -1:
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
wall_robot = controller()
wall_robot.run()
# Enter here exit cleanup code.
