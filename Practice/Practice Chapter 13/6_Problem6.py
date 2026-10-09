#Run pip freeze for the system interpreter.Take the contente and create a similar virtualenv.

'''
pip freeze > requirements.txt
virtualenv tanzinaenv
pip install pandas
pip install pyjokes
pip install -r .\requirements.txt
'''
