from flask import Flask,request,render_template,jsonify
from flask_cors import CORS,cross_originpip
import yagmail
import json


app=Flask(__name__)
CORS(app)   



@app.route('/',methods=['GET'])
def init():
    from cryptography.fernet import Fernet

    with open('filekey.key','rb') as key_file:
        key=key_file.read()
    fer=Fernet(key)

    with open('enc.txt','rb') as enc_file:
        enc=enc_file.read()
    
    decr=fer.decrypt(enc)
    eml_det=json.loads(decr)

    print(eml_det)

    jsondata={'status':'done'}
    jsondata=jsonify(jsondata)
    return jsondata
    
    



@app.route('/sendmail', methods=['POST'])
def sendmail():
    if request.method=='POST':
        data=request.get_json(force=True)

        print(data)


        model=data['MODEL']
        school=data['SCHOOL']
        battery=data['BATTERY']
        name=data['NAME']
        year = data['YEAR']
        rollno = data['ROLLNO']
        email= data['EMAIL']
        phone = data['PHONE']

        
        

        subj='Bonhomie Registration'

        body=f'''
        Hello {name},
        Your have been successfully registered for {model} & {battery}
        Thank You'''

        yag = yagmail.SMTP(user='sshadulla22@gmailcom',password='qjvr ctul qdmi aulg')

        yag.send(
            to=email,
            subject=subj,
            contents=body
        )

        print('MAIL SENT')
        jsondata={'status':'done'}
        jsondata=jsonify(jsondata)
        jsondata.headers.add('Access-Control-Allow-Origin', '*')
        return jsondata
        


if __name__=="__main__":
    app.run(debug=True)