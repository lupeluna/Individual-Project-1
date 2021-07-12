# Water-Potability-Project
______________________

Hello,

Welcome to the README file for my "Water Potability Project"

Here, you will find my work on working through the pipeline and will also find the data dictionary to help offer more insight to the variables being used.

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
| hardness   | float64 | Whether one is a senior or not|
| solids   | float64 | How many months a customer had service|
| chloramines   | float64 | total charges since day 1|
| sulfate  | float64| Yes = Churn, No = Not Churned|
| conductivity  | float64| total_charges / tenure_in_months|
| organic_carbon   | float64 | tenure_in_months / 12|
| trihalomethanes   | float64 | 1 = Churn, 0 = Not Churned|
| turbidity   | float64 | no partner & no dependents|
| potability   | int64 | 1 = has phone lines, 0 = No phone|




-------------------
 
 
#### Initial Hypotheses

> - **Hypothesis 1 -** I rejected the Null Hypothesis; there is a difference.
> - alpha = .05
> - $H_o$: There is no association between service types and churn.  
> - $H_a$: There is an association between service types and churn. 

> - **Hypothesis 2 -** I rejected the Null Hypothesis; there is a difference.
> - alpha = .05
> - $H_o$: There is no association between tenure types and churn.
> - $H_a$: There is an association between tenure types and churn.


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Executive Summary - Conclusions & Next Steps
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - Recommendations & next steps:

I would recommend a employer discount to large companies to entice their employees to have service with us and bring in large amounts of customers.
A feature I would have liked to create would be a column based on the number of services a customer has. I believe that the more services a person has, the less likely will leave the more services they have.
I believe an age column would be helpful between senior_citizens and not_senior to direct our marketing appropriately.
Another column of information that could be helpful is area of residence to see if perhaps there is a concentration of where churn is occuring







<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

##### **Plan ->** Acquire -> Prepare -> Explore -> Model -> Deliver
- [x] Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- [x] Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- [x]  Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train three different classification models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [x] Create csv file with the customer id, the probability of churn, and the model's predictions.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

___

#### Acquire
> - Store functions that are needed to acquire data  that will be used for the Telco Churn Analysis
> - The final function will return a pandas DataFrame


#### Prepare
> - Store functions needed to prepare the Telco data
> - Import the prepare functions created by using .prepare.py


#### Explore
> - Answer key questions, my hypotheseses, and figure out the features that can be used in a classification model to best predict driver for churn


#### Model
> - Establish a baseline accuracy to determine if having a model is better than no model and train for at least 3 different models

#### Deliver
> - Deliver my findings in the presention.



<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [X] Read this README.md
- [ ] Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_report.ipynb notebook