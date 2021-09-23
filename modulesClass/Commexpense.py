from tools.fonctions import *
from tools.filesConfig import *

class Commexpense():
    def __init__(self,sex,client_age_last_birthday,Adj_Inf_Disc_Rat,Guar_period,H_frame,F_frame):
        self.sex=sex        
        self.client_age_last_birthday=client_age_last_birthday
        self.Adj_Inf_Disc_Rat=Adj_Inf_Disc_Rat
        self.Guar_period=Guar_period
        self.H_frame=H_frame
        self.F_frame=F_frame
        
    def table(self):
        global vtpx
        if self.sex=="M":
            age=self.H_frame.iloc[which(self.H_frame.age==67):,0]
            qx=self.H_frame.iloc[which(self.H_frame.age==67):,1]
            px=1-qx
            tpx=px.cumprod()
            vtpx=(1+self.Adj_disc_R)**(-(age-self.Adj_disc_R+1-tpx))*tpx
            return pd.DataFrame({'age':age,'qx':qx,'tpx':tpx,'vtpx':vtpx})
        else :
            age=self.F_frame.iloc[which(self.F_frame.age==67):,0]
            qx=self.F_frame.iloc[which(self.F_frame.age==67):,1]
            px=1-qx
            tpx=px.cumprod()
            vtpx=(1+self.Adj_disc_R)**(-(age-self.Adj_disc_R+1-tpx))*tpx
        return pd.DataFrame({'age':age,'qx':qx,'tpx':tpx,'vtpx':vtpx})
    
    def ax(self):
        print(self.table())
        return vtpx.sum()+1
    

# B=Commexpense('M',67,0.03,10,Male,Female)
# B.ax()
