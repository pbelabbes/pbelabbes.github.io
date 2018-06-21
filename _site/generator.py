#!/usr/bin/env python

from JekyllMdFile import JekyllMdFile
from slugify import slugify 
import os


def generateFrontMatter(taxo_path, version, doc_site, old_path, url_to_md):

    with open(taxo_path, "r") as taxonomy:

        level_ref = -1
        old_level = 0
        order = 0
        c_categ = []

        # Read the taxonomy
        while 1:
            line = taxonomy.readline()
            if not line:
                break
            
            if "http" in line: continue
            # print line

            # Get the level of depth for the current link
            lineB = line.split('*')
            if len(lineB) <= 1 : continue
            spaces = lineB[0]
            level = 0
            for char in spaces:
                # print "-%s- is number : %d" % (char,ord(char))
                if ord(char) == 32:
                    level += 0.5
                elif ord(char) == 9 :
                    level+=1
                else:
                    print "-%s- is number : %d \n line :%s" % (char, ord(char), line)
            if level != old_level and level_ref == -1  : level_ref = level 
            level = int(level)/level_ref
            # print "space : %s has a length of %d" % (spaces,level)

            # Retrieve the name of the file

            lineB = lineB[1].split('[')[1].split(']')

            old_title = ""

            if 'title' in locals():
                old_title = title
            title = lineB[0]

            # Retrieve the path of the file
            lineB = lineB[1].split('(')[1].split(')')

            old_base_name = ""

            if 'base_name' in locals():
                old_base_name = base_name
            base_name = lineB[0]

            # print "Line in process : %s with level of %d " % (title, level)

            

            if level <= old_level and old_base_name  :
                
                JekyllMdFile.files.append(
                    JekyllMdFile(doc_site, version, order, old_path, old_title,
                                old_base_name, c_categ, url_to_md))
                order += 1

            if level > old_level:
                if old_title:
                    c_categ.append(old_title)
                old_level = level

            while level < old_level:
                try :
                    c_categ.pop()
                except IndexError :
                    print c_categ

                old_level -= 1

    JekyllMdFile.files.append(
        JekyllMdFile(doc_site, version, order, old_path, title, base_name, c_categ,
                    url_to_md))
    order += 1 
    JekyllMdFile.files.append(
        JekyllMdFile(doc_site, version, order, old_path, "index", "index.md", [],
                    url_to_md))

    # a_basenames = [f.base_name for f in JekyllMdFile.files]
    # print len(a_basenames)

def generateFiles():
    for f in JekyllMdFile.files:
        # print f.version
        # print f.path

        if not os.path.exists(f.path):
            # print f.path +  " doesn't exist"
            os.makedirs(f.path)
        
        # print "Le bon basename "+f.base_name
        
        with open(f.path +"/"+  f.base_name, "w") as dest:
          
            src = open(f.old_path +f.base_name,"r")
            dest.write(f.front_matter)
            while 1:
                line = src.readline()
                if not line : break
            
                dest.write(f.parseLine(line))
            src.close()   


def generate_doc(docSitePath, version, destPath):

    urlToMd = docSitePath+"/md/"
    taxonomy = urlToMd +"taxonomy.md"
    urlToNwMd = destPath

    docSite = docSitePath.split('/')[len(docSitePath.split('/'))-1]
    
    if  docSite == "bonita-doc":
        urlToNwMd +="_bonita/" + version 
        docSite = "bonita"  
    
    elif docSite == "bonita-continuous-delivery-doc":
        urlToNwMd +="_bcd/"+version
        docSite = "bcd"

    elif docSite == "bonita-ici-doc":
        urlToNwMd +="_ici/"+version
        docSite = "ici"

    generateFrontMatter(taxonomy, version, docSite, urlToMd, urlToNwMd)

    generateFiles()