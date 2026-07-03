DI\_FLAG project in detail:





**"One of my projects is DI Flag Issues Prediction, an NLP-based text classification project developed using machine learning.**



**The objective of the project was to automatically identify whether an audit observation is related to a Data Integrity (DI) issue.**



**In pharmaceutical companies, internal audits and regulatory inspections generate thousands of observations. Quality teams manually review each observation to determine whether it represents a Data Integrity issue, such as missing records, incomplete documentation, unauthorized data changes, or audit trail problems. This manual process is time-consuming and may lead to inconsistencies.**



**To address this problem, I built a machine learning model that predicts the DI flag from the observation description.**



**I started by understanding the dataset, handling missing values, removing unnecessary columns, and preprocessing the text using techniques such as lowercasing, punctuation removal, stop-word removal, and lemmatization.**



**Since machine learning models cannot process raw text directly, I converted the cleaned text into numerical vectors using TF-IDF.**



**I trained multiple classification models, including Logistic Regression, Naive Bayes, and Linear SVM, and compared their performance. I also performed hyperparameter tuning to improve the model.**



**During evaluation, I used metrics such as accuracy, precision, recall, F1-score, and the confusion matrix because the dataset was imbalanced, with approximately 90% 'No' and 10% 'Yes' labels.**



**The final model can automatically classify new audit observations as DI or non-DI, helping quality teams prioritize reviews and reduce manual effort."**















This is a very common interview question, and the best answer depends on where you actually got the dataset. You should always answer truthfully—interviewers often ask follow-up questions.



Case 1: Your senior or company provided the dataset (recommended if true)



If your senior gave you the dataset as part of a company-related project, you can say:



"The dataset was provided by my senior as part of a real-world project. It contains pharmaceutical audit observations used for predicting Data Integrity (DI) issues. Since it was project data, I focused on understanding the domain, preprocessing the data, building the NLP pipeline, and training the classification model."



If they ask why it isn't publicly available:



"It was shared with me for learning and project development. Due to confidentiality, I can't share the dataset publicly, but I can explain its structure, preprocessing steps, and the complete machine learning pipeline."



This is a professional and credible answer.



Case 2: You downloaded it from a public source



If you actually downloaded it from a public source (such as Kaggle or another repository), simply say:



"I obtained the dataset from a public dataset repository. I selected it because it represents a real-world NLP classification problem in the pharmaceutical domain."



Be prepared to mention the source if they ask.



Case 3: You created the dataset yourself



If you created or combined the dataset:



"I created the dataset by collecting and preprocessing data from multiple sources for educational purposes."



Only say this if it's true.



If they ask, "Why did you choose this dataset?"



A strong answer is:



"I wanted to work on a real-world business problem instead of a standard sentiment analysis project. This dataset allowed me to build an NLP solution for automatically identifying Data Integrity issues, which has practical value in the pharmaceutical industry."



Based on what you've told me



From our earlier conversations, you mentioned that your senior asked you to work on this project. If that is correct, then this is the best answer:



"The dataset was provided by my senior as part of a real-world project in the pharmaceutical domain. I used it to build an NLP-based DI Flag prediction model. Although I cannot publicly share the dataset because it is project-related, I can explain the dataset structure, preprocessing, feature engineering, model development, and evaluation in detail."



This answer is honest, professional, and usually satisfies interviewers.



One more piece of advice



Interviewers often ask this immediately after you answer where the dataset came from:



"What do the rows and columns represent?"



You should be ready to explain:



What one row represents (e.g., a single audit observation).

What the important columns are (especially ObsFullDescription and DI\_flag).

Why DI\_flag is the target variable.

Which features you used and which you dropped.



Being able to explain the dataset at that level often leaves a stronger impression than simply discussing the model.



i got this dataset from my coaching center



That's perfectly fine. In fact, many students work on datasets provided by their coaching institutes. The important thing is to be honest. Never say it came from a company or Kaggle if it didn't.



If the interviewer asks, "Where did you get this dataset?"



You can answer:



"I received this dataset from my coaching institute as part of a real-world machine learning project. The objective was to understand the business problem, perform data preprocessing, build an NLP-based classification model, and predict whether an audit observation should be flagged as a Data Integrity issue."



If they ask, "Is it a real dataset?"



You can say:



"Yes, I was informed that it is based on real pharmaceutical audit observations. The dataset was shared by my coaching institute for educational purposes. I don't know its exact source, but I focused on understanding the business problem and developing the complete machine learning solution."



This is an honest answer. Don't claim that it came directly from a pharmaceutical company unless you know that for sure.



If they ask, "Why did you choose this project?"



You can answer:



"My coaching institute provided several project options, and I chose this one because it solves a real business problem in the pharmaceutical domain. It also gave me hands-on experience with NLP, text preprocessing, feature engineering, model building, and handling an imbalanced classification dataset."



If they ask, "Did you understand the domain, or did you just build the model?"



This is where you can impress them:



"Initially, I wasn't familiar with the pharmaceutical domain, so I first studied what Data Integrity means, why audit observations are recorded, and how a DI flag is used in quality assurance. Once I understood the business problem, I analyzed the dataset, performed preprocessing, built the NLP pipeline, trained multiple models, and evaluated them using appropriate metrics."



This shows that you didn't just write code—you took the time to understand the business context, which interviewers appreciate.



One suggestion



Since this project will be on your resume, don't stop at knowing the code. Be prepared to answer questions like:



What is Data Integrity?

Why is this prediction useful?

Why did you choose TF-IDF?

Why did you use the selected classifier?

Why is the dataset imbalanced, and how did you handle it?

Why did you evaluate precision, recall, and F1-score instead of only accuracy?

What challenges did you face?

How would you improve the project if given more time or resources?



If you can answer these confidently, you'll come across as someone who truly understands the project rather than someone who only implemented it.



give answers to all these questions



Absolutely. Since this project is on your resume, you should prepare as if you're defending it in an interview. Below are answers that sound natural and demonstrate genuine understanding.



1\. Tell me about your DI Flag Issues Prediction project.



"My project is an NLP-based text classification system that predicts whether a pharmaceutical audit observation is related to a Data Integrity (DI) issue.



In pharmaceutical companies, auditors and quality assurance teams record thousands of observations during inspections. Manually reviewing every observation to identify Data Integrity issues is time-consuming and may lead to inconsistencies. The objective of my project was to automate this process using machine learning.



I started by understanding the dataset, performed data cleaning and text preprocessing, converted the observation descriptions into numerical vectors using TF-IDF, trained multiple machine learning models, compared their performance, and selected the best-performing model. Finally, I evaluated the model using metrics such as accuracy, precision, recall, F1-score, and the confusion matrix."



2\. What is Data Integrity?



"Data Integrity means ensuring that data remains accurate, complete, consistent, reliable, and unaltered throughout its lifecycle.



In the pharmaceutical industry, manufacturing and laboratory records must be trustworthy because they directly impact product quality and patient safety.



Examples of Data Integrity issues include unauthorized modification of records, missing batch documentation, incomplete laboratory records, or missing audit trails."



3\. Why is predicting DI issues important?



"Large pharmaceutical companies generate thousands of audit observations every year. Manually reviewing every observation requires significant time and effort.



A prediction model helps quality teams quickly identify observations that are likely related to Data Integrity issues. This reduces manual effort, improves consistency, and allows experts to prioritize high-risk cases."



4\. Why did you use NLP?



"The most important feature in the dataset is the observation description, which is unstructured text.



Machine learning algorithms cannot process raw text directly, so NLP techniques are required to clean the text, remove unnecessary words, and convert it into numerical features that can be used for classification."



5\. Explain your workflow.



"My workflow consisted of:



Understanding the business problem.

Exploring the dataset.

Cleaning the data by handling missing values and duplicates.

Preprocessing the text through lowercasing, punctuation removal, stop-word removal, and lemmatization.

Converting text into numerical vectors using TF-IDF.

Splitting the data into training and testing sets.

Training multiple classification models.

Performing hyperparameter tuning.

Evaluating the models.

Saving the best-performing model for prediction."

6\. Why did you use TF-IDF instead of Bag of Words?



"Bag of Words simply counts word frequencies, whereas TF-IDF considers both the frequency of a word within a document and how common that word is across all documents.



Words that appear in almost every document receive lower importance, while words that are unique to certain observations receive higher importance.



This usually results in better feature representation for text classification."



7\. What preprocessing did you perform?



"I performed:



Converted text to lowercase.

Removed punctuation.

Removed special characters.

Removed stop words.

Performed lemmatization.

Removed unnecessary spaces.

Converted the cleaned text into TF-IDF vectors."

8\. Why did you choose Logistic Regression / Naive Bayes / SVM?



(Modify according to your final model.)



If Logistic Regression:



"Logistic Regression is a strong baseline for text classification. It is simple, fast, handles high-dimensional sparse TF-IDF features well, and often performs competitively on NLP tasks."



If Naive Bayes:



"Naive Bayes works well with text because it estimates class probabilities based on word occurrences. It is computationally efficient and commonly used for document classification."



If Linear SVM:



"Linear SVM performs well on high-dimensional text data and is effective at finding a decision boundary that separates classes."



9\. Why did you train multiple models?



"Different algorithms have different strengths. Instead of assuming one model would perform best, I trained multiple models, compared their evaluation metrics, and selected the one that provided the best balance between accuracy, precision, recall, and F1-score."



10\. Why did you perform hyperparameter tuning?



"Hyperparameter tuning helps optimize model performance by selecting the best parameter values rather than relying on default settings.



I used techniques such as GridSearchCV or RandomizedSearchCV to identify the best hyperparameters."



11\. Why didn't your accuracy improve much?



"The original dataset contained approximately 500,000 records, but due to hardware limitations I trained on a representative 10% sample.



Using a smaller dataset limited the amount of information available to the model. Additionally, the dataset was highly imbalanced, with around 90% 'No' labels and 10% 'Yes' labels, which also affected model performance."



12\. Why didn't you use the full dataset?



"My laptop did not have sufficient memory and processing power to efficiently process the complete dataset.



Therefore, I used a random 10% sample for training. If more computational resources were available, I would train on the complete dataset, which could potentially improve the model's generalization."



13\. How did you sample the data?



"I selected a random sample using pandas' sample() function with a fixed random state to ensure reproducibility."



14\. Why is your dataset imbalanced?



"The dataset naturally contains many more non-DI observations than DI observations. This reflects the real-world scenario, where Data Integrity issues are relatively less frequent than normal audit observations."



15\. How did you handle class imbalance?



If you didn't use any balancing technique:



"I identified that the dataset was imbalanced and therefore evaluated the model using precision, recall, F1-score, and the confusion matrix instead of relying only on accuracy. If I were to improve the project further, I would experiment with class weighting or oversampling techniques such as SMOTE where appropriate."



Don't claim you used SMOTE if you didn't.



16\. Why isn't accuracy enough?



"In an imbalanced dataset, a model can achieve high accuracy simply by predicting the majority class.



Therefore, I also evaluated precision, recall, and F1-score to measure how well the model identified the minority class."



17\. What is Precision?



"Precision measures how many observations predicted as DI issues were actually DI issues.



It answers the question: 'When the model predicts a DI issue, how often is it correct?'"



18\. What is Recall?



"Recall measures how many actual DI issues were correctly identified by the model.



It answers the question: 'Out of all true DI issues, how many did the model detect?'"



19\. What is F1-score?



"F1-score is the harmonic mean of precision and recall. It is useful when both false positives and false negatives are important, especially in imbalanced datasets."



20\. What challenges did you face?



"The main challenges were:



Processing a very large dataset with limited hardware.

Handling class imbalance.

Understanding the pharmaceutical domain before building the model.

Selecting the most suitable preprocessing steps and classification algorithm."

21\. How would you improve this project?



"If I had access to better computational resources, I would:



Train on the complete dataset.

Experiment with transformer-based models such as BERT.

Address class imbalance using class weighting or resampling.

Deploy the model as a web application or API.

Continuously retrain the model with new audit observations."

22\. Where did you get the dataset?



"I received the dataset from my coaching institute as part of a project. It was provided for educational purposes, and I used it to understand the business problem and build an end-to-end NLP classification solution."



23\. What did you learn from this project?



"This project helped me understand how to solve a real-world NLP classification problem. I gained experience in text preprocessing, TF-IDF feature extraction, handling imbalanced datasets, comparing machine learning models, hyperparameter tuning, and selecting evaluation metrics appropriate for business problems."



24\. Why should we hire you based on this project?



"This project gave me experience beyond simply training a model. I learned to understand the business problem, preprocess unstructured text, build and evaluate machine learning models, and explain results from both technical and business perspectives. It also taught me how to work within practical constraints, such as limited computational resources."



⭐ Most Important Tip



During interviews, don't make your answers sound memorized. Use this simple structure for almost every project-related question:



Business perspective – Why does the problem matter?

Technical perspective – What techniques did you use?

Your contribution – What decisions did you make and what did you learn?



Interviewers are often more impressed by candidates who can connect the business problem to the technical solution than by candidates who only list algorithms and libraries.

