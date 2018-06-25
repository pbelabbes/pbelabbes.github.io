#!/usr/bin/env python
from slugify import slugify 
import re
from shutil import copyfile
import os

class JekyllMdFile(object):

    files =[]
    front_matter =""

    def __init__(self, docSite, version, order, old_path, title, base_name,categs, urlToNwMd):

        # print "categories : %s " % categs
        self.categs= [categ for categ in categs if categs]

        self.title = title 

        self.base_name = base_name 

        self.path = urlToNwMd+"/"+("/".join([slugify(categ) for categ in categs]))
        
        self.old_path=old_path
        
        self.order = order

        self.version = version

        self.docSite = docSite

        self.front_matter = """---
layout : doc
title : \"%s\"
version : \"%s\"
categories:\n%s
order : %d
---
""" % (self.title, self.version, self.getCategs(), self.order)

        # print "front matter of %s is %s\n" % (self.base_name, self.front_matter) 

    @staticmethod
    def getPath(basename, line):
        path = ""
        docSite = ""
        version = ""
            
        

        for md in JekyllMdFile.files:
            
            if basename == md.base_name :
                for c in md.categs :
                    path += slugify(c)+"/"
                
                docSite = md.docSite
                version = md.version

        if not docSite : 
            # print "-"+basename+"- line : \n"+ line +" "
            raise Exception("File not found")

        res = docSite+"/"+version+"/"+path
        return res
       
        
        

    def getCategs(self):
        result = ""

        for index,categ  in enumerate(self.categs) :
            result += "  - "+categ
            result += "\n" if index < len(self.categs)-1 else ""
        return result

    
    def  parseLine(self,line):

        if "(images/" in line :
            # print "images in process..."
            self.image_management(line)
        
        if  "](" in line and ".md" in line:
            line = self.addRelativePath(line)

        # if ":::" in line :
        #     line = self.insertAlert(line)

        if "${varVersion}" in line :
            line = line.replace("${varVersion}", "{{page.version}}")
        return line

    
    def image_management(self,line):
        split_line = line.split("](")

        lenSplitLine = len(split_line)
        for i in range(1,lenSplitLine):
            img_uri = split_line[i].split(")")[0]

            if "\"" in img_uri : img_uri = img_uri.split(" \"")[0]
            # print "insert images ... "
            self.insertImg(img_uri)

    
    
    def insertImg(self,img_uri):
        img_path = self.path+'/'
        path_tab = img_uri.split('/')

        img_basename = path_tab.pop()

        img_path+="/".join(path_tab)

        if not os.path.exists(img_path):
            # print f.path +  " doesn't exist"
            os.makedirs(img_path)

        # print "Start copying %s in %s" % (self.old_path+img_uri,img_path+"/"+img_basename)
        try :
            copyfile(self.old_path+img_uri,img_path+"/"+img_basename)
        except IOError :
            print "%s not found" % self.old_path+img_uri
        # print "Transfert successful"
   
    
    def addRelativePath(self,line):
        
        res = ""
        split1 = line.split("](")

        nbLinks = len(split1)

        res += split1[0]

        for i in range(1,nbLinks):

            after =""

            if "#" in split1[i] :
                split2 = split1[i].split('#')
                after+="#"
            elif "://" in split1[i]:
                res += "]("+split1[i]
                continue
            else :
                split2 = split1[i].split(")")
                after += ")"
            
            
            after += ')'.join(split2[1:])
            basename = split2[0]

            # print "[ "+self.base_name + "]\n" + line
            
            try : 
               
                path = JekyllMdFile.getPath(basename, line)
                if not path :
                    print line
                    path = ""
                res += "]({{\""+ path +basename.split(".md")[0]+"\" | relative_url}}"+after

            except Exception :
                

                res = res.split('[')[0] + res.split('[')[1] + ')'.join(after.split(')')[1:])

            
        # print res
        return res

    def insertAlert(self,line):

        # print self.base_name
        split1 = line.split(":::")
        level=""

        if len(split1) >= 2 :
            level = split1[1]

        level = level.replace(" ","")
        level = level.replace("\n","")
        
        # print level
        return "{% endalert %}\n" if not level else "{%% alert %s %%}\n" % level 