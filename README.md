# lemonde
A python lib to access lemonde newspaper articles

## Usage 
```python
from lemonde import LeMonde

lm = LeMonde()
for article in lm.get_articles():
    print(article.title)
    print(article.type)
    print(article.image)
    print(article.link)
```
