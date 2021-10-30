class World:
    def __init__(self, x_max, y_max, macro_grid_size, controller):
        self.x_max = x_max
        self.y_max = y_max
        self.macro_grid_size = macro_grid_size
        self.controller = controller
        self.agents = []
        self.objects = []

    def add_world_object(self, object):
        self.objects.append(object)

    def add_agent(self, agent):
        self.agents.append(agent)

    def print_world(self):
        for row in self.map:
            str_row = ''
            for x in row:
                str_row += str(x)
            print(str_row)


class World_object:
    """
    A generic class for world objects
    """

    def __init__(self, x_pos, y_pos, world):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.detected = False
        self.identified = False
        self.interacted = False
        world.add_world_object(self)


class Marker(World_object):
    def __init__(self, x_pos, y_pos, world):
        super().__init__(x_pos, y_pos, world)
        self.obj_type = "marker"
        self.icon = "o"
