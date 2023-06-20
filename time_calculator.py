

def add_time(x,y,r='no'):
    v=x.split(' ')
    z=y.split(':')
    s=v[0].split(':')
    y=v[1]
    t1 = int(s[0]) + int(z[0])
    t2 =  int(s[1]) + int(z[1])
    h=0
    g=''
    if t2 > 60:
        t2=t2 - 60
        h += 1
    
    if len(str(t2)) == 1 :
        g = '0'
    
    days = ['monday','tuesday','wednsday','thursday','friday','saturday','sunday']
    p=''
    
    f = ""
    m = 0
    at = int(s[0]) + h

    t1 = t1 + h

    
    
      
    for i in x,y:
       
        while t1>=12:
           

            
        
            if t1>=12 and y == 'AM':
               t1= t1-12
               y = 'PM'
            elif t1>= 12 and y == 'PM':
               t1= t1-12
               y = 'AM'
               m+=1

     
    if m == 0:
        d=''
    elif m == 1:
        d='(next day)'
    elif m > 1:
        d=f'({int(m)}days later)'
    
    try:
        r = r.lower()
    except:
        r='?'

    nd = ''
    


    if r in days:

        f =  days.index(r)
        nd = f + m
        if nd > 6:
            nd = nd -6
    
    
    

    try:
       days[nd]=days[nd].capitalize()
       p = f',{days[nd]}'
    except:
       p=''

       
    
    if t1 == 0:
        t1 = 12
       
    
        
    
    return print(str(t1)+':'+g+str(t2)+' '+y+p+' '+d)

add_time("10:10 PM", "3:30")
    
    

    
    
