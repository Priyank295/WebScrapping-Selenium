from bs4 import BeautifulSoup
import pandas as pd
import os


d = {'title': [], "price" : [] , "link" : []}

for file in os.listdir("data"):
    
    try: 
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")
        t = soup.find("h2")
        title = t.get_text()
        
        l = t.find("a")
        link = "https://www.amazon.in/" + l['href']
        
        p = soup.find("span" , attrs={"class" : "a-price-whole"})
        
        d['title'].append(title)
        d['price'].append(p.get_text())
        d['link'].append(link)
        # break
    except Exception as e:
        print(e)
        
df = pd.DataFrame(d)

df.to_csv("data.csv", index=False)