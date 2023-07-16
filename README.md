# VR Beatsaber Map Generator

This project is an attempt to automatically generate maps for the VR game "Beatsaber" using audio analysis libraries.

## Requirements

To use this map generator, you will need to have the following libraries installed:

- audioowl (installed without dependencies)
- numpy
- scipy
- cython
- madmom
- librosa

## Installation

To install the necessary libraries, you can use pip:

```
pip install audioowl --no-dependencies
pip install numpy
pip install scipy
pip install cython
pip install madmom
pip install librosa
```

## Usage

To use the map generator, run the `script.py` script it expects the some to be in the .ogg format in the same directory:

```
python script.py
```

The script will analyze the audio and attempt to generate a map for the Beatsaber game. The resulting map will be saved as a JSON file in the same directory.

## Note

This project is a work in progress and may not always generate accurate or playable maps. Use at your own risk.

trying to automatically generate Maps for [beat saber VR game](https://www.youtube.com/watch?v=2dRTe_iXtT0&ab_channel=syrmatrix)

Manually created tracks : [track 1](https://www.youtube.com/watch?v=0a2lswEUVWY&t=63s&ab_channel=MahmoudAshraf) , [track 2](https://www.youtube.com/watch?v=9sA0teajRsk&t=55s&ab_channel=MahmoudAshraf) , [track 3](https://www.youtube.com/watch?v=du_NvAMUqyM&t=127s&ab_channel=MahmoudAshraf)
