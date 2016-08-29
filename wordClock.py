# word clock.

# imports
import time
import cv2

# version 1.0

# Database for converting numbers to word for displaying sake.
# This data base is not used for the actual displaying.
hr2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
            11: 'Eleven', 12: 'Twelve'}
# For print purpose
min2words = {1: "O'clock", 2: 'Five past', 3: 'Ten past', 4: 'Quarter past', 5: 'Twenty past', 
             6: 'Twenty five past', 7: 'Half past', 8: 'Twenty Five Minutes to', 9: 'Twenty Minutes to', 10: 'Quarter to', 
            11: 'Ten Minutes to', 12: 'Five Minutes to'}

# funtion for converting number to words
# The above lists are reffered for the convertion
# and returned to the calling variable.
def hours2words(x_hour,x_min):
	if x_min>=30:
		if x_hour==12:
			x_hour=0
			x_hour_word = hr2words[x_hour+1];
		else:
			x_hour_word = hr2words[x_hour]
	else:
		x_hour_word = hr2words[x_hour]
	return x_hour_word   

# funtion for converting 24 hours format 
# to 12 hours format
def twentyfourTwelve(x_hour):
	if x_hour > 12:
		x_hour = x_hour-12
	return x_hour

# get mintues in words
# x_min_word = min2words[1]
# To display the respective word or worsd

def minutes2words(x_min,im_input,im_temp):
	if (1 <= x_min <5):
		x_min_word = min2words[1]
		im_temp = lightOclock(im_input,im_temp)
	elif (5<= x_min < 10):
		x_min_word = min2words[2]
		im_temp = lightFivepast(im_input,im_temp)
	elif (10<= x_min < 15):
		x_min_word = min2words[3]
		im_temp = lightTenpast(im_input,im_temp)
	elif (15<= x_min < 20):
		x_min_word = min2words[4]
		im_temp = lightQuarterpast(im_input,im_temp)
	elif (20<= x_min < 25):
		x_min_word = min2words[5]
		im_temp = lightTwentypast(im_input,im_temp)
	elif (25<= x_min < 30):
		x_min_word = min2words[6]
		im_temp = lightTwentyfivepast(im_input,im_temp)
	elif (30<= x_min < 35):
		x_min_word = min2words[7]
		im_temp = lightHalfpast(im_input,im_temp)
	elif (35<= x_min < 40):
		x_min_word = min2words[8]
		im_temp = lightTwentyfiveto(im_input,im_temp)
	elif (40<= x_min < 45):
		x_min_word = min2words[9]
		im_temp = lightTwentyto(im_input,im_temp)
	elif (45<= x_min < 50):
		x_min_word = min2words[10]
		im_temp = lightQuarterto(im_input,im_temp)
	elif (50<= x_min < 55):
		x_min_word = min2words[11]
		im_temp = lightTento(im_input,im_temp)
	elif (55<= x_min <= 59):
		x_min_word = min2words[12]
		im_temp = lightFiveto(im_input,im_temp)
	else:
		x_min_word = min2words[1]
		im_temp = lightOclock(im_input,im_temp)
	return x_min_word,im_temp

# List of fcuntion for giving light to all the words.
# Function for showing O'CLOCK
def lightOclock(im_input,im_temp):
	for i in xrange(459,942):
		for j in xrange(847,890):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	return im_temp

def lightItis(im_input,im_temp):
	for i in xrange(30,160):
		for j in xrange(25,85):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	for i in xrange(300,416):
		for j in xrange(25,85):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	return im_temp

def lightQuarterpast(im_input,im_temp):
	for i in xrange(196,776):
		for j in xrange(121,175):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	for i in xrange(24,338):
		for j in xrange(387,445):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255				
	return im_temp

def lightTwentypast(im_input,im_temp):
	for i in xrange(24,512):
		for j in xrange(209,269):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	for i in xrange(24,338):
		for j in xrange(387,445):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	return im_temp

def lightTenpast(im_input,im_temp):
	for i in xrange(457,683):
			for j in xrange(297,354):
				if im_input[j,i] >= 4:
					im_temp[j,i] = 255
	for i in xrange(24,338):
		for j in xrange(387,445):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	return im_temp

def lightTwentyfivepast(im_input,im_temp):
	for i in xrange(24,512):
		for j in xrange(209,269):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	for i in xrange(24,338):
		for j in xrange(387,445):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	for i in xrange(552,872):
		for j in xrange(211,267):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	return im_temp

def lightFivepast(im_input,im_temp):
	for i in xrange(24,338):
		for j in xrange(387,445):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	for i in xrange(552,872):
		for j in xrange(211,267):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	return im_temp

def lightHalfpast(im_input,im_temp):
	for i in xrange(20,348):
		for j in xrange(297,363):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	for i in xrange(24,338):
		for j in xrange(387,445):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	return im_temp

def lightQuarterto(im_input,im_temp):
	for i in xrange(196,776):
		for j in xrange(121,175):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	for i in xrange(806,952):
		for j in xrange(291,355):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255				
	return im_temp

def lightTwentyto(im_input,im_temp):
	for i in xrange(24,512):
		for j in xrange(209,269):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	for i in xrange(806,952):
		for j in xrange(291,355):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	return im_temp

def lightTento(im_input,im_temp):
	for i in xrange(457,683):
			for j in xrange(297,354):
				if im_input[j,i] >= 4:
					im_temp[j,i] = 255
	for i in xrange(806,952):
		for j in xrange(291,355):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	return im_temp

def lightTwentyfiveto(im_input,im_temp):
	for i in xrange(24,512):
		for j in xrange(209,269):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	for i in xrange(806,952):
		for j in xrange(291,355):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	for i in xrange(552,872):
		for j in xrange(211,267):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	return im_temp			
	
def lightFiveto(im_input,im_temp):
	for i in xrange(806,952):
		for j in xrange(291,355):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	for i in xrange(552,872):
		for j in xrange(211,267):
			if im_input[j,i] >= 4:
				im_temp[j,i] = 255
	return im_temp

	pass	

# Display and light which hour it is 
def lightHour(x_hour,im_input,im_temp):
	if x_min>=35:
		if x_hour == 12:
			x_hour=0
		x_hour=x_hour+1

	if x_hour==1:
		for i in xrange(20,244):
			for j in xrange(477,531):
				if im_input[j,i] >= 4:
					im_temp[j,i] = 255
	elif x_hour ==2:
		for i in xrange(717,961):
			for j in xrange(565,628):
				if im_input[j,i] >= 4:
					im_temp[j,i] = 255	
	elif x_hour ==3:
		for i in xrange(550,947):
			for j in xrange(480,539):
				if im_input[j,i] >= 4:
					im_temp[j,i] = 255	
	elif x_hour ==4:
		for i in xrange(26,337):
			for j in xrange(570,628):
				if im_input[j,i] >= 4:
					im_temp[j,i] = 255		
	elif x_hour ==5:
		for i in xrange(380,690):
			for j in xrange(569,633):
				if im_input[j,i] >= 4:
					im_temp[j,i] = 255
	elif x_hour ==6:
		for i in xrange(285,520):
			for j in xrange(473,547):
				if im_input[j,i] >= 4:
					im_temp[j,i] = 255
	elif x_hour ==7:
		for i in xrange(26,437):
			for j in xrange(753,806):
				if im_input[j,i] >= 4:
					im_temp[j,i] = 255
	elif x_hour ==8:
		for i in xrange(26,421):
			for j in xrange(658,720):
				if im_input[j,i] >= 4:
					im_temp[j,i] = 255	
	elif x_hour ==9:
		for i in xrange(631,954):
			for j in xrange(386,445):
				if im_input[j,i] >= 4:
					im_temp[j,i] = 255	
	elif x_hour ==10:
		for i in xrange(16,244):
			for j in xrange(835,895):
				if im_input[j,i] >= 4:
					im_temp[j,i] = 255		
	elif x_hour ==11:
		for i in xrange(462,942):
			for j in xrange(658,717):
				if im_input[j,i] >= 4:
					im_temp[j,i] = 255		
	else:
		for i in xrange(450,956):
			for j in xrange(739,809):
				if im_input[j,i] >= 4:
					im_temp[j,i] = 255
	return im_temp

# Get time handler
# Image read section
t = time.localtime()
im_in = cv2.imread('wordClock.png')
# uncommnet to get the shape of the stored image
# print(im_in.shape)
im_input = cv2.cvtColor(im_in,cv2.COLOR_BGR2GRAY)
im_te = cv2.imread('wordClock.png')
im_temp = cv2.cvtColor(im_te,cv2.COLOR_BGR2GRAY)


# Display hour, time and sec
# print ' Day of hr:', t.tm_hour
# print ' Day of min:', t.tm_min
# print ' Day of sec:', t.tm_sec

# to get the current time
# get hour
x_hour = t.tm_hour
# get min
x_min = t.tm_min
# get sec
x_sec = t.tm_sec

# call the main functions.
x_hour = twentyfourTwelve(x_hour) # conver 24 to 12 hr formet
im_temp = lightHour(x_hour,im_input,im_temp) # Light the hour
x_hour_words = hours2words(x_hour,x_min)
x_min_words,im_temp= minutes2words(x_min,im_input,im_temp) # Light the min
# Light It is, which is on for all the time.
im_temp = lightItis(im_input,im_temp)

# print(x_hour_words)
# print(x_min_words)

h,w,c = im_in.shape

# Converting the white lights to blue lights
# Change the light colors with changing the pixel
# value assignments 
for i in range(h-1):
	for j in range(w-1):
		if (im_temp[i,j] == 255):
			im_in[i,j,0] = 255
			im_in[i,j,1] = 255			


# Uncomment the comment in line 362 and move ':' to end, 
# and change 6000 >>> 0 
# this will give the window infinite time till you clik
# on the image window and press esc on the keyboard.
# display the clock face for 6 seconds
while(1):
    cv2.namedWindow('image', flags=cv2.WINDOW_NORMAL)
    im = cv2.resize(im_in, (700,700))
    cv2.imshow('image',im)

    # cv2.imshow('image',im)
    # display it for 6 seconds.
    if cv2.waitKey(6000):# & 0xFF == 27: 
        break
cv2.destroyAllWindows()






