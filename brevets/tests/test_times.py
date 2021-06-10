import acp_times
import nose   # testing framework
import arrow
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

bday = arrow.get('03/28/2000 T00:00', 'MM/DD/YYYY THH:mm') #arbitrary date



def test_starting_close_time(): #checks 1 hour added to start close time
    print("ans: ", bday)

    ans = bday.shift(hours=9) # +8 more than expected to account for a shift in acp_times.py
    #ans = bday.shift(hours=8) # +8 to account for the timeshift in acp_times.py
    ans = ans.isoformat()
    print("ans: ", ans)
    print("what calc is returning: ",acp_times.close_time(0, 200, bday) )

    assert acp_times.close_time(0, 200, bday) == ans

def test_starting_open_time(): # checks start time to be the same
    ans = bday.shift(hours=8)
    ans = ans.isoformat()

    assert acp_times.open_time(0, 200, bday) == ans

def test_starting_open_time1(): # checks open time for large control dist
    ans = bday.shift(hours=37, minutes=9)
    ans = ans.isoformat()
    
    assert acp_times.open_time(890, 1000, bday) == ans

def test_difclosetime(): # checks close time for short  control dist
    ans = bday.shift(hours=18)
    ans = ans.isoformat()
    print("ans: ", ans)
    print("what calc is returning: ",acp_times.close_time(150, 1000, bday) )
    #print("is same?", acp_times.close_time(60, 200, bday) == ans)
    assert acp_times.close_time(150, 1000, bday) == ans

def test_close_time2():
    ans = bday.shift(hours=39, minutes=20)
    ans = ans.isoformat()
    print("ans: ", ans)
    print("what calc is returning: ",acp_times.close_time(470, 1000, bday) )
    print("is same?", acp_times.close_time(470, 1000, bday) == ans, "\nans: ",ans, "\nwhat I'm returning: ",acp_times.close_time(470, 1000, bday) )


    assert acp_times.close_time(470, 1000, bday) == ans
