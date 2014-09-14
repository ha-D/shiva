from django.shortcuts import render
import gspread

def minutestotakeoff(request):
	gc = gspread.login('kami.endless@gmail.com', 'pcystefbmvmxgopj')
	sht1 = gc.open('Minutes to Takeoff').sheet1
	vals = sht1.get_all_values()
	vals = vals[2:]
	return render(request, 'mtt/takeoff.html', {'friends':vals})

def maps(request):
    gc = gspread.login('kami.endless@gmail.com', 'pcystefbmvmxgopj')
    sht1 = gc.open('Minutes to Takeoff').sheet1
    vals = sht1.get_all_values()
    vals = vals[2:]
    return render(request, 'mtt/maps.html', {'friends':vals})