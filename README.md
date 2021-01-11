# Simple Audio Retrieval Project 

Simple Audio Retrieval Project for   
```Multimedia Retrieval 2: Advanced Topics```   
from ```Prof. Daniel A. Keim, University of Konstanz```.  
  
This is the base repo and will provide code for a script to download songs from the FMA dataset for music analysis.  
https://github.com/mdeff/fma  
Another script will shortly introduce librosa and audio feature extractions.  
https://librosa.org/doc/latest/index.html
  
# Task and Points
 **a)** Download the needed data (the get_data.py should help or use curl or etc.) and install the needed libraries.  
    Make yourself familiar with librosa and the data.  
    Connect the labels of the data with the data itself.  
 **b)** Extract features from the data and store them in a way you prefer.  
    Randomly select 5% of the data as query samples.  
 **c)** Create a similarity function based on your extracted features.  
    Create a kNearestNeighbor ranking of the query samples.  
 **d)** Create a web app to interactively search for nearest neighbors.   
    Let a user select a sample and visualize the similarity function and features.  
 **e) BONUS:** Enhance the web app with more interaction and visualization features. **Be CREATIVE!**    
   
 Overall points: 36  
 **a)** 3  
 Show some steps to load all the data and show some statistics.  
 **b)** 12  
 Show how to store the data after you loaded it and how to extract featrures.  
 Be creative with the features and test them. Robust/good or creative features get you points.  
 **c)** 12  
 Show how your similarity function works and how to apply kNearestNeighbor search on the data.   
 The more robust your extracted features and similarity function are, the more points you get.  
 **d)** 9  
 Be creative again. FastAPI/Flask should enable an easy web app, but you can also use d3 and a html only version.  
 **e)** Bonus Points: 6  
 Be creative as possible. The cooler the idea, the better.  

 ## Submission

Submit either a zipped version of your web application and extraction scripts or submit a file with the link to your public repository. The code must be cloneable and runnable. If not, you get a maximum of half the points.

# Goals
 - Students should learn to apply librosa feature extractors
 - Students should create a simple similarity function to find nearest neighbors
 - Students should build a simple web app to interactively search for nearest neighbors
 - Students should enhance the web app with various additions, e.g., PCA plot of the data

# Data

The dataset originates from the Free Music Archive published at the ISMIR 2017.  
https://github.com/mdeff/fma  

## Meta Data
https://os.unil.cloud.switch.ch/fma/fma_metadata.zip : fma_metadata.zip (342 MiB)  
  
```tracks.csv```: per track metadata such as ID, title, artist, genres, tags, and play counts, for all 106,574 tracks.  
```genres.csv```: all 163 genres with name and parent (used to infer the genre hierarchy and top-level genres).  
```features.csv```: common features extracted with librosa.  
```echonest.csv```: audio features provided by Echonest (now Spotify) for a subset of 13,129 tracks.  

## Small Data

We will only work with the small dataset as it will already be enough data to work on (8000).  
https://os.unil.cloud.switch.ch/fma/fma_small.zip : fma_small.zip: 8,000 tracks of 30s, 8 balanced genres (GTZAN-like) (7.2 GiB)  
  
However, you can still use one of the larger datasets if you really want to.  

# Hints

```scripts/get_data.py``` shows how to download the data using Python.  
```scripts/requirements.txt``` shows some valuable Python libraries.  
```scripts/librosa-1-load-file.ipynb``` shows how to load a mp3 file in librosa.  
```scripts/librosa-2-extract-features.ipynb``` shows how to extract features using librosa.  
```scripts/librosa-3-extract-features-nn.ipynb``` shows how to extract logits from a neural network with MFCCs and librosa.  
```scripts/fastapi.py``` shows how to setup a fastapi backend.  

# Further References

https://librosa.org/doc/latest/index.html  
https://fastapi.tiangolo.com/  
https://pytorch.org/  
  
https://musicinformationretrieval.com/index.html 


# Acknowledgements

For the data:
Michaël Defferrard, Kirell Benzi, Pierre Vandergheynst, Xavier Bresson.  
```
Michaël Defferrard, Kirell Benzi, Pierre Vandergheynst, and Xavier Bresson. "Fma: A dataset for music analysis." In Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), 2017.
```
  
For Librosa:
McFee, Brian, Colin Raffel, Dawen Liang, Daniel PW Ellis, Matt McVicar, Eric Battenberg, and Oriol Nieto
```
McFee, Brian, Colin Raffel, Dawen Liang, Daniel PW Ellis, Matt McVicar, Eric Battenberg, and Oriol Nieto. "librosa: Audio and music signal analysis in python." In Proceedings of the 14th python in science conference, pp. 18-25. 2015.
```


