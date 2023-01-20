import pywebio
from pywebio.input import input, TEXT
from pywebio.output import put_text, put_html, put_markdown, put_table
def encryptor():
  english = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
  code = '$ £ ¢ ¥ | ● √ ¿ & × \ © ∆ @ + π ¶ % ~ ÷ } ◆ * ® _ % '.split()
  decoder = dict({})

  for i in range(len(english)):
    decoder[code[i]]=english[i]

  # message = '''€¿$÷  _+}   ¿$◆】√+÷  &~  ÷¿&~  +@©_  ©&●】, _+}%  ©&●】. _+}  €$@÷  ÷+  £】-¢+∆】 $   €%&÷】-%.  £}÷  _+}  
  # $%】 ● }©©_  $€$%】 +●  
  # ÷©】π%+£©】-∆~  _+}  $%】 √+&@√  ÷+  ●$¢】. _+}  $%】 @】-◆】-%  ∆】-$@÷  ÷+  £】 ¿$ππ_ , _+}  $%】 ∆】-$@÷  ÷+  £】 $©+@
  # '''.split()
  message = input().split()
  print(message)
  print("\n")
  meaning=""
  for j in message:
      word = ''
      for m in j:
          if m in [',','.','-']:
              continue
          if m=='】':
              m='|'
          elif m=='€':
              m='*'
          elif m=='【':
              m='^'
          elif m=='%':
              decoder[m]='R'
          word+=decoder[m]
      meaning+=word+" "
  put_text(meaning)
if __name__=='__main__':
  pywebio.start_server(encryptor,port=80)
