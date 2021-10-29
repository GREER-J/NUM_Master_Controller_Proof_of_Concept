"""
DATE: 17.10.21
AIM: Mission planning tester
AUTH: GREER, J
DES:
In NUM we're likely going to have at least 2 agents, a UAV and the USV.
These agents are going to have to navigate cooperatively but we may be able to avoid multi-agent SLAM

PLAN:
 - True map
 - Local agent simulation
 - Macro map
 - Macro agent organiser

TODO:
 - Everything
"""
# Imports
from world import World, World_object, Marker
from agent import UAV, USV
from controller import Master_controller

# Variables
x_max = 25
y_max = 25
macro_grid_size = 5


def setup():
    """setup Setup the simulation
    """
    controller = Master_controller()
    world = World(x_max=x_max, y_max=y_max,
                  macro_grid_size=macro_grid_size, controller=controller)
    uav = UAV(x_pos=3, y_pos=4, world=world)
    usv = USV(x_pos=0, y_pos=0, world=world)
    m1 = Marker(14, 12, world)
    m2 = Marker(12, 16, world)
    return(world)


def main():
    world = setup()
    continue_var = True
    time_step = 0
    cutoff = 10
    while(continue_var):
        # Run agents
        for agent in world.agents:
            agent.run_loop()

        if(time_step > cutoff):
            continue_var = False
        time_step += 1
    print("Done")


if(__name__ == '__main__'):
    main()
