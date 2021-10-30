class Master_controller:
    def __init__(self) -> None:
        self.found_objects = 0
        self.objects_identified = 0
        self.object_interacted = 0
        self.total_objects = 3
        self.known_objects = []

    def add_detected_object(self, object):
        self.known_objects.append(object)
        self.found_objects += 1

    def get_available_for_ident(self):
        available = []
        for obj in self.known_objects:
            if(obj.detected == True and obj.identified == False):
                available.append(obj)
        return(available)
