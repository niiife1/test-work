class Catalogue:

    def __init__(self,catalogue):
        self.catalogue = catalogue
        self.attribute = []
        self.product = []


    def add_product(self,product_name: str):
        if
            self.product.append(product_name)


    def get_by_letter(self,first_letter: str):
        pass
    def __repr__(self,):
        return f"Items in the {self.catalogue} catalogue:"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)