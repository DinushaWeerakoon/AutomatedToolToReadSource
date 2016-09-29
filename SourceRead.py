import os
print ("Welcome to my Tool")
ui_file= open('C:/ProjectSE/OpenCPN/src/toolbar.cpp','r')
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
for line in ui_file:
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
                            print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                        elif(object_name.endswith(',')):
                            object_name=object_name[:-1]
                            object_list.append(object_name)
                            print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                        elif(object_name.endswith('(')):
                            object_name=object_name[:-1]
                            object_list.append(object_name)
                            print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                        elif(object_name.endswith(')')):
                            print("not a object")
                        else:
                            
                            object_list.append(object_name)
                            print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                        
                        #print(line_num, word,object_list[index])
                        
                    else:
                        object_name=words[i+1]
                        if(object_name.endswith(';')):
                            object_name=object_name[:-1]
                            object_list.append(object_name)
                            print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                        elif(object_name.endswith(',')):
                            object_name=object_name[:-1]
                            object_list.append(object_name)
                            print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                        elif(object_name.endswith('(')):
                            object_name=object_name[:-1]
                            object_list.append(object_name)
                            print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                        elif(object_name.endswith(')')):
                            print("not a object")
                        else:
                            
                            object_list.append(object_name)
                            print(line_num, word,object_list[index])
                            count=count+1
                            index=index+1
                         
                    
                    
                #if(words[i-1]!="new"):
                #print(words[i+1]) 
                
    #print(line_num)
    line_num=line_num+1
    
print ("Number of places ", count)
    
