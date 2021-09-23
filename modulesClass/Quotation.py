class Quotation():
    def __init__(self,ApplicationDate,ClientDateofBirth,SpouseDateofBirth,Inv_Return,Escal_Rate,Adj_disc_R,AnnuityFreq,Annuity):
        self.ApplicationDate=ApplicationDate  # mettre en format date(année,mois,jour)
        self.ClientDateofBirth=ClientDateofBirth # mettre en format date(année,mois,jour)
        self.SpouseDateofBirth=SpouseDateofBirth # mettre en format date(année,mois,jour)
        self.Inv_Return=Inv_Return
        self.Escal_Rate=Escal_Rate
        self.Adj_disc_R=Adj_disc_R
        self.AnnuityFreq=AnnuityFreq
        self.Annuity=Annuity
    def ClientAgeLastBirthday(self):
        global ClientAgeLastBirthday
        ClientAgeLastBirthday=round((self.ApplicationDate-self.ClientDateofBirth).days/365)
        return ClientAgeLastBirthday
    def SpouseAgeLastBirthday(self):
        global SpouseAgeLastBirthday
        SpouseAgeLastBirthday=round((self.ApplicationDate-self.ClientDateofBirth).days/365)
        return SpouseAgeLastBirthday
    
    def SpouseAgeDifference(self):
        return SpouseAgeLastBirthday-ClientAgeLastBirthday
    
    def AdjustedDiscountRatetouse(self):
        return (1+ self.Inv_Return)/(1+self.Escal_Rate)-1
    
    def MonthlyAdjustedDiscountRatetouse(self):
        return (1+self.Adj_disc_R)**(1/self.AnnuityFreq)-1
    
    def ModalAnnuity(self):
        return self.Annuity
    

# B=Quotation(ApplicationDate=date(2021,6,18),ClientDateofBirth=date(1953,8,24)
# ,SpouseDateofBirth=date(1953,8,24),Inv_Return=0.1125
# ,Escal_Rate=0,Adj_disc_R=0.1125
# ,AnnuityFreq=12,Annuity= 20594.50)

# print(B.ClientAgeLastBirthday())
# print(B.SpouseAgeLastBirthday())
# print(B.SpouseAgeDifference())
# print(B.AdjustedDiscountRatetouse())
# print(B.MonthlyAdjustedDiscountRatetouse())
# print(B.ModalAnnuity())


