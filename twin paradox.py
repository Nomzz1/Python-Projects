import math
def twins(age, distance, velocity):
	time = (distance*2)*1/velocity
	jill_age = age + time
	c = 299792458
	v = velocity*c
	dilated_time = time*(math.sqrt(1-((v**2)/(c**2))))
	jack_age = age + dilated_time
	print("Jack's age is",str(jack_age)+", Jill's age is",str(jill_age))
twins(20, 10, 0.4)