# Text-to-Animalese Translator

This project is a Python-based text-to-animalese translator, inspired by the vocal sounds from _Animal Crossing_. Given any sentence, the program converts it into a sequence of corresponding sounds for each character, played at random speeds. The translator also filters out swear words and content in parentheses, ensuring clean outputs. Additionally, it saves the audio output as a file in the `outputs` folder.

### Features:

- Converts any text input into animalese sounds
- Plays each character at a random playback speed for a fun, varied experience
- Filters out swear words and content inside parentheses
- Put in your own voice
- Saves the generated audio to a `.mp3` file in the `outputs` folder

### Credits

This project is adapted from an idea originally implemented by [Henry Ishuman](https://linktr.ee/henryishuman). Much credit goes to Henry for his work in developing the concept that inspired this translator.

---

## Setup Instructions

### Prerequisites

To run this project, you need the following:

- Python 3.x installed on your machine
- `pydub` library (see below for installation)

### Install Dependencies

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd <repo-name>

   ```

2. Create and activate a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required libraries:

   ```
   pip install -r requirements.txt
   ```

4. Ensure you have the necessary .wav files for each letter and digit inside the res/audio/ directory. You can also include a bebebese_slow.wav file for handling unsupported characters.

### Recording your own voice

To add your own voice, replace the .wav files in "audio" with your own. For a good workflow I recommend importing them as different tracks in audacity (free program for audio recording) and exporting the tracks as different files when you are done.

You can get it to speed up and slow down by modifying the max speeds at the top of start.py or by changing the silence_thresh.

## File Structure

```
.
├── res
│ └── audio
│ ├── a.wav
│ ├── b.wav
│ ├── ...
│ └── bebebese_slow.wav
├── outputs
├── translator.py
├── requirements.txt
└── README.md
```

## Requirements

The required Python packages are listed in requirements.txt:

    •	pydub
    •	gtts

## License

This project is available under the MIT License.
