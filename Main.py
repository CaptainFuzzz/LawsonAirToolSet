from tkinter import filedialog as fd
from CTkMessagebox import CTkMessagebox
import customtkinter
import LATools



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        # Window Configuration
        self.title("LAToolSet")   
        self.geometry(f"{900}x{500}")   

        # Grid Configuration, layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
            

        # Sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=1000, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="La Tool Set", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.Existing_Products_option = customtkinter.CTkButton(self.sidebar_frame, command=self.Existing_product_frame, text="Change propities of existing products")
        self.Existing_Products_option.grid(row=1, column=0, padx=20, pady=10)

        self.button2 = customtkinter.CTkButton(self.sidebar_frame, command=self.New_Products_frame, text="Create new products")
        self.button2.grid(row=2, column=0, padx=20, pady=10)
        
        # Main frame
        self.mainframe = customtkinter.CTkFrame(self, fg_color="black")
        self.mainframe.grid(row=0, column=1, columnspan=2, rowspan=4, sticky="nsew")

    
    def Existing_product_frame(self):
        existing_products = Button_Functionality()
        
        # Create frame that contains buttons to perform functions        
        self.frame = customtkinter.CTkFrame(self, fg_color="grey")
        self.frame.grid(row=0, column=1, columnspan=2, rowspan=4, sticky="nsew")
        self.frame.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.frame.grid_rowconfigure((0,1,2,3,4), weight=1)

        # Create and add buttons to the new frame.

        self.Upload_XML = customtkinter.CTkButton(self.frame, command=lambda: existing_products.Upload_XML_file(), text="Upload Export File (.xml)")
        self.Upload_XML.grid(row=0, column=0, padx=20, pady=5)

        self.Reduce_Product_List = customtkinter.CTkButton(self.frame, command=lambda: existing_products.Reduce_list(), text="Reduce Product list")
        self.Reduce_Product_List.grid(row=1, column=0, padx=20, pady=5)

        self.Energy_ratings = customtkinter.CTkButton(self.frame, command=lambda: existing_products.Add_Energy_Ratings(), text="Add Energy Rating Images")
        self.Energy_ratings.grid(row=2, column=0, padx=20, pady=5)
    
        self.Update_Specs = customtkinter.CTkButton(self.frame, command=lambda: existing_products.Update_Specifications(), text="Update Specifications")
        self.Update_Specs.grid(row=3, column=0, padx=20, pady=5)

        self.Update_Prices = customtkinter.CTkButton(self.frame, command=lambda: existing_products.Update_Prices(), text="Update Prices")
        self.Update_Prices.grid(row=0, column=1, padx=20, pady=5)


        self.Create_XML_File = customtkinter.CTkButton(self.frame, command=lambda: existing_products.Create_XML_file(), text="Create Import File")
        self.Create_XML_File.grid(row=4, column=4, padx=20, pady=5)



    def New_Products_frame(self):
        New_Products = Button_Functionality()
        
        # Create new frame that contains button to create new products

        self.frame = customtkinter.CTkFrame(self, fg_color="grey")
        self.frame.grid(row=0, column=1, columnspan=2, rowspan=4, sticky="nsew")
        self.frame.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.frame.grid_rowconfigure((0,1,2,3,4), weight=1)

        # Create buttons and add to frame
        
        self.Create_New_Products = customtkinter.CTkButton(self.frame, command=lambda: New_Products.Create_New_Products(), text="Create New Products")
        self.Create_New_Products.grid(row=2, column=3, padx=20, pady=5)

        self.Create_XML_File = customtkinter.CTkButton(self.frame, command=lambda: New_Products.Create_XML_file(mode_type=True), text="Create Import File")
        self.Create_XML_File.grid(row=4, column=4, padx=20, pady=5)



class Button_Functionality:

    def __init__(self, Products=None, xml_filename=None, csv_filename=None, html_filename=None):
        self.html_filename = html_filename
        self.xml_filename = xml_filename
        self.csv_filename = csv_filename
        self.Products = Products


    def Upload_XML_file(self):
        
        temp_products = []
        
        filetypes = (('xml files', '*.xml'), 
                     ('All files', '*.*'))
        
        self.xml_filename = fd.askopenfilename(title='Open .xml', initialdir='/', filetypes=filetypes)

        products = LATools.Parse_file(self.xml_filename)

        for product in products:
            temp_products.append(LATools.Create_Product_Object(product, self.xml_filename))

        self.Products = temp_products

    
    def Error_MessageBox(self):
        msg = CTkMessagebox(title="Info", message="No export (.xml) file has been provided.", 
                      option_1="Upload file?", option_2="Cancel")

        if msg.get() == "Upload file?":
            self.Upload_XML_file()
            return True
        else:
            return False
        

    def Reduce_list(self):

        if self.xml_filename == None:
            msg = self.Error_MessageBox()

            if msg == False:
                return

        filetypes = (('csv files', '*.csv'),
                     ('All files', '*.*'))

        self.csv_filename = fd.askopenfilename(title='Open .csv', initialdir='/', filetypes=filetypes)
        
        old_Prod_list = self.Products
        self.Products = LATools.Reduce_List(old_Prod_list, self.csv_filename)


    def Update_Prices(self):

        if self.xml_filename == None:
            msg = self.Error_MessageBox()

            if msg == False:
                return

        filetypes = (('csv files', '*.csv'),
                     ('All files', '*.*'))

        self.csv_filename = fd.askopenfilename(title='Open .csv', initialdir='/', filetypes=filetypes)

        old_Prods_list = self.Products
        self.Products = LATools.Update_Prices(old_Prods_list, self.csv_filename)

    
    def Add_Energy_Ratings(self):

        if self.xml_filename == None:
            msg = self.Error_MessageBox()

            if msg == False:
                return

        filetypes = (('csv files', '*.csv'),
                     ('All files', '*.*'))

        self.csv_filename = fd.askopenfilename(title='Open .csv', initialdir='/', filetypes=filetypes)

        old_Prod_list = self.Products
        self.Products = LATools.Add_Energy_Rating_Image(old_Prod_list, self.csv_filename)

    
    def Update_Specifications(self):
        
        if self.xml_filename == None:
            msg = self.Error_MessageBox()

            if msg == False:
                return

        filetypes_csv = (('csv files', '*.csv'),
                     ('All files', '*.*'))
        
        filetypes_html = (('html files', '*.html'),
                     ('All files', '*.*'))
        
        self.csv_filename = fd.askopenfilename(title='Open .csv', initialdir='/', filetypes=filetypes_csv)
        self.html_filename = fd.askopenfilename(title='Open .html', initialdir='/', filetypes=filetypes_html)

        old_Prod_list = self.Products
        self.Products = LATools.Update_Specifications(old_Prod_list, self.csv_filename, self.html_filename)


    def Create_New_Products(self):

        filetypes = (('csv files', '*.csv'),
                     ('All files', '*.*'))

        self.csv_filename = fd.askopenfilename(title='Open .csv', initialdir='/', filetypes=filetypes)

        self.Products = LATools.Create_Products_CSV(self.csv_filename)


    def Create_XML_file(self, mode_type:bool = False):
        
        if mode_type == False:

            if self.xml_filename == None:
                CTkMessagebox(title="Warning", message="No export (.xml) file has been provided.")
                return
        
        else:

            if self.csv_filename == None:
                CTkMessagebox(title="Warning", message="No .csv creation file provided.")
                return

        filetypes = (('xml files', '*.xml'),
                     ('All files', '*.*'))

        Save_path = fd.asksaveasfilename(initialfile="Untitled.xml", defaultextension=".xml", filetypes=filetypes)
        
        LATools.Create_XML(self.Products, Save_path)
    







if __name__ == "__main__":
    app = App()

    app.mainloop()