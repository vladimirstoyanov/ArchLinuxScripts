import os
import sys
import subprocess

def speak(text: str,
          voice: str = None,
          speed: int = 0,
          pitch: int = 0,
          volume: int = 100,
          module: str = None,
          chunk_size: int = 0):  # optional for very long text
    """
    Speak using spd-say with -w to BLOCK until speech actually finishes.
    This ensures sequential playback in loops.
    """
    if not text.strip():
        return

    cmd = ["spd-say", "-w"]  # ← The magic flag: wait for completion

    if module:
        cmd.extend(["-o", module])
    if voice:
        cmd.extend(["-y", voice])
    if speed != 0:
        cmd.extend(["-r", str(speed)])
    if pitch != 0:
        cmd.extend(["-p", str(pitch)])
    if volume != 100:
        cmd.extend(["-i", str(volume)])

    if chunk_size > 0:
        # Split if text is huge (helps avoid rare queue stalls)
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        for chunk in chunks:
            full_cmd = cmd + [chunk]
            _run_spd(full_cmd)
    else:
        full_cmd = cmd + [text]
        _run_spd(full_cmd)


def _run_spd(cmd):
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # Optional: tiny post-speak gap for natural flow
        # import time; time.sleep(0.3)
    except subprocess.CalledProcessError as e:
        print(f"spd-say failed (code {e.returncode}) – is speech-dispatcher running?")
    except FileNotFoundError:
        print("spd-say not found – check speech-dispatcher install.")

if __name__ == '__main__':
    data = ""
    with open("input.txt", "r") as f:
        data = f.read()

    speak (data)
