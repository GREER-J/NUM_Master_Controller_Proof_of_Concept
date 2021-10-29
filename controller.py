class Master_controller:
    def __init__(self) -> None:
        self.found_objects = 0
        self.objects_identified = 0
        self.object_interacted = 0
        self.total_objects = 'n'
        self.known_objects = []

    def add_detected_object(self, object):
        self.known_objects.append(object)
