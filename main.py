import os
import string
import pandas as pd

def main():
    langs = ['Amis_wiki', 'Paiwan_wiki', "Atayal_wiki", "Sakizaya_wiki", "Seediq_wiki"]
    home = os.curdir
    counts = {'Amis_wiki':0, 'Paiwan_wiki':0, "Atayal_wiki":0, "Sakizaya_wiki":0, "Seediq_wiki":0}
    for lang in os.listdir():
        if lang in langs:
            lang_path = os.path.join(home, lang)
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
            
    

    print(counts)

def count():
    data = pd.read_csv("counts.txt")
    token_counts = data.groupby('Language')['Tokens'].sum().reset_index()
    token_counts.columns = ['Language', 'Total Tokens']

    print(token_counts)
    print(list(token_counts['Language']))
    print(list(token_counts['Total Tokens']))

if __name__ == "__main__":
    count()