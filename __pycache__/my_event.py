
class Event:
    def __init__(self, time, obj_a, obj_b):
        self.time = time
        self.a = obj_a
        self.b = obj_b

        # Count states for validation
        if obj_a is not None:
            self.count_a = getattr(obj_a, 'count', -1)
        else:
            self.count_a = -1
        if obj_b is not None:
            self.count_b = getattr(obj_b, 'count', -1)
        else:
            self.count_b = -1

    def __lt__(self, that):
        return self.time < that.time

    def is_valid(self):
        if (self.a is not None) and hasattr(self.a, 'count') and (self.a.count != self.count_a):
            return False
        if (self.b is not None) and hasattr(self.b, 'count') and (self.b.count != self.count_b):
            return False
        return True
