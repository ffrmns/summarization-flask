<<<<<<< HEAD
version https://git-lfs.github.com/spec/v1
oid sha256:573ead432d0fa771c3d4988b3916d6898342496304f6afac08339403f8eebb0b
size 3369
=======
#importing libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
from transformers import T5ForConditionalGeneration
from transformers import T5Tokenizer
from transformers import pipeline
#creating the flask object
app = Flask(__name__)
#loading the model weights
model = T5ForConditionalGeneration.from_pretrained('model') # the path to .bin and config.json
tokenizer = T5Tokenizer.from_pretrained('model')
me = pipeline('summarization', model=model, tokenizer=tokenizer)

@app.route('/summarize',methods=['POST'])
def summarize():
    message_sum = request.form['message_sum']
    ARTICLE = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York. A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband. Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other. In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage. Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the 2010 marriage license application, according to court documents. Prosecutors said the marriages were part of an immigration scam. On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further. After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002. All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say. Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages. Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted. The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali. Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force. If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18. """
    dropdown = message_sum #@param ["text", "artikel", "ARTICLE"] {type:"raw"}
    output = me(dropdown, max_length=130, min_length=5, do_sample=False)[0]['summary_text']
    outputs = 'The summarization is: '+output
    return render_template('index.html', summarization_text=outputs , value=message_sum)
 

#create routes
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
>>>>>>> non-lfs-code
