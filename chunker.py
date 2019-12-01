def chunker(name):
    from pydub import AudioSegment
    from pydub.utils import make_chunks

    myaudio = AudioSegment.from_file("ul/{}/audio.wav".format(name) , "wav") 
    chunk_length_ms = 15000 # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

    #Export all of the individual chunks as wav files
    ct=0
    for i, chunk in enumerate(chunks):
        chunk_name = "ul/{}/chunk{}.wav".format(name,i)
        #print ("exporting", chunk_name)
        ct+=1
        chunk.export(chunk_name, format="wav")
    return ct
