import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from pdfminer.high_level import extract_text
import re
def cleanResume(resumeText):
    resumeText = re.sub('http\S+\s*', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#\S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@\S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText) 
    resumeText = re.sub('\s+', ' ', resumeText)  # remove extra whitespace
    return resumeText

m={15: 'Jave Developer', 23: 'Testing', 8: 'DevOps Engineer', 20: 'Python Developer', 24: 'Web Design', 12: 'HR',
13: 'Hadoop', 3: 'Blockchain', 10: 'ETL Developer', 18: 'Operations Manager', 6: 'Data science', 22: 'Sales', 
16: 'Mechanical Engineer', 1: 'Arts', 7: 'Database', 11: 'Electrical Engineer', 14: 'Health & Fitness', 19: 'PMO',
4: 'Business Analyst', 9: '.Net Developer', 2: 'Automation', 17: 'Network Security Engineer', 21: 'SAP Developer',
5: 'Civil Engineer', 0: 'Advocate'}

def resume_screener(resume_path):
  loaded_model = pickle.load(open('/content/resume_screener.pkl', 'rb'))
  txt=extract_text(resume_path)
  res_clean=cleanResume(txt)
  feat=word_vectorizer.transform([res_clean])
  return m[loaded_model.predict(features)[0]]

resume_screener('/content/resume_dataScience.pdf')
