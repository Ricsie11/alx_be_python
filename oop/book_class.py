class Book:
    #Constructor
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    #Magic method
    def __str__(self):
        return f'{self.title} by {self.author}, published {self.year}.'
    
    def __repr__(self):
        return f"Book('Title: {self.title}', Author: '{self.author}', Year: {self.year})."
    

    #Destructor
    def __del__(self):
        print (f'Deleting {self.title}.')
    

book = Book("1984", "George Orwell", 1949)
print(book)
