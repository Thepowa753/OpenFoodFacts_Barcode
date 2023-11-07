class FoodDto:
    Error: str
    Image: str
    Barcode: str
    Name: str
    Categories: list[str]
    EN_categories: list[str]
    Ingredients: list[str]
    Packaging: str
    def __init__(self, Image = None, Barcode = None, Name = None, Categories = None, EN_categories = None, Ingredients = None, Packaging = None, Error = None):
        self.Image = Image
        self.Barcode = Barcode
        self.Name = Name
        if Categories is not None:
            self.Categories = Categories.split(", ")
        else:
            self.Categories = Categories
        self.EN_categories = EN_categories
        self.Ingredients = Ingredients
        self.Packaging = Packaging
        self.Error = Error
    

    def toString(self):
        return f"Barcode: {self.Barcode}" + \
            (f"\nName: {self.Name}" if self.Name is not None else '') + \
            (f"\nImage: {self.Image}" if self.Image is not None else '') + \
            (f"\nCategories: {self.Categories}" if self.Categories is not None and len(self.Categories)>0  else '') + \
            (f"\nEN_categories: {self.EN_categories}" if self.EN_categories is not None and len(self.EN_categories)>0  else '') + \
            (f"\nIngredients: {self.Ingredients}" if self.Ingredients is not None and len(self.Ingredients)>0 else '') + \
            (f"\nPackaging: {self.Packaging}" if self.Packaging is not None else '') + \
            (f"\nError: {self.Error}" if self.Error is not None else '')