from flask import Flask,render_template,request

app=Flask(__name__)

def flames_game(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    name3 = list(name1 + name2)
    for char in set(name1):
        while char in name2:
            name2 = name2.replace(char, '', 1)
            name3.remove(char)
            name3.remove(char) if char in name3 else None
    count = len(name3)
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    
    index = 0
    while len(flames) > 1:
        index = (index + count - 1) % len(flames)
        flames.pop(index)  

    result = flames[0]
    relation = ['Friends', 'Lovers', 'Admires', 'Marriage', 'Enemies', 'Siblings']
    relation_index = {'F': 0, 'L': 1, 'A': 2, 'M': 3, 'E': 4, 'S': 5}

    return relation[relation_index[result]]

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name1=request.form['name1']
        name2=request.form['name2'] 
        result=flames_game(name1,name2)
        return render_template('result.html',result=result)
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)  
