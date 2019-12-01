from flask import *
import shutil
import os
import numpy as np
from vidown import download
from audc import audc
from chunker import chunker
from aud2text import aud2text

app = Flask(__name__)

@app.route('/' ,methods=['GET','POST'])
def upload_file():
   return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      link=request.form['link']
      lang=request.form['lang']
      
      name=str(np.random.randn())
      path = "ul/{}".format(name)
      pathout = "static/{}".format(name)
      pathvid = "video/{}".format(name)

      try:
         os.mkdir(pathvid)
      except OSError:
         return ("Creation of the directory %s failed" % pathvid)

      try:
         os.mkdir(path)
      except OSError:
         return ("Creation of the directory %s failed" % path)
      
      try:
         os.mkdir(pathout)
      except OSError:
         return ("Creation of the directory %s failed" % pathout)

      #download
      try:
         download(name,link)

      except Exception as e:
         return(str(e))

      
      #audio convert
      try:
         audc(name)


      except Exception as e:
         return(str(e))


      #chunker
      try:
         ct=chunker(name)

      except Exception as e:
         return(str(e))

      #aud2txt
      try:
         aud2text(name,ct,lang)

      except Exception as e:
         return(str(e))

      shutil.rmtree('ul/{}'.format(name))
      #return send_file('static/{}/res.txt'.format(name), attachment_filename='extrext.txt')
      return redirect("download/{}".format(name))

@app.route('/download/<filefolder>' ,methods=['GET','POST'])
def return_files_tut(filefolder):
   try:
      os.remove("video/{}/videostream.mp4".format(filefolder))
      return send_file('static/{}/res.txt'.format(filefolder), attachment_filename='extrext.txt' ,as_attachment=True)
   except Exception as e:
      return str(e)


if __name__ == '__main__':
   app.run(debug = True)




#return render_template('uploadd.html',msg='Successfully processed',link=link ,name=name)

