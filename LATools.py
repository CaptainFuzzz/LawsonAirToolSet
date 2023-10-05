# Backend for the LAtoolset contains all the functions to create new and edit existing products for and on the Neto websites.

import os
import pathlib
import math
import Energy_Ratings as ER
import Product as pt
import lxml.etree
import pandas as pd
from bs4 import BeautifulSoup as BS

def Parse_file(file: str):

    file_path = pathlib.Path(file)
    
    if file_path.suffix == ".xml":
    
        with open(file, 'r', encoding='UTF-8') as xmlfile:
            xml = xmlfile.read()
            Soup = BS(xml, "lxml-xml")
        xmlfile.close()
    
        Products = Soup.find_all("Product")
    
        return Products
    

    dataframe = pd.read_csv(file)

    Products = []
    
    for index, row in dataframe.iterrows():
        Products.append(tuple(row))
    
    return Products


def Create_Product_Object(Product, file: str):
    file_path = pathlib.Path(file)

    if file_path.suffix == ".xml":
        product = pt.Product(
        Main_Image = Product.find('Main_Image').text,
        Alt_Image_01 = Product.find('Alt_Image_01').text,
        Alt_Image_02 = Product.find('Alt_Image_02').text,
        Alt_Image_03 = Product.find('Alt_Image_03').text,
        Alt_Image_04 = Product.find('Alt_Image_04').text,
        Alt_Image_05 = Product.find('Alt_Image_05').text,
        Alt_Image_06 = Product.find('Alt_Image_06').text,
        Alt_Image_07 = Product.find('Alt_Image_07').text,
        Alt_Image_08 = Product.find('Alt_Image_08').text,
        Alt_Image_09 = Product.find('Alt_Image_09').text,
        Alt_Image_10 = Product.find('Alt_Image_10').text,
        Brand = Product.find('Brand').text,
        Sku = Product.find('SKU').text,
        Parent_SKU = Product.find('Parent_SKU').text,
        Name = Product.find('Name').text,
        Subtitle = Product.find('Subtitle').text,
        Custom_Label = Product.find('Custom_Label').text,
        Rrp = Product.find('RRP').text,
        Price_A = Product.find('Price_A').text,
        Price_B = Product.find('Price_B').text,
        Description = Product.find('Description').text,
        Short_Description = Product.find('Short_Description').text,
        Features = Product.find('Features').text,
        Specifications = Product.find('Specifications').text,
        Warranty = Product.find('Warranty').text,
        Specifics = Product.find('Specifics').text,
        Categories = Product.find('Categories').text,
        Add_Cart = Product.find('Add_Cart').text,
        Mansfield_Stock = Product.find('Mansfield_Stock').text,
        Sydney_Stock = Product.find('Sydney_Stock').text,
        Width = Product.find('Width').text,
        Length = Product.find('Length').text,
        Height = Product.find('Height').text,
        Shipping_Weight = Product.find('Shipping_Weight').text,
        Search_Keywords = Product.find('Search_Keywords').text,
        SEO_Page_Title = Product.find('SEO_Page_Title').text,
        SEO_Meta_Keywords = Product.find('SEO_Meta_Keywords').text,
        SEO_Meta_Description = Product.find('SEO_Meta_Description').text,
        Date_Added = Product.find('Date_Added').text,
        Active = Product.find('Active').text,
        Approved = Product.find('Approved').text
        )

        return product
    


    product = pt.Product(
    Main_Image = Product[0],
    Alt_Image_01 = Product[1],
    Alt_Image_02 = Product[2],
    Alt_Image_03 = Product[3],
    Alt_Image_04 = Product[4],
    Alt_Image_05 = Product[5],
    Alt_Image_06 = Product[6],
    Alt_Image_07 = Product[7],
    Alt_Image_08 = Product[8],
    Alt_Image_09 = Product[9],
    Alt_Image_10 = Product[10],
    Brand = Product[11],
    Sku = Product[12],
    Parent_SKU = Product[13],
    Name = Product[14],
    Subtitle = Product[15],
    Custom_Label = Product[16],
    Rrp = Product[17],
    Price_A = Product[18],
    Price_B = Product[19],
    Description = Product[20],
    Short_Description = Product[21],
    Features = Product[22],
    Specifications = Product[23],
    Warranty = Product[24],
    Specifics = Product[25],
    Categories = Product[26],
    Add_Cart = Product[27],
    Mansfield_Stock = Product[28],
    Sydney_Stock = Product[29],
    Width = Product[30],
    Length = Product[31],
    Height = Product[32],
    Shipping_Weight = Product[33],
    Search_Keywords = Product[34],
    SEO_Page_Title = Product[35],
    SEO_Meta_Keywords = Product[36],
    SEO_Meta_Description = Product[37],
    Date_Added = Product[38],
    Active = Product[39],
    Approved = Product[40],
    DescTitle= Product[41]
    )
    
    return product



def Reduce_List(Products, Reduce_List_file:str):

    products = []
    dataframe = pd.read_csv(Reduce_List_file)

    for product in Products:
        for index, row in dataframe.iterrows():
            r = tuple(row)
            if product.Sku == r[0]:
                products.append(product)
    
    return products



def Update_Prices(Products, Price_Change_List:str):

    products = []

    dataframe = pd.read_csv(Price_Change_List)

    for product in Products:
        for index, row in dataframe.iterrows():
            r = tuple(row)
            if product.Sku == r[0]:
                product.Change_Prices(r[1], r[2])
                products.append(product)
    
    return products



def Update_Specifications(Products, SKU_csv_file:str, Specification_html_file:str):

    products = []

    df = pd.read_csv(SKU_csv_file)

    Specification_file = open(Specification_html_file, 'r')
    specs = Specification_file.read()
    Soup = BS(specs,'lxml')

    specifications = Soup.prettify()
    
    for product in Products:
        for index, row in df.iterrows():
            r = tuple(row)

            if product.Sku == r[0]:
                product.Change_Specifications(specifications)
                products.append(product)
    
    return products



def Create_Products_CSV(CSV_file:str):
    Products = []

    df = pd.read_csv(CSV_file)

    for index, row in df.iterrows():
        temp = []
        r = tuple(row)
        r_list = list(r)        
        
        for i in r_list:
            if (type(i) == float) and (math.isnan(i)): i = ""

            temp.append(i)
        
        r_list = temp


        prod = Create_Product_Object(r_list, CSV_file)
        
        Products.append(prod)
    
    return Products



def Create_XML(Products, Save_Path:str):
    
    OutFile = Save_Path

    root = lxml.etree.Element('Products')

    for prod in Products:
        Product = lxml.etree.SubElement(root, 'Product')

        Main_Image = lxml.etree.SubElement(Product, 'Main_Image')
        Alt_Image_01 = lxml.etree.SubElement(Product, 'Alt_Image_01')
        Alt_Image_02 = lxml.etree.SubElement(Product, 'Alt_Image_02')
        Alt_Image_03 = lxml.etree.SubElement(Product, 'Alt_Image_03')
        Alt_Image_04 = lxml.etree.SubElement(Product, 'Alt_Image_04')
        Alt_Image_05 = lxml.etree.SubElement(Product, 'Alt_Image_05')
        Alt_Image_06 = lxml.etree.SubElement(Product, 'Alt_Image_06')
        Alt_Image_07 = lxml.etree.SubElement(Product, 'Alt_Image_07')
        Alt_Image_08 = lxml.etree.SubElement(Product, 'Alt_Image_08')
        Alt_Image_09 = lxml.etree.SubElement(Product, 'Alt_Image_09')
        Alt_Image_10 = lxml.etree.SubElement(Product, 'Alt_Image_10')
        Brand = lxml.etree.SubElement(Product, 'Brand')
        Sku = lxml.etree.SubElement(Product, 'SKU')
        Parent_SKU = lxml.etree.SubElement(Product, 'Parent_SKU')
        Name = lxml.etree.SubElement(Product, 'Name')
        Subtitle = lxml.etree.SubElement(Product, 'Subtitle')
        Custom_Label = lxml.etree.SubElement(Product, 'Custom_Label')
        Rrp = lxml.etree.SubElement(Product, 'RRP')
        Price_A = lxml.etree.SubElement(Product, 'Price_A')
        Price_B = lxml.etree.SubElement(Product, 'Price_B')
        Description = lxml.etree.SubElement(Product, 'Description')
        Short_Description = lxml.etree.SubElement(Product, 'Short_Description')
        Features = lxml.etree.SubElement(Product, 'Features')
        Specifications = lxml.etree.SubElement(Product, 'Specifications')
        Warranty = lxml.etree.SubElement(Product, 'Warranty')
        Specifics = lxml.etree.SubElement(Product, 'Specifics')
        Categories = lxml.etree.SubElement(Product, 'Categories')
        Add_Cart = lxml.etree.SubElement(Product, 'Add_Cart')
        Mansfield_Stock = lxml.etree.SubElement(Product, 'Mansfield_Stock')
        Sydney_Stock = lxml.etree.SubElement(Product, 'Sydney_Stock')
        Width = lxml.etree.SubElement(Product, 'Width')
        Length = lxml.etree.SubElement(Product, 'Length')
        Height = lxml.etree.SubElement(Product, 'Height')
        Shipping_Weight = lxml.etree.SubElement(Product, 'Shipping_Weight')
        Search_Keywords = lxml.etree.SubElement(Product, 'Search_Keywords')

        SEO_Page_Title = lxml.etree.SubElement(Product, 'SEO_Page_Title')
        SEO_Meta_Keywords = lxml.etree.SubElement(Product, 'SEO_Meta_Keywords')
        SEO_Meta_Description = lxml.etree.SubElement(Product, 'SEO_Meta_Description')
        
        Date_Added = lxml.etree.SubElement(Product, 'Date_Added')
        Active = lxml.etree.SubElement(Product, 'Active')
        Approved = lxml.etree.SubElement(Product, 'Approved')

        Brand.text = prod.Brand
        Sku.text = prod.Sku
        Parent_SKU.text = prod.Parent_SKU
        Subtitle.text = prod.Subtitle
        Custom_Label.text = prod.Custom_Label

        Rrp.text = str(prod.Rrp)
        Price_A.text = str(prod.Price_A)
        Price_B.text = str(prod.Price_B)
        Add_Cart.text = prod.Add_Cart
        Mansfield_Stock.text = str(prod.Mansfield_Stock)
        Sydney_Stock.text = str(prod.Sydney_Stock)

        Width.text = str(prod.Width)
        Length.text = str(prod.Length)
        Height.text = str(prod.Height)
        Shipping_Weight.text = str(prod.Shipping_Weight)

        Search_Keywords.text = prod.Search_Keywords
        Date_Added.text = prod.Date_Added
        Active.text = prod.Active
        Approved.text = prod.Approved
        
        Name.text = lxml.etree.CDATA(prod.Name)
        Categories.text = lxml.etree.CDATA(prod.Categories)
        Specifics.text = lxml.etree.CDATA(prod.Specifics)


        Main_Image.text = lxml.etree.CDATA(prod.Main_Image)
        Alt_Image_01.text = lxml.etree.CDATA(prod.Alt_Image_01)
        Alt_Image_02.text = lxml.etree.CDATA(prod.Alt_Image_02)
        Alt_Image_03.text = lxml.etree.CDATA(prod.Alt_Image_03)
        Alt_Image_04.text = lxml.etree.CDATA(prod.Alt_Image_04)
        Alt_Image_05.text = lxml.etree.CDATA(prod.Alt_Image_05)
        Alt_Image_06.text = lxml.etree.CDATA(prod.Alt_Image_06)
        Alt_Image_07.text = lxml.etree.CDATA(prod.Alt_Image_07)
        Alt_Image_08.text = lxml.etree.CDATA(prod.Alt_Image_08)
        Alt_Image_09.text = lxml.etree.CDATA(prod.Alt_Image_09)
        Alt_Image_10.text = lxml.etree.CDATA(prod.Alt_Image_10)

        
        if (os.path.exists(prod.Description)) and (prod.DescTitle != None):
            description_file = open(prod.Description, 'r')
            des = description_file.read()
            Soup = BS(des, 'lxml')

            title = Soup.find('title', id='t')
            title.string = prod.DescTitle
            description = Soup.prettify()

            Description.text = lxml.etree.CDATA(description)
        
        else:
            Description.text = lxml.etree.CDATA(prod.Description)


        if (os.path.exists(prod.Specifications)):
            Specification_file = open(prod.Specifications, 'r')
            specs = Specification_file.read()
            Soup = BS(specs,'lxml')

            specs = Soup.prettify()
            
            Specifications.text = lxml.etree.CDATA(specs)
        
        else:
            Specifications.text = lxml.etree.CDATA(prod.Specifications)



        Short_Description.text = lxml.etree.CDATA(prod.Short_Description)
        Features.text = lxml.etree.CDATA(prod.Features)
        Specifications.text = lxml.etree.CDATA(prod.Specifications)
        Warranty.text = lxml.etree.CDATA(prod.Warranty)

        SEO_Page_Title.text = lxml.etree.CDATA(prod.SEO_Page_Title)
        SEO_Meta_Keywords.text = lxml.etree.CDATA(prod.SEO_Meta_Keywords)
        SEO_Meta_Description.text = lxml.etree.CDATA(prod.SEO_Meta_Description)
    
    lxml.etree.indent(root)

    xmlstr = lxml.etree.tostring(root, method='xml')

    with open(OutFile, 'wb') as f:
        f.write(xmlstr)
    f.close()

    if os.path.exists(OutFile):
        print("File has been created successfully!\n")
    else:
        print("File could not be created.")

def First_Empty_Image_Slot(product: pt.Product):
    if (len(product.Main_Image) == 1): return 0
    if (len(product.Alt_Image_01) == 1): return 1
    if (len(product.Alt_Image_02) == 1): return 2
    if (len(product.Alt_Image_03) == 1): return 3
    if (len(product.Alt_Image_04) == 1): return 4
    if (len(product.Alt_Image_05) == 1): return 5
    if (len(product.Alt_Image_06) == 1): return 6
    if (len(product.Alt_Image_07) == 1): return 7
    if (len(product.Alt_Image_08) == 1): return 8
    if (len(product.Alt_Image_09) == 1): return 9
    if (len(product.Alt_Image_10) == 1): return 10

def Energy_Rating_Image(product, slot, value):
    if (slot == 0): product.Main_Image = ER.EnergyRating.Energy_Rating(value)
    if (slot == 1): product.Alt_Image_01 = ER.EnergyRating.Energy_Rating(value)
    if (slot == 2): product.Alt_Image_02 = ER.EnergyRating.Energy_Rating(value)
    if (slot == 3): product.Alt_Image_03 = ER.EnergyRating.Energy_Rating(value)
    if (slot == 4): product.Alt_Image_04 = ER.EnergyRating.Energy_Rating(value)
    if (slot == 5): product.Alt_Image_05 = ER.EnergyRating.Energy_Rating(value)
    if (slot == 6): product.Alt_Image_06 = ER.EnergyRating.Energy_Rating(value)
    if (slot == 7): product.Alt_Image_07 = ER.EnergyRating.Energy_Rating(value)
    if (slot == 8): product.Alt_Image_08 = ER.EnergyRating.Energy_Rating(value)
    if (slot == 9): product.Alt_Image_09 = ER.EnergyRating.Energy_Rating(value)
    if (slot == 10): product.Alt_Image_10 = ER.EnergyRating.Energy_Rating(value)

def Add_Energy_Rating_Image(Products, Energy_Rating_List:str):
    
    products = []
    temp = []

    dataframe = pd.read_csv(Energy_Rating_List)

    for index, row in dataframe.iterrows():
        temp.append(tuple(row))
    
    for product in Products:
        for item in temp:
            if (item[0] == product.Sku):
                slot = First_Empty_Image_Slot(product)
                products.append(Energy_Rating_Image(product, slot, item[1]))
    
    return products

