PolicyPulse AI – Final Project README

Project Overview:
-----------------
PolicyPulse AI is a real-time government policy analysis agent that helps users understand the impact and progress of U.S. congressional bills. It uses a combination of prediction modeling, summarization, and user personalization.

We built:
- A prediction model using PySpark (TF-IDF + logistic regression)
- Summarization using Mistral 7B (LLM)
- Retrieval-Augmented Generation (RAG) using LangChain for context-based outputs
- A Streamlit app interface where users can interact with these features

Folder Contents:
----------------
- app.py ......................... Main Streamlit app
- spark_model.py ................. PySpark model for bill passage prediction
- requirements.txt ............... Python libraries needed to run the app
- final_report.pdf ............... Final written report (includes explanation, results, and analytics framework)
- final_presentation.pdf ......... Slide deck for our presentation

Folders:
- data/
    - topic_trends_by_year.csv ... Dataset used for visualizing historical topic trends
- utils/
    - congress_api.py ............ Pulls bill data from Congress API
    - mistral.py ................. Summarization using Mistral 7B
    - rag.py ..................... RAG-based response generator using LangChain
    - predict.py ................. Prediction helper functions
    - user_impact.py ............. Personalization logic for user roles and regions

How to Run the App:
-------------------
1. Open terminal or command prompt
2. Navigate to this folder using `cd` command
3. Run the following commands:

   pip install -r requirements.txt  
   streamlit run app.py

Note: You’ll need an internet connection to query real-time data from the Congress API.

Additional Notes:
-----------------
- We used only one structured dataset (topic_trends_by_year.csv) for historical topic visualizations.
- The app is modular, allowing future updates with new APIs or models.
- Any "__MACOSX" folders were automatically created and can be ignored or deleted.

Team Members:
-------------
Rupesh, Emma, Mandovi, Afnan, Guangwei

Thank you for reviewing our project!
