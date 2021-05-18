import acp_times.py
import nose
import arrow
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_starting_close_time(): #checks 1 hour added to start close time
    ans = arrow.now()
    ans = ans.shift(hours=1)
    ans = ans.format('YYYY-MM-DD THH:mm')

    assert acp_times.close_time(0, 200, arrow.now()) == ans

def test_starting_open_time(): # checks start time to be the same
    ans = arrow.now()
    ans = ans.format('YYYY-MM-DD THH:mm')
    assert acp_times.open_time(0, 200, arrow.now()) == ans

def test_starting_open_time1(): # checks open time for large control dist
    ans = arrow.now()
    ans = ans.shift(hours=29, minutes=9)
    ans = ans.format('YYYY-MM-DD THH:mm')

    assert acp_times.open_time(890, 1000, arrow.now()) == ans

def test_starting_close_time1(): # checks close time for short  control dist
    ans = arrow.now()
    ans = ans.shift(hours=5)
    ans = ans.format('YYYY-MM-DD THH:mm')

    assert acp_times.close_time(60, 200, arrow.now()) == ans

def test_starting_close_time2():
    ans = arrow.now()
    ans = ans.shift(hours=65, minutes=23)
    ans = ans.format('YYYY-MM-DD THH:mm')

    assert acp_times.open_time(890, 1000, arrow.now()) == ans