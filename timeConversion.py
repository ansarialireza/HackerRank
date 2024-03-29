

def timeConversion(time):
    
    hh=time[:2]
    mm=time[3:5]
    ss=time[6:8]
    am_pm=time[8:11]
    
    if am_pm =='AM':
        hh=int(hh)
        if hh==12:
            hh-=12
        hh=str(hh)
        hh='0'+hh


    elif am_pm =='PM':
        hh=int(hh)
        if hh !=12:
            hh+=12
        hh=str(hh)
    time=hh + ':' + mm + ':' + ss
    return time

    


# time='07:05:45PM'
time='12:05:45AM'
new_time=timeConversion(time)
print(new_time)
