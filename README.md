# Resume-parser-screener

#### Extracting Name, Phone Number, Email, Matching Skills from JD database, College, and Grade. 
#### Screener model is used to predict if the resume is fit for the role of Data Scientist.
By : [Tanishq Selot](https://github.com/tanishq150802)

## Requirements
* Python 3.10
* nltk
* pdfminer.six
* doc2txt
* Regex
* sklearn
* spacy
* Stanford NER (Name Entity Recognition)

All the parser code is contained within **Resume_parser.ipynb**. 
The screener code is contained within **Resume_screener.ipynb**.

### Parser
* For converting the resume file into text: doc2txt (for .docx) and pdfminer.six (for .pdf).
* Stanford NER perfomed the best while extracting Name and matching skills.
* NLTK performs satisfactorily while extracting any field.
* Feel free to experiment more!

### Screener
* Categories -
  #### ['Data Science' 'HR' 'Advocate' 'Arts' 'Web Designing' 'Mechanical Engineer' 'Sales' 'Health and fitness' 'Civil Engineer' 'Java Developer' 'Business Analyst' 'SAP Developer' 'Automation Testing' 'Electrical Engineering' 'Operations Manager' 'Python Developer' 'DevOps Engineer' 'Network Security Engineer' 'PMO' 'Database' 'Hadoop' 'ETL Developer' 'DotNet Developer' 'Blockchain' 'Testing']
* Text is cleaned using Regex - removing hashtags, URLs, mentions etc.
* Label Encoder to covert categorical labels into numerical values.
* Tf-Idf Vectorizer for numerical representation of resume text.
* K-Nearest Neighbour results:

| Training Accuracy  | Testing Accuracy |
| ------------- | ------------- |
| 99 % | 98 %  |

![image](https://github.com/tanishq150802/Resume-parser-screener/assets/81608921/b49fa963-6a8a-43e2-a593-c943fdd68c8f)

### Future Plan

I plan on deploying the screener on a django Web App.

### References
* [Stanford NER .jar file and caseless models](https://nlp.stanford.edu/software/CRF-NER.shtml)
* [Screener Dataset](https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset)
