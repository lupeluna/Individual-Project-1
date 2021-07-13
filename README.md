# Water-Potability-Project
<img> https://user-images.githubusercontent.com/80718680/125486994-cd5b009c-4dbe-4446-bef6-d1c2ef432897.png


Hello,

Welcome to the README file for my "Water Potability Project"

Here, you will find my work on the water_potability.csv file which contains water quality metrics for 3276 different water bodies.  You will also find the data dictionary to help offer more insight to the variables being used.
_______________________

## Abstract

Are you interested in the quality of potable water?  Water is a basic human right and clean access to it is vital to our survival.  The data used in this project are the quality metrics for 3276 different water bodies.  We will find out how drinkable the water and predict if water is safe to drink.



_______________________

## GOAL:

My goal is to identify and key driver(s) of water potability within the Water_potability database and develop a classification model to accurately predict the key driver(s) of drinkable water.

______________________



## Planning process

Below you will see the TRELLO pipleline I used which can also be found in this link: [TrelloBoard](https://trello.com/b/v8QuSceS/individual-project-water-quality)



___________________________

-  Please use this data dictionary as a reference for the variables used within in the data set.



|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
| ph | float64   | PH is an important parameter in evaluating the acid–base balance of water. It is also the indicator of acidic or alkaline condition of water status. WHO has recommended maximum permissible limit of pH from 6.5 to 8.5. The current investigation ranges were 6.52–6.83 which are in the range of WHO standards.    |
| hardness   | float64 | Hardness is mainly caused by calcium and magnesium salts. These salts are dissolved from geologic deposits through which water travels. The length of time water is in contact with hardness producing material helps determine how much hardness there is in raw water. Hardness was originally defined as the capacity of water to precipitate soap caused by Calcium and Magnesium. |
| solids   | float64 | Water has the ability to dissolve a wide range of inorganic and some organic minerals or salts such as potassium, calcium, sodium, bicarbonates, chlorides, magnesium, sulfates etc. These minerals produced un-wanted taste and diluted color in appearance of water. This is the important parameter for the use of water. The water with high TDS value indicates that water is highly mineralized. Desirable limit for TDS is 500 mg/l and maximum limit is 1000 mg/l which prescribed for drinking purpose.|
| chloramines   | float64 | Chlorine and chloramine are the major disinfectants used in public water systems. Chloramines are most commonly formed when ammonia is added to chlorine to treat drinking water. Chlorine levels up to 4 milligrams per liter (mg/L or 4 parts per million (ppm)) are considered safe in drinking water.|
| sulfate  | float64| Sulfates are naturally occurring substances that are found in minerals, soil, and rocks. They are present in ambient air, groundwater, plants, and food. The principal commercial use of sulfate is in the chemical industry. Sulfate concentration in seawater is about 2,700 milligrams per liter (mg/L). It ranges from 3 to 30 mg/L in most freshwater supplies, although much higher concentrations (1000 mg/L) are found in some geographic locations.|
| conductivity  | float64| Pure water is not a good conductor of electric current rather’s a good insulator. Increase in ions concentration enhances the electrical conductivity of water. Generally, the amount of dissolved solids in water determines the electrical conductivity. Electrical conductivity (EC) actually measures the ionic process of a solution that enables it to transmit current. According to WHO standards, EC value should not exceeded 400 μS/cm.|
| organic_carbon   | float64 | Total Organic Carbon (TOC) in source waters comes from decaying natural organic matter (NOM) as well as synthetic sources. TOC is a measure of the total amount of carbon in organic compounds in pure water. According to US EPA < 2 mg/L as TOC in treated / drinking water, and < 4 mg/Lit in source water which is use for treatment |
| trihalomethanes   | float64 | THMs are chemicals which may be found in water treated with chlorine. The concentration of THMs in drinking water varies according to the level of organic material in the water, the amount of chlorine required to treat the water, and the temperature of the water that is being treated. THM levels up to 80 ppm is considered safe in drinking water.|
| turbidity   | float64 | The turbidity of water depends on the quantity of solid matter present in the suspended state. It is a measure of light emitting properties of water and the test is used to indicate the quality of waste discharge with respect to colloidal matter. The mean turbidity value obtained for Wondo Genet Campus (0.98 NTU) is lower than the WHO recommended value of 5.00 NTU.|
| potability   | int64 | Indicates if water is safe for human consumption where 1 = Potable and 0 = Not potable|




-------------------
 
 
#### Initial Hypotheses

> - **Hypothesis 1 -** 
> - alpha = .05
> - $H_o$: There is no association between solids and potability.  
> - $H_a$: There is an association between solids and potability. 

> - **Hypothesis 2 -** 
> - alpha = .05
> - $H_o$: There is no association between conductivity and potability.
> - $H_a$: There is an association between conductivity and potability.


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - Recommendations & next steps:







<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

##### **Plan ->** Acquire -> Prepare -> Explore -> Model -> Deliver
- [x] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [x] Acquire data from the kaggle Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- [x]  Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train two different classification models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [x] Create csv file with the water potability and the model's predictions.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

___

#### Acquire
> - Store functions that are needed to acquire data that will be used for the Water Potability Analysis
> - The final function will return a pandas DataFrame


#### Prepare
> - Store functions needed to prepare the Water Potability data
> - Import the prepare functions created by using prepare.py


#### Explore
> - Answer key questions, my hypotheseses, and figure out the features that can be used in a classification model to best predict driver for water potability


#### Model
> - Establish a baseline accuracy to determine if having a model is better than no model and train for at least 2 different models

#### Deliver
> - Deliver my findings in the presention.



<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [X] Read this README.md
- [ ] Download the aquire.py, prepare.py, and Water_Potability_final.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the Water_Potability_final.ipynb notebook