class Hospital(object):
    def __init__(self, uid , num_beds, location):
        self.uid = uid
        self.total_beds = num_beds
        self.remaining_beds = self.total_beds
        self.occupied_beds = 0
        self.is_full = False
        self.location = location

    def occupy_bed(self):
        if not self.is_full:
            self.remaining_beds -= 1
            self.occupied_beds += 1
            if self.remaining_beds == 0:
                self.is_full = True
            