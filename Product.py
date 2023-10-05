# Defines a product object for creating, changing and manipulating products for the Maropost websites for Lawson Air.

class Product:

    def __init__(self, Main_Image = None, Alt_Image_01 = None, Alt_Image_02 = None, Alt_Image_03 = None, Alt_Image_04 = None, Alt_Image_05 = None, Alt_Image_06 = None, 
                 Alt_Image_07 = None, Alt_Image_08 = None, Alt_Image_09 = None, Alt_Image_10 = None, Brand = None, Sku = None, Parent_SKU = None, Name = None, Subtitle = None, 
                 Custom_Label = None, Rrp = None, Price_A = None, Price_B = None, Description = None, Short_Description = None, Features = None, Specifications = None, 
                 Warranty = None, Specifics = None, Categories = None, Add_Cart = None, Mansfield_Stock = None, Sydney_Stock = None, Width = None, Length = None, 
                 Height = None, Shipping_Weight = None, Search_Keywords = None, SEO_Page_Title = None, SEO_Meta_Keywords = None, SEO_Meta_Description = None, 
                 Date_Added = None, Active = None, Approved = None, DescTitle = None):

        self.Main_Image = Main_Image
        self.Alt_Image_01 = Alt_Image_01
        self.Alt_Image_02 = Alt_Image_02
        self.Alt_Image_03 = Alt_Image_03
        self.Alt_Image_04 = Alt_Image_04
        self.Alt_Image_05 = Alt_Image_05
        self.Alt_Image_06 = Alt_Image_06
        self.Alt_Image_07 = Alt_Image_07
        self.Alt_Image_08 = Alt_Image_08
        self.Alt_Image_09 = Alt_Image_09
        self.Alt_Image_10 = Alt_Image_10
        self.Brand = Brand
        self.Sku = Sku
        self.Parent_SKU = Parent_SKU
        self.Name = Name
        self.Subtitle = Subtitle
        self.Custom_Label = Custom_Label
        self.Rrp = Rrp
        self.Price_A = Price_A
        self.Price_B = Price_B
        self.Description = Description
        self.Short_Description = Short_Description
        self.Features = Features
        self.Specifications = Specifications
        self.Warranty = Warranty
        self.Specifics = Specifics
        self.Categories = Categories
        self.Add_Cart = Add_Cart
        self.Mansfield_Stock = Mansfield_Stock
        self.Sydney_Stock = Sydney_Stock
        self.Width = Width
        self.Length = Length
        self.Height = Height
        self.Shipping_Weight = Shipping_Weight
        self.Search_Keywords = Search_Keywords
        self.SEO_Page_Title = SEO_Page_Title
        self.SEO_Meta_Keywords = SEO_Meta_Keywords
        self.SEO_Meta_Description = SEO_Meta_Description
        self.Date_Added = Date_Added
        self.Active = Active
        self.Approved = Approved
        self.DescTitle = DescTitle
    
    def Change_Prices(self, price_A: int, price_B: int):
        self.Rrp = price_A
        self.Price_A = price_A
        self.Price_B = price_B

    def Change_SKU(self, sku: str):
        self.Sku = sku

    def Change_Description(self, description: str, desctitle: str = None):
        if (desctitle != None):
            self.DescTitle = desctitle
            self.Description = description
        else:
            self.Description = description

    def Change_Short_Description(self, short_description: str):
        self.Short_Description = short_description

    def Change_Features(self, features: str):
        self.Features = features

    def Change_Specifications(self, specifications):
        self.Specifications = specifications

    def Change_Warranty(self, warranty: str):
        self.Warranty = warranty
