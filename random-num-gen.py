import datetime #lets try later with zero imports.

#tryting to make a random num gen without a pre-made random lib

def rand_date_time():
    now = datetime.datetime.now()
    date_int = int(now.strftime('%d%m%y'))
    time_int = int(now.strftime('%H%M'))
    var_name = date_int / time_int 
    return var_name[0]
  
print(rand_date_time())
