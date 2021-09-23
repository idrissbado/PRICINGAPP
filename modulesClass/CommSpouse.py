from tools.fonctions import *
from tools.filesConfig import *

class CommSpouse():
    def __init__(self,sex,client_age_last_birthday,Adj_disc_R,Guar_period,H_frame,F_frame):
        self.sex=sex        
        self.client_age_last_birthday=client_age_last_birthday
        self.Adj_disc_R=Adj_disc_R
        self.Guar_period=Guar_period
        self.H_frame=H_frame
        self.F_frame=F_frame
        
    def table(self):
        global vtpxy
        global vtpy
        if self.sex=="M":
            age=self.H_frame.iloc[which(self.H_frame.age==67):,0]
            qx=self.H_frame.iloc[which(self.H_frame.age==67):,1]
            qy=self.H_frame.iloc[which(self.H_frame.age==67):,1]
            px=1-qx
            py=1-qy
            pxy=px*py
            tpy=py.cumprod() 
            vtpy=(1+self.Adj_disc_R)**(-(age-self.Adj_disc_R+1-tpy))*tpy
            tpxy=pxy.cumprod()
            tpx=px.cumprod()
            vtpxy=(1+self.Adj_disc_R)**(-(age-self.Adj_disc_R+1-tpxy))*tpxy
            return pd.DataFrame({'age':age,'qx':qx,'qy':qy,'px':px,'py':py,'pxy':pxy,'tpy':tpy,'tpx':tpx,'vtpy':vtpy,'tpxy':tpxy,'vtpxy':vtpxy})
        else :
            age=self.F_frame.iloc[which(self.F_frame.age==67):,0]
            qx=self.F_frame.iloc[which(self.F_frame.age==67):,1]
            qy=self.F_frame.iloc[which(self.F_frame.age==67):,1]
            px=1-qx
            py=1-qy
            pxy=px*py
            tpy=py.cumprod() 
            vtpy=(1+self.Adj_disc_R)**(-(age-self.Adj_disc_R+1-tpy))*tpy
            tpxy=pxy.cumprod()
            tpx=px.cumprod()
            vtpxy=(1+self.Adj_disc_R)**(-(age-self.Adj_disc_R+1-tpxy))*tpxy
            vtpx=(1+self.Adj_disc_R)**(-(age-self.Adj_disc_R+1-tpx))*tpx
        return pd.DataFrame({'age':age,'qx':qx,'qy':qy,'px':px,'py':py,'pxy':pxy,'tpy':tpy,'tpx':tpx,'vtpy':vtpy,'tpxy':tpxy,'vtpxy':vtpxy})
    
    def axy(self):
        global axy
        self.table()
        print(self.table())
        axy=vtpxy.sum()+1
        return axy
    
    def ay(self):
        global ay
        self.table()
        print(self.table())
        ay=vtpy.sum()+1
        return ay
    
    def ax_y(self):
        self.table()
        self.axy()
        self.ay()
        return ay-axy
    
    
# A=CommSpouse('M',67,0.1125,10,Male,Female)
# A.ax_y()
    
