def aud2text(name,ct,lang):
    import speech_recognition as sr
    r=sr.Recognizer()
    file=open("static/{}/res.txt".format(name),"a")
    qu=ct+1
    ini=int(qu/17)
    rem = qu % 17
    for j in range(ini):
      for i in range(j*17,17*(j+1)):
        try:
          aud=sr.AudioFile("ul/{}/chunk{}.wav".format(name,i))
          with aud as source:
            audio=r.record(source)
          a=r.recognize_google(audio , language="en-US")
          file.write(a)
          file.write(" ")
          print(0)
        except Exception as e:
          print(e)
        file.close()
        file=open("static/{}/res.txt".format(name),"a")          

    for k in range(ini*17,ct):
        try:
          aud=sr.AudioFile("ul/{}/chunk{}.wav".format(name,k))
          with aud as source:
            audio=r.record(source)
          a=r.recognize_google(audio , language=lang)
          file.write(a)
          file.write(" ")
          print(0)
        except Exception as e:
          print(e)
    file.close()      
