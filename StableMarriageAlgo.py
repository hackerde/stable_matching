class male:
    def __init__(self, name):
        self.name = name
        self.PList = []
        self.CurrentChoice = ""
    def crossout(self):
        self.PList.pop(0)
        self.CurrentChoice = self.PList[0]
    def propose(self, other):
        other.CurrentSuitors.append(self)
    def setPList(self, a, b, c):
        self.PList = [a, b, c]
        self.CurrentChoice = self.PList[0]
    
class female:
    def __init__(self, name):
        self.name = name
        self.PList = []
        self.CurrentSuitors = []
    def reject(self, other):
        other.crossout()
    def setPList(self, a, b, c):
        self.PList = [a, b, c]

#main

Tim = male("Tim")
Nate = male("Nate")
George = male("George")
Anna = female("Anna")
Kim = female("Kim")
Kate = female("Kate")

Tim.setPList(Kate, Anna, Kim)
Nate.setPList(Kate, Anna, Kim)
George.setPList(Kate, Anna, Kim)
Anna.setPList(Nate, Tim, George)
Kim.setPList(Nate, Tim, George)
Kate.setPList(Nate, Tim, George)

boys = [Tim, Nate, George]
girls = [Anna, Kim, Kate]

def check(girls):
    for girl in girls:
        if not(girl.CurrentSuitors):
            return 0
    return 1

counter = 1
while not(check(girls)):
    print "\nDay", counter, "\n"
    for boy in boys:
        boy.propose(boy.CurrentChoice)
        print boy.name, "proposes", boy.CurrentChoice.name
    print
    for girl in girls:
        for person in girl.PList:
            if person in girl.CurrentSuitors:
                for guy in girl.CurrentSuitors:
                    if guy!=person:
                        girl.reject(guy)
                        print girl.name, "rejects", guy.name
                girl.CurrentSuitors = [person]
                break
    counter+=1

print "So finally...\n"
print "Anna marries", Anna.CurrentSuitors[0].name
print "Kate marries", Kate.CurrentSuitors[0].name
print "Kim marries", Kim.CurrentSuitors[0].name
