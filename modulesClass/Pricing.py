class Pricing():
    def __init__(self,Adj_disc_R,Guar_period,
                 M_Adj_Disc_R,gpx,ax_commutation,annuity_freq,
                 Var_Expperannuity,ax_comexp,Rend_fix_exp,ax_h,
                 Initial_Expense,Profit_Mar,
                 Quote_Required1,Quote_Required2,Premium,spouse_option,comm_Rate):
        
        self.Adj_disc_R=Adj_disc_R
        self.Guar_period=Guar_period
        self.M_Adj_Disc_R=M_Adj_Disc_R
        self.gpx=gpx
        self.ax_commutation=ax_commutation
        self.annuity_freq=annuity_freq
        self.Var_Expperannuity=Var_Expperannuity
        self.ax_comexp=ax_comexp
        self.Rend_fix_exp=Rend_fix_exp
        self.ax_h=ax_h
        self.Initial_Expense=Initial_Expense
        self.Profit_Mar=Profit_Mar
        self.spouse_option=spouse_option
        self.Quote_Required1=Quote_Required1
        self.Quote_Required2=Quote_Required2
        self.Premium=Premium
        self.comm_Rate=comm_Rate
        
    def PV_Liability(self):
        global pv_Liability
        pv_Liability=((1-(1+self.Adj_disc_R)**(-self.Guar_period))/(self.M_Adj_Disc_R/(1+self.M_Adj_Disc_R))/self.annuity_freq+((1+self.Adj_disc_R)**(-self.Guar_period)*self.gpx*(self.ax_commutation-((self.annuity_freq-1)/(2*self.annuity_freq)))))
        return pv_Liability
                
    def Expense_Liability(self):
        global expense_Liability
        expense_Liability=self.Var_Expperannuity*(self.ax_comexp-((self.annuity_freq-1)/(2*self.annuity_freq)))
        return  expense_Liability
    
    def Expense_Renewal_Liability(self):
        global expense_Renewal_Liability
        expense_Renewal_Liability=self.Rend_fix_exp*(self.ax_comexp-((self.annuity_freq-1)/(2*self.annuity_freq)))
        return expense_Renewal_Liability
    
    def PV_Spouse_Annuity(self):
        global pv_Spouse_Annuity
        pv_Spouse_Annuity=self.ax_h-(((self.annuity_freq-1)/(2*self.annuity_freq)))
        return pv_Spouse_Annuity
    
    def Expenses_during_spouse_annuity(self):
        global expenses_during_spouse_annuity
        expenses_during_spouse_annuity=self.Var_Expperannuity*pv_Spouse_Annuity+self.Rend_fix_exp*pv_Spouse_Annuity
        return expenses_during_spouse_annuity

    def Annuity(self):
        if self.Quote_Required2==self.Quote_Required2:
            return (self.Premium*(1-self.Profit_Mar-self.comm_Rate)-self.Initial_Expense-expense_Liability)/((pv_Liability+self.spouse_option*pv_Spouse_Annuity+expense_Liability)*self.annuity_freq)
        else:
            return (self.Premium*self.annuity_freq*(pv_Liability+expense_Liability+self.spouse_option*pv_Spouse_Annuity)+self.Initial_Expense+expense_Renewal_Liability)/(1-self.Profit_Mar-self.comm_Rate)
        
# A=Pricing(Adj_disc_R=0.1125,
#           Guar_period=10,
#           M_Adj_Disc_R=0.0089, 
#           gpx=0.627238, 
#           ax_commutation=5.066061706,
#           annuity_freq=12 ,
#           Var_Expperannuity=0 ,
#           ax_comexp=10.743902 ,
#           Rend_fix_exp=5000 ,
#           Initial_Expense=5000,
#           Profit_Mar=0.0137915,
#           comm_Rate=0.04,
#           spouse_option=0,
#           ax_h=1.202,
#           Quote_Required1='From Premium to Annuity',
#           Quote_Required2='From Premium to Annuity',
#           Premium=2000000)



# print(A.PV_Liability())
# print(A.Expense_Liability())
# print(A.Expense_Renewal_Liability())
# print(A.PV_Spouse_Annuity())
# print(A.Expenses_during_spouse_annuity())
# print(A.Annuity())