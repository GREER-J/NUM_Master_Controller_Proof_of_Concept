
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

    def detect_object(self):
        for obj in self.world.objects:
            del_x = obj.x_pos - self.x_pos
            if(del_x <= self.detection_range):
                del_y = obj.y_pos - self.y_pos
                if(del_y <= self.detection_range):
                    if(obj.detected == False):
                        obj.detected = True
                        return(obj)

    def calculate_macro_grid_pos(self):
        macro_x_grid = int(self.x_pos / self.world.macro_grid_size)
        macro_y_grid = int(self.y_pos / self.world.macro_grid_size)
        return(macro_x_grid, macro_y_grid)

    def report_object_to_controller(self, object):
        object.macro_x_pos, object.macro_y_pos = self.calculate_macro_grid_pos(
            object)
        self.world.controller.add_detected_object(object)

    def get_interaction_task(self):
        print(f"{self.name} interacting")
        pass

    def get_identification_task(self):
        print(f"{self.name} identifying")
        available = self.world.controller.get_available_for_ident()
        print(len(available))

    def get_scout_target(self):
        print(f"{self.name} scouting")
        target_x = self.world.x_max / 2
        target_y = self.world.y_max / 2
        self.move(target_x, target_y)
        obj = self.detect_object()
        if(obj):
            print("Found obj!")
            self.world.controller.add_detected_object(obj)

        pass

    def run_loop(self):
        # Update task status
        found_objects = self.world.controller.found_objects
        identified_objects = self.world.controller.objects_identified
        interacted_objects = self.world.controller.object_interacted
        total_objects = self.world.controller.total_objects
        if(identified_objects > interacted_objects):
            # Interaction task available
            self.get_interaction_task()
        if(found_objects > identified_objects):
            # Identification task available
            self.get_identification_task()
        # Otherwise scout for more things
        self.get_scout_target()


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
