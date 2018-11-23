# Longest Collatz sequence
# Finding a number under a start_num n that produces the longest chain?
import time
_start_time = time.time()
_start_num = 10**6


def term_counter(_temp):
	_term_count = 1
	while _temp > 1:
		_term_count += 1 
		_temp = _temp/2 if _temp%2==0 else 3*_temp+1
	return _term_count

if __name__ == '__main__':
	_max_count = 0
	_target_num = 0
	while _start_num > 1:
		length_count = 0
		print 'Working on number %d ' % (_start_num)
		_term_count = term_counter(_start_num)
		if _term_count > _max_count:
			_max_count =  _term_count
			_target_num = _start_num
		_start_num -= 1
	print 'Search completed with max count @ %d  starting number %d ' % (_max_count,_target_num)
	print 'Computed in %f ' % (time.time()-_start_time)	


