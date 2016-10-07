import os
print ("Welcome to my Tool")
test_file= open('C:/ProjectSE/OpenCPN/src/toolbar.cpp','r')
ui_object=['wxCaret','wxControl','wxCursor','wxDC','wxDropTarget',
           'wxLayoutConstraints','wxSizer','wxToolTip','wxWindowBase','wxWindow',
           'wxScrollHelper','wxFrame','wxMenuBar','wxMenuItem','wxToolBar',
           'wxBitmap','wxBrush','wxColour','wxFont','wxIcon',
           'wxPalette','wxPen','wxRegion','wxString','wxIconBundle'
           'wxPoint','wxBitmapHandler','wxIcon','wxMask','wxPalette',
           'wxClientDC','wxPaintDC','wxWindowDC','wxScreenDC','wxMemoryDC',
           'wxPrinterDC','wxPrintData','wxWindowDC','wxClientDC','wxPaintDC',
           'wxMemoryDC','wxPrinterDC','wxScreenDC','wxButtonBase','wxAcceleratorEntry',
           'wxMenu','wxPenBase','wxPenList','wxBrushBase','wxBrushList'
           'wxPaletteBase','wxSizer','wxStdDialogButtonSizer','wxBoxSizer','wxDialogLayoutAdapter'
           'wxDialog','wxButton','wxScrolledWindow','wxMessageDialogBase','wxDataObjectBase',
           'wxToolTip','wxCoord','wxRect','wxCoord','wxPoint',
           'wxBrush','wxToolBarToolBase']

line_num=1
count=1
object_list=[]
index=0
object_name=""

#print (ui_file.read())
for line in test_file:
    words=line.split()
    #print(words)
    
    for i,word in enumerate(words):
        #print(word)
        for obj in ui_object:
            if((word == obj) | (word==(obj+"*")) | (word==(obj+"&"))):
                if(words[i+1]!="{"):
                    if(words[i+1]=="*"):
                        object_name=words[i+3]
                        if(object_name.endswith(';')):
                            object_name=object_name[:-1]
                            object_list.append(object_name)
                            #print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                        elif(object_name.endswith(',')):
                            object_name=object_name[:-1]
                            object_list.append(object_name)
                            #print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                        elif(object_name.endswith('(')):
                            object_name=object_name[:-1]
                            object_list.append(object_name)
                            #print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                        elif(object_name.endswith(')')):
                            print("not a object")
                        else:
                            
                            object_list.append(object_name)
                            #print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                        
                        #print(line_num, word,object_list[index])
                        
                    else:
                        object_name=words[i+1]
                        if(object_name.endswith(';')):
                            object_name=object_name[:-1]
                            object_list.append(object_name)
                            #print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                        elif(object_name.endswith(',')):
                            object_name=object_name[:-1]
                            object_list.append(object_name)
                            #print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                        elif(object_name.endswith('(')):
                            object_name=object_name[:-1]
                            object_list.append(object_name)
                            #print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                        elif(object_name.endswith(')')):
                            print("not a object")
                        else:
                            
                            object_list.append(object_name)
                            #print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                         
                    
                    
                #if(words[i-1]!="new"):
                #print(words[i+1]) 
                
    #print(line_num)
    line_num=line_num+1
    
"""with open('C:/ProjectSE/OpenCPN/src/toolbar.cpp', mode='rt', encoding='utf-8') as f:
    text = f.read()


for x in object_list:
   search_word=x
   if search_word in text:
       with open('C:/ProjectSE/OpenCPN/src/toolbar.html', mode='wt', encoding='utf-8') as f:
            f.write(text.replace(search_word, '<span style="color: red">{}</span>'.format(search_word)))

   else:
       print("The word is not in the text")
"""
with open("C:/ProjectSE/OpenCPN/src/toolbar.cpp") as f:
    
    with open("C:/ProjectSE/OpenCPN/src/toolbar.txt", "w") as f1:
        for line in f:
            if "ROW" in line:
                f1.write(line)
        text = f1.read()
for x in object_list:
   search_word=x
   if search_word in text:
       print()
       print(text.replace(search_word, '\033[44;33m{}\033[m'.format(search_word)))

   else:
       print("The word is not in the text")
print ("Number of places ", count)

    

