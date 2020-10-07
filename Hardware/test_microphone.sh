sudo arecord -l
sudo arecord -f S16_LE -c 2 -d 10 -r 16000 --device="hw:0,0" /tmp/test-mic.wav
sudo aplay /tmp/test-mic.wav
