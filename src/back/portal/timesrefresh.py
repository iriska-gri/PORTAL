from datetime import datetime

def time_until_end_of_day(dt=None):
    if dt is None:
        dt = datetime.now()
    return ((24 - dt.hour - 1) * 60 ) + ((60 - dt.minute - 1)) 
    
 