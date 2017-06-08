# Hospital Assignment
# You're going to build a hospital with patients in it! Create a hospital class.
import time

class Hospital(object):
    def __init__(self):
        self.patients = []
        self.name = "St. Mary's Hospital"
        self.capacity = 15
        self.beds = []
        self.createBeds()
    def admit(self, new_patient):
        if len(self.patients) >= self.capacity:
            print 'Patient admission unsuccessful: the hospital is full.'
        else:
            for each in range(0, len(self.beds)):
                pass
        return self
    def discharge(self, corpse):
        pass
        return self
    def createBeds(self):
        for each in range(0, self.capacity + 1):
            self.beds.append({'number' : each + 1, 'patient_id' : '',
                              'available' : True})

class Patient(object):
    def __init__(self, name, allergies, bed_num=None):
        self.idnum = hex(int(time.clock()*10000000))[2:]
        self.name = name
        self.allergies = allergies
        self.bed_num = bed_num

marys = Hospital()