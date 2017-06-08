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
        self.call_list = []
        for each in calls:
            self.call_list.append(each)
        self.resizeQueue()
    def resizeQueue(self):
        self.queue_size = len(self.call_list)
        return self
    def add(self, call):
        if isinstance(call, Call):
            self.call_list.append(call)
            self.resizeQueue()
        return self
    def remove(self):
        self.call_list.pop(0)
        self.resizeQueue()
        return self
    def info(self):
        print 'Queue Length:', str(self.queue_size)
        for each in range(0, self.queue_size):
            print str(each + 1) + ': ' + (self.call_list[each].name + ' ' +
                                          self.call_list[each].phone_number)
        return self

    # Ninja Level
    # Add a method to the call center class that can find and remove a call from
    # the queue according to the phone number of the caller.
    def removeThisCall(self, this_phone_number):
        for each in range(0, self.queue_size):
            if this_phone_number == self.call_list[each].phone_number:
                self.call_list.pop(each)
                self.resizeQueue()
                # DON'T FORGET TO BREAK OUT OF THE LOOP (EACH STOPS EXISTING)
                return self
        return self

    # Hacker Level
    # Add a method to the call center that sorts the calls in the queue
    # according to time of call in ascending order.
    def sortQueue(self):
        self.call_list.sort(key=lambda x: x.timestamp, reverse=False)

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
# Test Ninja Level
best_call_center_ever.removeThisCall('9999999999')
best_call_center_ever.info()
# Test Hacker Level
best_call_center_ever.sortQueue()
best_call_center_ever.info()