class convert_temp():
    def __init__(self,t):
        self.t=t
    def fc(self):
        f=self.t
        c=(f-32)*5/9
        print(f'{f} Fahrenheit is {c} Celsius.')
    def cf(self):
        c=self.t
        f=(c*9/5)+32
        print(f'{c} Celsius is {f} Fahrenheit.')
    def fk(self):
        f=self.t
        k=(f+459.67)*5/9
        print(f'{f} Fahrenheit is {k} Kelvin.')
    def kf(self):
        k=self.t
        f=(k*9/5)-459.67
        print(f'{k} Kelvin is {f} Fahrenheit.')
    def fr(self):
        f=self.t
        r=f+459.67
        print(f'{f} Fahrenheit is {r} Rankine.')
    def rf(self):
        r=self.t
        f=r-459.67
        print(f'{r} Rankine is {f} Fahrenheit.')
    def ck(self):
        c=self.t
        k=c+273.15
        print(f'{c} Celsius is {k} Kelvin.')
    def kc(self):
        k=self.t
        c=k-273.15
        print(f'{k} Kelvin is {c} Celsius.')
    def kr(self):
        k=self.t
        r=k*9/5
        print(f'{k} Kelvin is {r} Rankine.')
    def rk(self):
        r=self.t
        k=r*5/9
        print(f'{r} Rankine is {k} Kelvin.')
    def rc(self):
        r=self.t
        c=(r-491.67)*5/9
        print(f'{r} Rankine is {c} Celsius.')
    def cr(self):
        c=self.t
        r=(c+273.15)*9/5
        print(f'{c} Celsius is {r} Rankine.')   
        
class convert_length:
    
    def __init__(self,l):
        self.l=l
    def m_cm(self):
        m=self.l
        cm=m*100
        print(f'{m} meter is {cm} centimeter.')
    def m_mm(self):
        m=self.l
        mm=m*1000
        print(f'{m} meter is {mm} milimeter.')
    def cm_m(self):
        cm=self.l
        m=cm*0.01
        print(f'{cm} centimeter is {m} meter.')
    def mm_m(self):
        mm=self.l
        m=mm*0.001
        print(f'{mm} milimeter is {m} meter.')
    def m_ft(self):
        m=self.l
        ft=m*3.2808
        print(f'{m} meter is {ft} feet.')
    def ft_m(self):
        ft=self.l
        m=ft/3.2808
        print(f'{ft} feet is {m} meter.')
    def inch_cm(self):
        inch=self.l
        cm=inch/0.3937
        print(f'{inch} inch is {cm} centimeter.')
    def cm_inch(self):
        cm=self.l
        inch=cm*0.3937
        print(f'{cm} centimeter is {inch} inch .')
    def mm_inch(self):
        mm=self.l
        inch=mm*0.03937
        print(f'{mm} milimeter is {inch} inch .')
    def inch_mm(self):
        inch=self.l
        mm=inch/0.03937
        print(f'{inch} inch  is {mm} milimeter.')

class convert_pressure:
    def __init__(self,p):
        self.p=p
    def bar_pascal(self):
        bar=self.p
        pascal=0.00001*bar
        print(f'{bar} bar is {p} pascal.')
    def pascal_bar(self):
        pascal=self.p
        bar=100000*pascal
        print(f'{pascal} pascal is {bar} bar.')
    def pascal_psi(self):
        pascal=self.p
        psi=6894.75*pascal
        print(f'{pascal} pascal is {psi} psi.')
    def psi_pascal(self):
        psi=self.p
        pascal=psi/6894.75
        print(f'{psi} psi is {pascal} pascal.')
        
def main():
    k=int(input('convert_temp=1 or convert_length=2 or convert_pressure=3:'))
    if k==1:
        t=float(input('Temprature='))
        s=int(input('fc:1,cf:2,fk:3,kf:4,rf:5,fr:6,ck:7,kc:8,kr:9,rk:10,rc:11,cr:12:'))
        convert=convert_temp(t)
        if s==1:
            convert.fc()
        elif s==2:
            convert.cf()
        elif s==3:
            convert.fk()
        elif s==4:
            convert.kf()
        elif s==5:
            convert.rf()
        elif s==6:
            convert.fr()
        elif s==7:
            convert.ck()
        elif s==8:
            convert.kc()
        elif s==9:
            convert.kr()
        elif s==10:
            convert.rk()
        elif s==11:
            convert.rc()
        elif s==12:
            convert.cr()
        else:
            print('wrong input. try again!')

    if k==2:
        l=float(input('Length='))
        s=int(input('m_cm:1,m_mm:2,cm_m:3,mm_m:4,m_ft:5,ft_m:6,inch_cm:7,cm_inch:8,mm_inch:9,inch_mm:10:'))
        convert=convert_length(l)
        if s==1:
            convert.m_cm()
        elif s==2:
            convert.m_mm()
        elif s==3:
            convert.cm_m()
        elif s==4:
            convert.mm_m()
        elif s==5:
            convert.m_ft()
        elif s==6:
            convert.ft_m()
        elif s==7:
            convert.inch_cm()
        elif s==8:
            convert.cm_inch()
        elif s==9:
            convert.mm_inch()
        elif s==10:
            convert.inch_mm()
        else:
            print('wrong input. try again!')
    if k==3:
        p=float(input('Pressure='))
        s=int(input('bar_pascal:1,pascal_bar:2,pascal_psi:3,psi_pascal:4:'))
        convert=convert_pressure(p)
        if s==1:
            convert.bar_pascal()
        elif s==2:    
            convert.pascal_bar()
        elif s==3:    
            convert.pascal_psi()
        elif s==4:    
            convert.psi_pascal()
        else:
            print('wrong input. try again!')
            
    w=input('do you want convert again?y/n:' )
    if w=='y':
         main()
            
main()        
        
