import numpy_financial as npf
fv=15692.93
rate=0.05/12
nper=10*12
pmt=-100
pv=npf.pv(rate,nper,pmt,fv)
print('pv is :',pv)
print('fv is :',npf.fv(rate,nper,pmt,pv))
print('rate is :',npf.rate(nper,pmt,pv,fv))
print('nper is :',npf.nper(rate,pmt,pv,fv))
print('pmt is :',npf.pmt(rate,nper,pv,fv))
