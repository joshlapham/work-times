#!/usr/bin/python

import datetime
from work_times_mysql import record_time
    
def main():
    # Monday
    mon_start = datetime.datetime(2017, 01, 30, 8, 30, 00)
    mon_end = datetime.datetime(2017, 01, 30, 16, 00, 00)
    mon_total = mon_end - mon_start
    
    # Tuesday
    tue_start = datetime.datetime(2017, 01, 31, 9, 00, 00)
    tue_end = datetime.datetime(2017, 01, 31, 17, 00, 00)
    tue_total = tue_end - tue_start
    
    # Wednesday
    wed_start = datetime.datetime(2017, 02, 01, 9, 30, 00)
    wed_end = datetime.datetime(2017, 02, 01, 17, 30, 00)
    wed_total = wed_end - wed_start
    
    # Thursday
    thu_start = datetime.datetime(2017, 02, 02, 9, 00, 00)
    thu_end = datetime.datetime(2017, 02, 02, 17, 00, 00)
    thu_total = thu_end - thu_start
    
    # Friday
    fri_start = datetime.datetime(2017, 02, 03, 9, 00, 00)
    fri_end = datetime.datetime(2017, 02, 03, 15, 30, 00)
    fri_total = fri_end - fri_start
    
    # TOTAL
    total = mon_total + tue_total + wed_total + thu_total + fri_total
    seconds = total.total_seconds()
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    print '{} hours, {} minutes'.format(hours, minutes)
    
    # Record in SQL database
    # record_time(mon_start, mon_end)
    # record_time(tue_start, tue_end)
    # record_time(wed_start, wed_end)
    # record_time(thu_start, thu_end)
    # record_time(fri_start, fri_end)
    
if __name__ == '__main__':
    # TODO: pass args
    main()
