cd $1
arduino-cli compile --fqbn arduino:avr:leonardo
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:leonardo
