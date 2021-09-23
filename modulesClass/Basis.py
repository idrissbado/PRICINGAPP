from tools.fonctions import *
from tools.filesConfig import *

class Basis():
    def __init__(self,MarketGrossyieldRate,
                 ReinvestmentRiskMargin,PrudentMargin,Tax,
                 AnnuityFreq,Expl_Inf_Rate,Enterpremiun,PremiumBreak1,
                 aun,PremiumBreak2,adeux,atrois,WritingAgentCommission,UnitManagerComm,
                 AgencyManagerComm,RegionalManagerComm,DeputyNationalManager,
                 NationalManagerComm,Illiquiditymargin,Profitcriterion):
        self.MarketGrossyieldRate=MarketGrossyieldRate
        self.ReinvestmentRiskMargin=ReinvestmentRiskMargin
        self.PrudentMargin=PrudentMargin
        self.Tax=Tax
        self.AnnuityFreq=AnnuityFreq
        self.Expl_Inf_Rate=Expl_Inf_Rate
        self.Enterpremiun=Enterpremiun
        self.PremiumBreak1=PremiumBreak1
        self.aun=aun
        self.PremiumBreak2=PremiumBreak2
        self.adeux=adeux
        self.atrois=atrois
        self.WritingAgentCommission=WritingAgentCommission
        self.UnitManagerComm=UnitManagerComm
        self.AgencyManagerComm=AgencyManagerComm
        self.RegionalManagerComm=RegionalManagerComm
        self.DeputyNationalManager=DeputyNationalManager
        self.NationalManagerComm=NationalManagerComm
        self.Illiquiditymargin=Illiquiditymargin
        self.Profitcriterion=Profitcriterion
    
    def PricingGrossYieldRate(self):
        global PricingGrossYieldRate
        PricingGrossYieldRate=self.MarketGrossyieldRate-self.ReinvestmentRiskMargin-self.PrudentMargin-self.Tax
        return  PricingGrossYieldRate
    
    def Mthlyconvertibleinvestmentreturnrate(self):
        return ((1+PricingGrossYieldRate)**(1/self.AnnuityFreq)-1)
    
    def AdjustedInflationRate(self):
        global AdjustedInflationRate
        AdjustedInflationRate=(1+ PricingGrossYieldRate)/(1+ self.Expl_Inf_Rate)-1
        return AdjustedInflationRate
    
    def Monthlyconvertibleadjustedinterestrate(self):
        return (((1+AdjustedInflationRate)**(1/self.AnnuityFreq)-1))
    
    def MortalityLoadingAdjustment(self):
        if self.Enterpremiun<self.PremiumBreak1:
            return(self.aun)
        elif  self.Enterpremiun<self.PremiumBreak2:
            return(self.adeux)
        else:
            return(self.atrois)
    
    def Commissionrate(self):
        global Commissionrate
        Commissionrate=self.WritingAgentCommission*(1+self.UnitManagerComm+self.AgencyManagerComm+self.RegionalManagerComm+self.DeputyNationalManager+self.NationalManagerComm)
        return Commissionrate
    def Naicomlevy(self):
        global Naicomlevy
        Naicomlevy=0.01*(1-Commissionrate)
        return Naicomlevy
        
    def ProfitandContigencyMargin(self):
        ProfitandContigencyMargin=Naicomlevy+self.Illiquiditymargin+self.Profitcriterion
        return  ProfitandContigencyMargin
        

# A=Basis(MarketGrossyieldRate=0.12,ReinvestmentRiskMargin=0.005,PrudentMargin=0.0025,Tax=0,
#         AnnuityFreq=12,Expl_Inf_Rate=0.08,Enterpremiun=2000000,PremiumBreak1=5000000,aun=0,
#         PremiumBreak2=10000000,adeux=-1,atrois=-3,WritingAgentCommission=0.03,
#         UnitManagerComm=0.075,AgencyManagerComm=0.05,RegionalManagerComm=0.03,
#         DeputyNationalManager=0.018,NationalManagerComm=0.022,Illiquiditymargin=0,
#         Profitcriterion=0.04)

# print(A.PricingGrossYieldRate())
# print(A.Mthlyconvertibleinvestmentreturnrate())
# print(A.AdjustedInflationRate())
# print(A.Monthlyconvertibleadjustedinterestrate())
# print(A.MortalityLoadingAdjustment())
# print(A.Commissionrate())
# print(A.Naicomlevy())
# print(A.ProfitandContigencyMargin())
 