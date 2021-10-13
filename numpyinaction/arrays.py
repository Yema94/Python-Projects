import time
import numpy

start_time = time.time()

int_array = numpy.array([1, 2, 3, 4])
print(int_array)

char_array = numpy.array(['a', 'b', 'c'])
print(char_array)

string_array = numpy.array(["ich", "dich", "Yesh"])

time.sleep(3)
stop_time = time.time()
print("Elapsed time: ab {} bis {}".format(start_time, stop_time))
print(f"process finished in {stop_time - start_time} secs")
