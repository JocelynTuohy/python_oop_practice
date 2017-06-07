# Call Center Assignment
# Store calls in a queue while callers wait to speak with a call center
# employee.

import uuid

# Call Class
class Call(object):
    def __init__(self, name, phone_number, timestamp, reason):
        self.unique_id = uuid.uuid4()
        self.name = name
        self.phone_number = phone_number
        self.timestamp = timestamp
        self.reason = reason
    def display(self):
        print 'Call Attributes:'
        print 'Unique ID:', self.unique_id
        print 'Call Time:', self.timestamp
        print 'Caller Name:', self.name
        print 'Phone Number:', self.phone_number
        print 'Reason for Call:', self.reason
        print ''

# CallCenter Class
class CallCenter(object):
    def __init__(self, *calls):
        self.calls = []
        for each in calls:
            self.calls.append(each)
        self.resizeQueue()
    def resizeQueue(self):
        self.queue_size = len(self.calls)
        return self
    def add(self, call):
        if isinstance(call, Call):
            self.calls.append(call)
            self.resizeQueue()
        return self
    def remove(self):
        self.calls.pop(0)
        self.resizeQueue()
        return self
    def info(self):
        print 'Queue Length:', str(self.queue_size)
        for each in range(0, self.queue_size):
            print str(each + 1) + ': ' + (self.calls[each].name + ' ' +
                                          self.calls[each].phone_number)

amanda = Call('Amanda', '2065556575', '13.45', 'there is fluoride in the water')
bernard = Call('Bernard', '1111111111', '0838', 'i lost my cat')
carol = Call('Carol', '7777777777', '1856', 'the walls are blue not green')
dillon = Call('Dillon', '9999999999', '1626', 'the dishes are in the sink')

amanda.display()
bernard.display()

best_call_center_ever = CallCenter(amanda, bernard, carol, dillon)
best_call_center_ever.info()
best_call_center_ever.remove()
best_call_center_ever.info()
best_call_center_ever.add(amanda)
best_call_center_ever.info()
