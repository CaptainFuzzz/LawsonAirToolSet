# Lawson Air Tool Set (LAToolSet)

This program was developed as an in-house tool for automating the different tasks involved in maintaining and creating new air conditioning product series on the company's websites.
The program works alongside the **.xml** exporting and importing templates within the cpanel of the websites.

![Startup Screenshot](Images/Start.png)

###
## Installation
Install modules using pip:
```
pip install customtkinter
pip install CTkMessagebox
pip install lxml
pip install pandas
pip install beautifulsoup4
```
# Updating and Changing Pre-existing products:

By using a **.xml** export file and a **.csv** file the program can change/update different aspects of products. These changes are then exported as a new **.xml** file for importing to either of the websites.


&nbsp;
![Page1 Screenshot](Images/Updating_Products_page.png)
&nbsp;


# Creating New Products
Uploading a **.csv** file that follows the structure of the **Product_Struct.csv** file, the program can convert this information into **.xml** that can be imported to the Neto site.
&nbsp;
![Page2 Screenshot](Images/Product_Creation.png)
