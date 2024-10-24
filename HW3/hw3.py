"""
HW3
Authors: Thatcher Craig  David Zhang
"""
import audio

#This function repeat the clip for specified times.
def loop():
    name_loop = input("Enter the name of an audio file: ")
    num_loops = int(input("Enter the number of times to repeat the sound clip: "))
    looped = []
    original = audio.read_wav(name_loop)
    
    for i in range(num_loops + 1):
        looped = i * original
    
    audio.write_wav(looped,'looped.wav')
    #audio.play('looped.wav')

#This function cut the clip in half and swap them.
def flipflop():
    audio_name = input("Enter the name of the audio file: ")
    samples = audio.read_wav(audio_name)
    len_audio = len(samples)
    first_half = []
    second_half = []
    flipflopped = []
    
    for i in range(int(len_audio / 2)):
        first_half.append(samples[i])
    
    for i in range(int(len_audio / 2), len_audio):
        second_half.append(samples[i])
    
    flipflopped = second_half + first_half
    
    audio.write_wav(flipflopped,'flipflopped.wav')
    #audio.play('flipflopped.wav')
    

#This function makes the clip sounds weaker and weaker.
def fade():
    audio_name = input("Enter the name of the audio file: ")
    samples = audio.read_wav(audio_name)
    len_audio = len(samples)
    
    for i in range(len_audio):
        samples[i] = samples[i] * (1 - i / (len_audio -1))
        
    audio.write_wav(samples,'faded.wav')
    #audio.play('faded.wav')

#This function makes the clip echoes.
def echo():
    audio_name = input("Enter the name of the audio file: ")
    original = audio.read_wav(audio_name)
    SOFTNESS_FACTOR = 0.3
    SHITF_AMOUNT = 1/8
    softened = []
    new = []

    # This is the softened list.
    for i in range(len(original)): 
        softened.append(original[i]*SOFTNESS_FACTOR)
        
    # We split the list into three parts. The first part is from
    # the original list where it is not added to the softened list.
    for i in range(int(len(original)*SHITF_AMOUNT)):
        new.append(original[i])
        
    # The second part is the part where the original list and the
    # softened list are added together.
    for i in range(int(len(original)*SHITF_AMOUNT),len(original)):
        new.append(original[i]+softened[i-int(len(original)*SHITF_AMOUNT)])
        
    # The third part is the part of the leftover elements in the soften list.
    for i in range(len(original)-int(len(original)*SHITF_AMOUNT),len(original)):
        new.append(softened[i])
    
    audio.write_wav(new,'echoed.wav')
    #audio.play('echoed.wav')


#This function cut the clip and repeat the cutted clip for specified times
#Most DJ use this sound effect in their music
def dj():
    audio_name = input("Enter the name of the audio file: ")
    num_cut = int(input("Enter the time you want to cut the clip: "))
    num_times = int(input("Enter the number of times you want to repeat the cutted part: "))
    samples = audio.read_wav(audio_name)
    len_audio = len(samples)
    new = []
    
    for i in range(int(len_audio/num_cut)):
        new.append(samples[i])
        
    new = new * num_times 

        
        
    audio.write_wav(new,'faded.wav')
    #audio.play('faded.wav')
    
    


def main():
    loop()
    flipflop()
    fade()
    echo()
    dj()
'''
Note: Do not change/remove the following code!
''' 

if __name__ == "__main__":
    main()   