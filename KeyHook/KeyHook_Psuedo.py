#psuedo code for KeyHook.py
'''
database serialize use's data

keys are issues by buildings
employees can make request for key
each request records room access and identity of employee
keys may be returned and rerequested

each emplyee has an id number
track each key with who and when request was made (time and date)
room has a unique number within each bulding
there are at least one door per room with a name

room access key is a copy of a master
master is called a hook
each hook has a unique number
each hook may open several doors
when keys are returned the same key may be issued to another employee
when a key is lost record and charge employee $25
make sure that we never issue a key unless it has been requested
make sure that we never issue two keys to the same employee that are the same hook
'''

# this program is a database for a key management system
# it uses the following classes:
# Employee
#    id
#    name
#    department
# 
# Department
#    id
#    name
#    building
#
# Room
#    number
#    name
#    building
#    door
#
# Key
#    number
#    hook
#    room
#    employee
#    date
#    time
#    returned
#    lost
#    lost charge
#
# Hook
#    number
#    room
#    door
#
# KeyRequest
#    employee
#    room
#    date
#    time
#    key
#
# KeyReturn
#    employee
#    key
#    date
#    time
#
# KeyLost
#    employee
#    key
#    date
#    time
#    charge
#
# KeyIssue
#    employee
#    key
#    date
#    time
#    status