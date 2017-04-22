


#!/usr/bin/env python
# Your task here is to extract data from xml on authors of an article
# and add it to a list, one item for an author.
# See the provided data structure for the expected format.
# The tags for first name, surname and email should map directly
# to the dictionary keys
import xml.etree.ElementTree as ET

article_file = "exampleResearchArticle.xml"


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def get_author(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {}
        data["fnm"] = author.find('./fnm').text
        data["snm"] = author.find('./snm').text
        data["email"] = author.find('./email').text

        authors.append(data)

    return authors

def main():
      root = get_root(article_file)
      print root
      print "\n"
      for child in root:
          print child.tag

      print "\n"
      data = get_author(root)
      print data
      print "\n"

      for i in range(len(data)):
          print data[i]["fnm"] + ' ' + data[i]["snm"] + ' ' + 'Email:' + data[i]["email"]


if __name__ == '__main__':
    main()

