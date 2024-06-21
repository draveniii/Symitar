#Member Class
#Draven McConathy
#05/31/2024
#Contains information about the member in question including name, address, and date of birth

class Member:
    def __init__(self, name, address, dateOfBirth):
        self.memberName = name
        self.memberAddress = address
        self.memberDOB = dateOfBirth

    def get_memberName(self):
        return self.memberName 

    def get_memberAddress(self):
        return self.memberAddress

    def get_memberDOB(self):
        return self.memberDOB
    
    def change_memberName(self, newMemberName):
        self.memberName = newMemberName

    def change_memberAddress(self, newMemberAddress):
        self.memberAddress = newMemberAddress

