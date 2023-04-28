# Syntax Tree permutations 

<p>This API is created for making some text more unique by changing it's syntax tree.
Say we have NP node in syntax tree, which also has child NP nodes separated by (,,) or CC nodes. We can make text more unique by swapping these NP nodes between each other. In such a case, meaning of a text won't be lost</p>

To run this application you need to have Python(>=3.9) with flask and nltk libraries. To install flask and nltk, use these commands
```
  pip install flask
  pip install nltk
  ```
  
To run application, open console in directory with app.py and tree_opearions.py files and type
```
flask run --port=<port>
```
after = you have to write port, on which you want this application to run 
