### remove long silences in the audio


before first run
```
python3 -m venv venv_remove_silence
source venv_remove_silence/bin/activate
pip3 install -r requirements.txt
```

put input files into `input_files` directory

run 
```
python3 audio_trimmer.py
```

the results will be saved in `results` directory


### How does the script work?
One can change the parameters CHUNK_SIZE and CHUNK_BUFFER (they are integers)
 
The script eliminates a chunk of CHUNK_SIZE ms 
only if previous CHUNK_BUFFER and next CHUNK_BUFFER chunks are silent as well  

