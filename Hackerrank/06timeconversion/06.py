def timeConversion(s):

    hours, minutes, seconds = map(int, s[:-2].split(':'))
  
    if 'PM' in s and hours != 12:
        hours += 12
   
    if 'AM' in s and hours == 12:
        hours = 0
    
    military_time = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
    return military_time


sample_input = input()
print(timeConversion(sample_input)) 
