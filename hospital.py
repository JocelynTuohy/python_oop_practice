# Hospital Assignment
# You're going to build a hospital with patients in it! Create a hospital class.
import random

class Hospital(object):
    def __init__(self):
        self.patients = []
        self.name = "St. Mary's Hospital"
        self.capacity = 15
        self.beds = []
        self.createBeds()
        self.profile()
    def admit(self, new_patient):
        if len(self.patients) >= self.capacity:
            print (new_patient.name +
                   ' admission unsuccessful: the hospital is full.')
        else:
            for each in range(0, len(self.beds)):
                if self.beds[each]['available'] == True:
                    new_patient.bed_num = self.beds[each]['number']
                    self.beds[each]['available'] = False
                    self.beds[each]['patient_id'] = new_patient.idnum
                    print new_patient.name + ' admission successful.'
                    break
            self.patients.append(new_patient)
        return self
    def discharge(self, corpse):
        for each in range(0, len(self.patients)):
            if corpse.name == self.patients[each].name:
                for bed in range(0, len(self.beds)):
                    if self.beds[bed]['number'] == self.patients[each].bed_num:
                        self.beds[bed]['available'] = True
                        self.beds[bed]['patient_id'] = None
                        break
                self.patients[each].bed_num = None
                print corpse.name + ' discharge successful.'
                self.patients.pop(each)
                return self
        return self
    def createBeds(self):
        for each in range(0, self.capacity + 1):
            self.beds.append({'number' : each + 1, 'patient_id' : None,
                              'available' : True})
        return self
    def census(self):
        print 'Current Hospital Patients:'
        for each in range(0, len(self.patients)):
            print (
                'ID #: ' + str(self.patients[each].idnum) + ' - ' +
                self.patients[each].name + ' - ' +
                'Bed No.:' + str(self.patients[each].bed_num))
        print ''
        return self
    def profile(self):
        print self.name, '- Capacity:', str(self.capacity)
        return self

class Patient(object):
    def __init__(self, name, allergies):
        self.idnum = ''
        for _i in range(8):
            self.idnum += str(random.randint(0,9))
        self.name = name
        self.allergies = allergies
        self.bed_num = None

marys = Hospital()

amanda = Patient('Amanda Sharpe', ['apples'])
ashcan = Patient('"Ashcan" Pete', ['apples', 'anchovies'])
bob = Patient('Bob Jenkins', ['bananas'])
carolyn = Patient('Carolyn Fern', ['coconut'])
darrell = Patient('Darrell Simmons', ['dates'])
dexter = Patient('Dexter Drake', ['dates', 'doughnuts'])
gloria = Patient('Gloria Goldberg', ['gummi bears'])
harvey = Patient('Harvey Walters', ['hard candies'])
jenny = Patient('Jenny Barnes', ['jam'])
joe = Patient('Joe Diamond', ['jam', 'jell-o'])
kate = Patient('Kate Winthrop', ['kangaroos'])
mandy = Patient('Mandy Thompson', ['melons'])
michael = Patient('Michael McGlen', ['melons', 'mandarins'])
monterey = Patient('Monterey Jack', ['melons', 'mandarins', 'margaritas'])
mary = Patient('Sister Mary', ['melons', 'mandarins', 'margaritas', 'milk'])
vincent = Patient('Vincent Lee', ['virtually everything'])

marys.admit(amanda).admit(ashcan).admit(bob).admit(carolyn).admit(darrell)
marys.admit(dexter).admit(gloria).admit(harvey).admit(jenny).admit(joe)
marys.admit(kate).admit(mandy).admit(michael).admit(monterey).admit(mary)
marys.admit(vincent).discharge(ashcan).admit(vincent).census()
