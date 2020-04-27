import json
import audioowl
import matplotlib.pyplot as plt
import sys
import os
import errno

def getNote(_time, _lineIndex , _lineLayer , _type , _cutDirection ):
    _note = """
        {
            "_time": 1,
            "_lineIndex": 2,
            "_lineLayer": 0,
            "_type": 0,
            "_cutDirection": 1
        }
    """
    note = json.loads(_note)
    note['_time']= _time
    note['_lineIndex']= _lineIndex
    note['_lineLayer']= _lineLayer
    note['_type']= _type
    note['_cutDirection']= _cutDirection
    #print(note)
    return note


 
#waveform = audioowl.get_waveform('beat30.wav')
#data = audioowl.analyze_file('drums.mp3', sr=22050)

songName = '7akim'
data = audioowl.analyze_file(path=songName+'.ogg')

 
# some JSON:
x =  """
{
    "_version": "2.0.0",
    "_customData": {
        "_time": 0,
        "_BPMChanges": [],
        "_bookmarks": []
    },
    "_events": [],
    "_notes": [],
    "_obstacles": []
}
"""

# parse x:
y = json.loads(x)




for x in data['beat_samples']:
    print(x/22050)
    _time = x/22050
    y["_notes"].append( getNote(_time,2,0,0,1))    

filename = "./" + songName + "/EasyStandard.dat"
if not os.path.exists(os.path.dirname(filename)):
    try:
        os.makedirs(os.path.dirname(filename))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise


with open( filename , 'w') as outfile:
    json.dump(y, outfile)

print(y)

#print(json.loads(obj))


# print('the beats @ times')
# for x in data['beat_samples']:
#   print(x/22050)

print('-----------------------------------------------------')
print('---------sample_rate--------------------------------------------')
print (  data['sample_rate'])
print('---------duration--------------------------------------------')
print (  data['duration'])
print('---------beat_samples--------------------------------------------')
print (  data['beat_samples'])
print('---------number_of_beats--------------------------------------------')
print (  data['number_of_beats'])
print('---------tempo_float--------------------------------------------')
print (  data['tempo_float'])
print('---------tempo_int--------------------------------------------')
print (  data['tempo_int'])
print('---------zero_crossing--------------------------------------------')
print (  data['zero_crossing'])
print('---------noisiness_median--------------------------------------------')
print (  data['noisiness_median'])
print('---------noisiness_sum--------------------------------------------')
print (  data['noisiness_sum'])
print('---------notes--' , len(data['notes'] ),'------------------------------------------')
print (  data['notes'])

plt.figure()
plt.vlines(data['beat_samples'], -1.0, 1.0)

plt.show()
