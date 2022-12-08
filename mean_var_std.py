import numpy as np

def calculate(list):
   
  if len(list)<9:
    raise ValueError("List must contain nine numbers.") 
  else:
    pass
        
  a=np.array(list)
  print(a)
  aa=a.mean()
  
  print('================')
  bb=a.var()
  b=a.sum()
  c=a.std()
  cc=a.max()
  dd=a.min()
  

  z=a.copy().reshape((3, 3))
  print(z)
  onev=z[:3,0]
  twov=z[:3,1]
  threev=z[:3,2]
  print(threev)
  oneh=z[0,:3]
  twoh=z[1,:3]
  threeh=z[2,:3]
  print(threeh)
  print(onev.sum())
 # info=[]
#info.append(aa)
 # print(info)
  inf=[]
  m=onev.mean()
  mm=twov.mean()
  mmm=threev.mean()
  inf.append(m)
  inf.append(mm)
  inf.append(mmm)
  print(inf)
  info=[]
  mh=oneh.mean()
  mmh=twoh.mean()
  mmmh=threeh.mean()
  info.append(mh)
  info.append(mmh) 
  info.append(mmmh)
  meann=[]
  meann.append(inf)
  meann.append(info)
  meann+=[aa]
  print(meann)
    
  varr=[]
  varv=[]
  varh=[]
  vv=onev.var()
  vvv=twov.var()
  vvvv=threev.var()
  varv.extend([vv,vvv,vvvv])
  vh=oneh.var()
  vvh=twoh.var()
  vvvh=threeh.var()
  varh.extend([vh,vvh,vvvh])
  varr.append(varv)
  varr.append(varh)
  varr+=[bb]
    
  stdd=[]
  stdv=[]
  stdh=[]

  sv=onev.std()
  ssv=twov.std()
  sssv=threev.std()
  stdv.extend([sv,ssv,sssv])

  sh=oneh.std()
  ssh=twoh.std()
  sssh=threeh.std()
  stdh.extend([sh,ssh,sssh])
  stdd.append(stdv)
  stdd.append(stdh)
  stdd+=[c]
    
  maxx=[]
  maxv=[]
  maxh=[]

  mxv=onev.max()
  mmxv=twov.max()
  mmmxv=threev.max()
  maxv.extend([mxv,mmxv,mmmxv])

  mxh=oneh.max()
  mmxh=twoh.max()
  mmmxh=threeh.max()
  maxh.extend([mxh,mmxh,mmmxh])
 
  maxx.append(maxv)
  maxx.append(maxh)
  maxx+=[cc]

  minn=[]
  minv=[]
  minh=[]
    
  miv=onev.min()
  mmiv=twov.min()
  mmmiv=threev.min()
  minv.extend([miv,mmiv,mmmiv])
    
  mih=oneh.min()
  mmih=twoh.min()
  mmmih=threeh.min()
  minh.extend([mih,mmih,mmmih])
  minn.extend([minv,minh])
  minn+=[dd]
         
  summ=[]
  sumv=[]
  sumh=[]       
  suv=onev.sum()
  ssuv=twov.sum()
  sssuv=threev.sum()
  sumv.extend([suv,ssuv,sssuv])     
  suh=oneh.sum()
  ssuh=twoh.sum()
  sssuh=threeh.sum()
  sumh.extend([suh,ssuh,sssuh])
         
  summ.extend([sumv,sumh])
  summ+=[b]
  top= {
  'mean':meann,
  'variance':varr ,
  'standard deviation': stdd,
  'max':maxx,
  'min': minn,
  'sum': summ,
          }

  print(top)
