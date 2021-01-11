# pip install fastapi uvicorn[standard]


from fastapi import FastAPI

app = FastAPI()


@app.get('/get-zcr')
async def root():
    music_file = '../data/fma_small/000/000002.mp3'
    y, sr = librosa.load(music_file)
    
    zcr = librosa.feature.zero_crossing_rate(y)
    
    return {'zcr': zcr}

# uvicorn main:app --reload
