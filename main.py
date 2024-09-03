import os
import string
import pandas as pd
import xml.etree.ElementTree as ET


def main():
    langs = ['Amis_wiki', 'Paiwan_wiki', "Atayal_wiki", "Sakizaya_wiki", "Seediq_wiki"]
    home = os.curdir
    counts = {'Amis_wiki':0, 'Paiwan_wiki':0, "Atayal_wiki":0, "Sakizaya_wiki":0, "Seediq_wiki":0}
    files = dict()
    for lang in os.listdir():
        if lang in langs:
            lang_path = os.path.join(home, lang)
            print(lang, len(os.listdir(lang_path)), "\n")
            for article in os.listdir(lang_path):
                if article == ".DS_Store":
                    continue
                article_path = os.path.join(lang_path, article)
                if lang == "Amis_wiki" or lang == "Paiwan_wiki" or lang == "Atayal_wiki":
                    article_txt = os.path.join(article_path, article+"_cleaned.txt")
                else:
                    article_txt = os.path.join(article_path, article+"_edited.txt")
                file = open(article_txt, "r")
                data = file.read()
                file.close()
                data = ''.join([i for i in data if not i.isdigit()])
                data = data.translate(str.maketrans('', '', string.punctuation))
                #print(len(data.split()))
                counts[lang] += len(data.split())
                if lang == "Amis_wiki":
                    files[article] = len(data.split())
            
    

    print(counts)
    print(files)

def count():
    data = pd.read_csv("counts.txt")
    token_counts = data.groupby('Language')['Tokens'].sum().reset_index()
    token_counts.columns = ['Language', 'Total Tokens']

    print(token_counts)
    print(list(token_counts['Language']))
    print(list(token_counts['Total Tokens']))
    print(sum(list(token_counts['Total Tokens'])))


def count_ILRDF():
    dir = os.path.join(os.curdir, "ILRDF")
    ILRDF_count = dict()
    for file in os.listdir(dir):
            count = 0
            file_path = os.path.join(dir, file)
            tree = ET.parse(file_path)
            root = tree.getroot()

            # Iterate over all <S> elements
            for s in root.findall('.//S'):
                # Find the <FORM> element within the <S> element
                form = s.find('FORM')

                if form is not None and form.text is not None:
                    # Split the text of the <FORM> element into words
                    words = form.text.split()
                    # Count the number of words
                    count += len(words)
            
            ILRDF_count[file.split('.')[0]] = count

if __name__ == "__main__":
    count()