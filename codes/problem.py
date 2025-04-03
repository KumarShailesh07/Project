'''
Design a ‘book’ class with title, author, publisher, price, and author’s royalty as
instance variables. Provide getter and setter properties for all variables. 
Also, define a method royalty() to calculate royalty amount author can expect
to receive the following royalties:10%  of the retail price on the first 500 copies;
12.5% for the next 1,000 copies sold, then 15% for all further copies sold.

Then design a new ‘ebook’ class inherited from the ‘book’ class. 
Add ebook format (EPUB, PDF,  MOBI, etc) as an additional instance variable
in the inherited class.
Override royalty() method to deduct GST @12% on ebooks.
'''

class book:
    def __init__(self,title,author,publisher,price,royality):
        self.title=title
        self.author=author
        self.publisher=publisher
        self.price=price
        self.royality=royality

    def gettitle(self):
        return self.title
    def getauthor(self):
        return self.author
    def getpublisher(self):
        return self.publisher
    def getprice(self):
        return self.price
    def getroyality(self):
        return self.royality
    
    