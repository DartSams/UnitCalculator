# UnitCalculator

## PREVIEW
<img src="static\images\project_preview\unit calculater preview.png" alt="unit calculater preview">

### Steps To Add New Units by webscraping google

## Step 1
    - In the file <scrape conversion data.py> make a list of strings containing the measurements of the units 

## Step 2
    - Next add the list previousely created to the dict varaible <unit_dict> 

## Step 3
<pre> In the same file <scrape conversion data.py> call the function <scrape_conversion_data> and pass in 
    the parameters the first being the list created in Step 1 and the second parameter being the unit type
    this function will scrape google collecting data and inputting them in a dictionary to be exported to a newly created file in the <units> folder 
</pre>

## Step 4
    - In the units folder locate the newly created file and put the json dict into a variable <unit_name_data>
    Ex. length_data = {}

## Step 5
    - In the <units> folder locate the file <__init__.py> this file is needed so files inside the folder can be called/used outside this scope such as being used in the main.py file now here you will add the line 
    <from units.unit_name import unit_name_data> 

## Step 6
    - Next in the <main.py> file find the dict <UNITS> and create a new key and value pair the key being the unit and the value being the file created in Step 3

    Ex. "length":units.length_data

### Adding New Units Without Scraping

## Step 1
    - In the <Units> folder create a file of the unit that you want to have data on

## Step 2
    - In the file from Step 1 create a dict under the variable <unit_name_data> and inside that dict create key and value pairs of the measurements of the unit the key being the measurement and the value being the another dict of all of the other measurements
    Ex. energy_data = {
        "Joule":{
            "to_Kilojoule":{
                "conversion_number":1000.0,
                "operation":"divide"
            }
        }
    }

## Step 3
    - In the units folder locate the newly created file and put the json dict into a variable <unit_name_data>
    Ex. length_data = {}

## Step 4
    - In the <units> folder locate the file <__init__.py> this file is needed so files inside the folder can be called/used outside this scope such as being used in the main.py file now here you will add the line 
    <from units.unit_name import unit_name_data> 

## Step 5
    - Next in the <main.py> file find the dict <UNITS> and create a new key and value pair the key being the unit and the value being the file created in Step 3

    Ex. "length":units.length_data