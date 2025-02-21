# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.
# ''')
# print("""Even so my sun one early morn did shine,
# With all triumphant splendour on my brow;
# But out, alack, he was but one hour mine,
# The region cloud hath mask’d him from me now …""")
# import pyttsx3
# engine = pyttsx3.init()
# engine.say(" hello  myself Durgesh nai")
# engine.runAndWait()
import os

# Specify the directory path
directory_path = '/'

try:
    # Get the list of all entries in the directory
    entries = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
