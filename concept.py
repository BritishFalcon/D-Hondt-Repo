from operator import attrgetter

class Party():
    
    def __init__(self, Votes, Candidates):
        self.StartVotes = int(Votes)
        self.Candidates = Candidates

        self.NewVotes = self.StartVotes
        self.Seats = 0

    def seatwon(self):
        self.Seats += 1
        self.NewVotes = int(self.StartVotes / (self.Seats + 1))
        
        return self.Candidates.pop()

BrexitParty = Party("452321", ["BP5","BP4","BP3","BP2","BP1"])
LiberalDemocrats = Party("203989",["LD5","LD4","LD3","LD2","LD1"])
Labour = Party("164682", ["LAB5","LAB4","LAB3","LAB2","LAB1"])
Conservative = Party("126138", ["CON5","CON4","CON3","CON2","CON1"])
Green = Party("124630", ["GR5","GR4","GR3","GR2","GR1"])
UKIP = Party("58198", ["UKP5","UKP4","UKP3","UKP2","UKP1"])
ChangeUK = Party("41117", ["CUK5","CUK4","CUK3","CUK2","CUK1"])
IndependentNetwork = Party("7641", ["INET5","INET4","INET3","INET2","INET1"])
Independent = Party("4511", ["IND5","IND4","IND3","IND2","IND1"])



PartyList = [BrexitParty, LiberalDemocrats, Labour, Conservative, Green, UKIP, ChangeUK, IndependentNetwork, Independent]
CandList = []

for Seat in range(1,6):
    WinningParty = max(PartyList, key=attrgetter("NewVotes"))
    print(eval("WinningParty.seatwon()"))
