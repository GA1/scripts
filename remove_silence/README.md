##### script trimming audio files


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