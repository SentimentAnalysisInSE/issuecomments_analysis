Microsoft TextAnalytics is used to analyze the setiment of the different jira comments. the output from the API give both scores and assignes a label. We have used the label designated by mircosoft as our datas setiment label. 
In order to run Microwork.py you must have azure core and azure ai installed on the local machine.
once mirowork.py is run it will output the sores and label to the output that the user chooses utilizing >>

microwork.py -> converter.py

Converter.py then converts this output to just the label (positive negitive neutral) (mixed is assigned to neutral) to be put into a csv.
