
class Agent():
    def __init__(self, x_pos, y_pos, world):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.world = world
        self.world.add_agent(self)

    def move(self, target_x, target_y):
        for i in range(self.movement_range):
            del_x = target_x - self.x_pos
            del_y = target_y - self.y_pos
            if(del_x > 0):
                self.x_pos += 1
            elif(del_x < 0):
                self.x_pos -= 1
            if(del_y > 0):
                self.y_pos += 1
            elif(del_y < 0):
                self.y_pos -= 1
        print(f"{self.name} moved to ({self.x_pos},{self.y_pos})")

    def search(self):
        for obj in self.world.objects:
            del_x = obj.x_pos - self.x_pos
            if(del_x <= self.detection_range):
                del_y = obj.y_pos - self.y_pos
                if(del_y <= self.detection_range):
                    print(obj)
                    return(obj)

    def calculate_macro_grid_pos(self):
        macro_x_grid = int(self.x_pos / self.world.macro_grid_size)
        return(macro_x_grid)

    def run_loop(self):
        # Update task status
        found_objects = self.world.controller.found_objects
        identified_objects = self.world.controller.objects_identified
        interacted_objects = self.world.controller.object_interacted
        total_objects = self.world.controller.total_objects


class UAV(Agent):
    def __init__(self, x_pos, y_pos, world):
        super().__init__(x_pos, y_pos, world)
        self.icon = "<"
        self.movement_range = 2
        self.detection_range = 2
        self.name = "UAV"


class USV(Agent):
    def __init__(self, x_pos, y_pos, world):
        super().__init__(x_pos, y_pos, world)
        self.icon = "H"
        self.movement_range = 1
        self.detection_range = 2
        self.name = "USV"
