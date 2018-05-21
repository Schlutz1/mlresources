#!../python/bin/python
#file formatting script, converts to utf-8 encoding, and Unix (LF)

import csv
import sys
import os
#import pandas as pd
import cchardet as c


def csvencode(filename) :
  #print("resp")
  #try:
      #out file name
  #splunk_path = os.environ['SPLUNK_HOME']
  #splunk_path = "/Applications/Splunk"
  convfile = filename.replace(".csv","_utf8.csv")

  #data=pd.read_csv(filename)
  #    for col in data.columns:
  #        try:
  #            if "Unnamed" not in col:
  #                data[col]=data[col].str.replace(",","")
  #        except:
  #                data[col]=data[col]

  #data.to_csv(tmpfile)
  #os.system('touch '+splunk_path+'/etc/apps/aiam-ml-core/lookups/worked')

  #os.remove(filename)
  with open(filename) as f:
      data=f.read()
      enc=c.detect(data)['encoding'].upper()    
  print('enc',enc)    
  if 'ISO-8859-1' in enc:
      enc='CP1252'
  cmd='iconv -c -f '+enc+' -t utf-8 '+filename+' > '+convfile

  os.system(cmd)

      #reads in file
  with open(convfile, 'r+') as f:
      text = f.read()


    #  #encodes in utf-8 and changes to Unix line flush
      #temp = text.encode('utf-8', 'strict')
      temp_line = text.replace('\r', '\n')
      final = temp_line.replace('\n\n', '\n')

    #  #removes prev file to overwrite
    #  os.remove(tmpfile)

    #  #writes out file
      f.seek(0)
      f.write(final)
      f.truncate()

  print("File successfuly converted")
  #except Exception, e:
  #    print("File failed to convert " + str(e))
