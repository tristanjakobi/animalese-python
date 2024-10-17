import os
import random
import re
from pydub import AudioSegment
from datetime import datetime

# File paths
audio_folder = "audio/"
bebebese = os.path.join(audio_folder, "bebebese_slow.wav")
output_folder = "outputs/"

# Ensure output directory exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Parameters for playback speed
playbackSpeedMin = 3.5
playbackSpeedMax = 5.0

# Swear words to filter out
swear_words = ["fuck", "shit", "piss", "crap", "bugger"]

def replace_swear_words(sentence):
    """Replace swear words with asterisks."""
    for word in swear_words:
        sentence = re.sub(word, '*' * len(word), sentence, flags=re.IGNORECASE)
    return sentence

def replace_parentheses(sentence):
    """Replace content within parentheses with asterisks."""
    return re.sub(r'\(.*?\)', lambda x: '*' * (len(x.group()) - 2), sentence)

def remove_spaces(sentence):
    """Remove all spaces from the sentence."""
    return sentence.replace(" ", "")

def build_sentence(sentence):
    """Clean and format the sentence."""
    sentence = sentence.lower()
    sentence = replace_swear_words(sentence)
    sentence = replace_parentheses(sentence)
    sentence = remove_spaces(sentence)
    return sentence

def get_character_audio_file(character):
    """Get the file path for a character's audio file, or return 'bebebese' for unsupported characters."""
    if character.isalpha() or character.isdigit():
        return os.path.join(audio_folder, f"{character}.wav")
    elif character == " ":
        return None
    else:
        return bebebese

def trim_silence(audio, silence_thresh=-35, chunk_size=10):
    """Trim leading and trailing silence from an audio segment."""
    start_trim = detect_leading_silence(audio, silence_thresh, chunk_size)
    end_trim = detect_leading_silence(audio.reverse(), silence_thresh, chunk_size)
    duration = len(audio)
    return audio[start_trim:duration-end_trim]

def detect_leading_silence(sound, silence_thresh=-35.0, chunk_size=10):
    """Detect leading silence in an audio segment."""
    trim_ms = 0  # ms
    assert chunk_size > 0  # chunk size must be greater than 0
    while trim_ms < len(sound) and sound[trim_ms:trim_ms+chunk_size].dBFS < silence_thresh:
        trim_ms += chunk_size
    return trim_ms

def speak_sentence(sentence):
    """Generate and concatenate audio files for each character in the sentence."""
    sentence = build_sentence(sentence)
    playback_speed = random.uniform(playbackSpeedMin, playbackSpeedMax)
    combined_audio = AudioSegment.silent(duration=1)  # Reduced initial silence duration
    
    for char in sentence:
        char_file = get_character_audio_file(char)
        if char_file and os.path.exists(char_file):
            try:
                audio = AudioSegment.from_wav(char_file)
                audio = trim_silence(audio)  # Trim silence
                if len(audio) > 50:  # Only speed up if the audio segment is longer than 50ms
                    audio = audio.speedup(playback_speed, chunk_size=50, crossfade=25)
                combined_audio += audio
            except Exception as e:
                print(f"Error loading or processing audio file for character '{char}': {e}")
        else:
            print(f"Audio file for character '{char}' does not exist: {char_file}")
    
    # Generate a unique filename using the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_folder, f"output_audio_{timestamp}.mp3")
    
    # Export the concatenated audio as MP3
    try:
        combined_audio.export(output_path, format="mp3")
        print(f"Audio saved to {output_path}")
    except Exception as e:
        print(f"Error exporting audio file: {e}")

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a phrase: ")
    speak_sentence(user_input)