from tools.fonctions import *
from tools.filesConfig import *

class Commutation():
    def __init__(self,sex,client_age_last_birthday,Adj_disc_R,Guar_period,H_frame,F_frame):
        self.sex=sex        
        self.client_age_last_birthday=client_age_last_birthday
        self.Adj_disc_R=Adj_disc_R
        self.Guar_period=Guar_period
        self.H_frame=H_frame
        self.F_frame=F_frame
        
    def Male_table(self):
        global vtpx
        age=self.H_frame.iloc[which(self.H_frame.age==77):,0]
        qx=self.H_frame.iloc[which(self.H_frame.age==77):,1]
        px=1-qx
        tpx=px.cumprod()
        vtpx=(1+self.Adj_disc_R)**(-(age-self.Adj_disc_R+1-tpx))*tpx
        return pd.DataFrame({'age':age,'qx':qx,'px':px,'tpx':tpx,'vtpx':vtpx})
    
    def Female_table(self):
        global tpx
        age=self.F_frame.iloc[which(self.F_frame.age==67):,0]
        qx=self.F_frame.iloc[which(self.F_frame.age==67):,1]
        px=1-qx
        tpx=px.cumprod()
        return pd.DataFrame({'age':age,'qx':qx,'px':px,'tpx':tpx})
    
    def ax(self):
        return vtpx.sum()+1
    
    def gpx(self):
        if self.Guar_period==0 :
            return 1
        else :
            a=tpx.reset_index(drop=True)
            print(a)
        return a[9]


# A=Commutation('M',67,0.1125,10,Male,Female)
# A.Male_table()
# A.Female_table()
# A.ax()
# A.gpx()
