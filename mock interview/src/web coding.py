from flask import *
from src.dbconnection import *


app=Flask(__name__)
app.secret_key ="123"
@app.route("/")
def log():
    return  render_template("login index.html")


@app.route('/login',methods=['post', 'get'])
def login():
    username= request.form['textfield']
    password= request.form['textfield2']
    qry="select * from login where username=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return'''<script>alert("invalid");window.location='/'</script>'''
    elif res['type'] == 'admin':
        session['lid'] = res['id']
        return '''<script>alert(" welcome admin");window.location='/admin'</script>'''
    elif res['type'] == 'expert':
        session['lid'] = res['id']
        return'''<script>alert(" welcome expert");window.location='/expert'</script>'''
    elif res['type'] == 'candidate':
        session['lid'] = res['id']
        return '''<script>alert(" welcome candidates");window.location='/candidateshome'</script>'''
    else:
        return '''<script>alert("invalid");window.location='/'</script>'''






@app.route("/addandmanageexpert")
def addandmanageexpert():
    r="select*from expert"
    v = selectall(r)
    return  render_template("admin/ADD AND MANAGE EXPERT.html",val=v)


@app.route("/addingexpert",methods=['post'])
def addingexpert():
    return  render_template("admin/ADDING EXPERT.html")

@app.route("/addingexpert1",methods=['post'])
def addingexpert1():
    fname=request.form['textfield']
    lname = request.form['textfield10']
    email=request.form['textfield2']
    Phone=request.form['textfield3']
    place=request.form['textfield4']
    post=request.form['textfield6']
    pin=request.form['textfield7']
    username = request.form['textfield8']
    password = request.form['textfield9']
    qry="INSERT INTO `login` VALUES(NULL,%s,%s,'expert')"
    val=( username, password)
    id=iud(qry,val)
    qr="INSERT INTO expert VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    va=(str(id),fname,lname,Phone,place,post,pin,email)
    iud(qr,va)
    return '''<script>alert("success");window.location='/addandmanageexpert'</script>'''


@app.route("/edit_EXPERT")
def edit_EXPERT():
    id=request.args.get('id')
    session['EE_id']=id
    qry="select * from expert  WHERE L__id=%s"
    res=selectone(qry,id)

    return  render_template("admin/edit_EXPERT.html",val=res)

@app.route("/edit_EXPERT1",methods=['post'])
def edit_EXPERT1():
    fname=request.form['textfield']
    lname = request.form['textfield10']
    email=request.form['textfield2']
    Phone=request.form['textfield3']
    place=request.form['textfield4']
    post=request.form['textfield6']
    pin=request.form['textfield7']


    qr="UPDATE `expert` SET `first_name`=%s,`last_name`=%s,`Phone_no`=%s,`place`=%s,`post`=%s,`pin`=%s,`email`=%s WHERE L__id=%s"
    va=(fname,lname,Phone,place,post,pin,email,session['EE_id'])
    iud(qr,va)
    return '''<script>alert("success");window.location='/addandmanageexpert'</script>'''






@app.route("/admin")
def admin():
    return  render_template("admin/Admin.html")

@app.route("/sendreply")
def sendreply():
    return  render_template("admin/SEND REPLY.html")

@app.route("/viewcomplaint")
def viewcomplaint():
    qry="SELECT * FROM `complaint` JOIN `candidates` ON complaint.L_id=`candidates`.`L_id` "
    res=selectall(qry)
    return  render_template("admin/VIEW COMPLAINT.html",val=res)

@app.route("/viewfeedback")
def viewfeedback():
    qry="SELECT * FROM `feedback` join `candidates` ON feedback.L_id=`candidates`.`L_id`   "
    res=selectall(qry)
    return  render_template("admin/VIEW FEEDBACK.html",val=res)

@app.route("/addandmanagequestions")
def addandmanagequestions():
    qry="SELECT * FROM `question`"
    res=selectall(qry)
    return  render_template("expert/Add and manage questions.html",data=res)

@app.route("/editquestions")
def editquestions():
    qry="SELECT * FROM `test`"
    res=selectall(qry)
    qry1="SELECT * FROM `question` WHERE `Q_id`=%s"
    id = request.args.get('id')
    session['QN_id'] = id
    res1 = selectone(qry1, id)


    return  render_template("expert/Edit questions .html",data=res,val=res1)

@app.route("/editquestions1",methods=['post'])
def editquestion1():
    Question = request.form['textfield2']
    answer = request.form['textfield3']
    TID = request.form['select']

    qry = "UPDATE question SET Questions=%s,Answers=%s  ,`T_id`=%s WHERE `Q_id`=%s"
    va = (Question,TID,answer,session['QN_id'] )
    iud(qry, va)
    return '''<script>alert("success");window.location='/addandmanagequestions'</script>'''




@app.route("/addandmanagequestions2")
def addandmanagequestions2():
    return  render_template("expert/Add and manage questions 2.html")

@app.route("/addandmanagetest")
def addandmanagetest():
    qry="SELECT * FROM`test`JOIN `category`ON `category`.`Cat_id`=`test`.`Cat_id`"
    res=selectall(qry)
    return  render_template("expert/Add and manage Test.html",data=res)


@app.route("/addandmanagetest2",methods=['post'])
def addandmanagetest2():
    qry1 = "SELECT * FROM`test`JOIN `category`ON `category`.`Cat_id`=`test`.`Cat_id`"
    res1 = selectall(qry1)
    qry="SELECT * FROM `result` join `expert` ON result.L_id=`expert`.`L__id`   "
    val=selectall(qry)
    return  render_template("expert/Add and manage Test 2.html",v=val,val1=res1)

@app.route("/addtestcategory")
def addtestcategory():
    return  render_template("expert/Add Test Category.html")



@app.route("/expert")
def expert():
    return  render_template("expert/Expert.html")

@app.route("/viewnotification")
def viewnotification():
    q="SELECT * FROM `notification`  "
    v=selectall(q)
    return  render_template("expert/View Notification.html",val=v)

@app.route("/viewresult")
def viewresult():
    q="SELECT * FROM`result`JOIN `candidates`ON `result`.`L_id`=`candidates`.`L_id`JOIN`test`ON `test`.`T_id`=`result`.`T_id`"
    v=selectall(q)
    return  render_template("expert/View Result.html",val=v)

@app.route("/attendtest1")
def attendtest1():
    q = "select * from test"
    v = selectall(q)
    return  render_template("candidates/Attend test 1.html",val=v)

@app.route("/attendtest2")
def attendtest2():
    return  render_template("candidates/Attend Test 2.html")

@app.route("/candidateshome")
def candidates():
    return  render_template("candidates/canditates.html")

@app.route("/sendcomplaintandviewreply1")
def sendcomplaintandviewreply1():
    return  render_template("candidates/send complaint and view reply.html")

@app.route("/viewtestcategorycategory")
def viewtestcategorycategory():
    q = "SELECT * FROM `category`  "
    v = selectall(q)
    return  render_template("candidates/view test category-category.html",val=v)

@app.route("/viewtestcategorytest")
def viewtestcategorytest():
    return  render_template("candidates/view test category-test.html")

@app.route("/viewtestresult")
def viewtestresult():
    q = "SELECT * FROM `result`  "
    v = selectall(q)
    return  render_template("candidates/view test result.html",val=v)

@app.route("/sendcomplaintandviewreply")
def sendcomplaintandviewreply():
    return  render_template("send complaintand view replyt.html")


@app.route("/notification")
def notification():
    q="select * from notification"
    v=selectall(q)
    return  render_template("admin/notification.html",val=v)


@app.route("/notification2",methods=['post'])
def notification2():
    return  render_template("admin/notification2.html")

@app.route("/addnotification",methods=['post'])
def addnotification():
    send=request.form['textfield']
    qry="INSERT INTO `notification` VALUES(NULL,%s,curdate())"

    val=(send)
    iud(qry,val)
    return '''<script>alert("success");window.location='/notification'</script>'''



@app.route("/addtestcategory1",methods=['post'])
def addtestcategory1():
    add=request.form['textfield']
    qry="INSERT INTO `category` VALUES(NULL,%s,%s,curdate())"

    val=(session['lid'],add)
    iud(qry,val)
    return '''<script>alert("success");window.location='/expert'</script>'''

@app.route("/addandmanagetest1",methods=['post'])
def addandmanagetest1():
    test=request.form['textfield2']
    cat=request.form['select']
    qry="INSERT INTO `test` VALUES(NULL,%s,curdate(),%s)"

    val=(test,cat)
    iud(qry,val)
    return '''<script>alert("success");window.location='/expert'</script>'''


@app.route("/addandmanagequestion1",methods=['post'])
def addandmanagequestion1():
    Question=request.form['textfield2']
    answer=request.form['textfield3']
    TID=request.form['select']
    qry="INSERT INTO `question` VALUES(NULL,%s,%s,%s)"

    val=(Question,TID,answer)
    iud(qry,val)
    return '''<script>alert("success");window.location='/expert'</script>'''

@app.route("/addingcandidates")
def addingcandidates():
    return  render_template("candidates/candidate registration.html")

@app.route("/addingcandidate1",methods=['post'])
def addingcandidate1():
    fname=request.form['textfield']
    lname = request.form['textfield2']
    email=request.form['textfield4']
    Phone=request.form['textfield3']
    place=request.form['textfield5']
    post=request.form['textfield6']
    pin=request.form['textfield7']
    username = request.form['textfield8']
    password = request.form['textfield9']
    qry="INSERT INTO `login` VALUES(NULL,%s,%s,'candidate')"
    val=( username, password)
    id=iud(qry,val)
    qr="INSERT INTO candidates VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    va=(str(id),fname,lname,email,Phone,place,pin,post)
    iud(qr,va)
    return '''<script>alert("success");window.location='/'</script>'''

@app.route("/delete")
def delete():
    id=request.args.get('id')
    qry="delete from expert where L__id=%s"
    iud(qry,id)
    qry = "delete from `login` where id=%s"
    iud(qry, id)
    return '''<script>alert("Deleted");window.location='/addandmanageexpert'</script>'''

@app.route("/deletenotification")
def deletenotification():
    id=request.args.get('id')
    print(id)
    qry="delete from notification where N_id=%s"
    iud(qry,id)
    return '''<script>alert("Deleted");window.location='/notification'</script>'''

@app.route("/deletetest")
def deletetest():
    id=request.args.get('id')
    print(id)
    qry="delete from test where T_id=%s"
    iud(qry,id)
    return '''<script>alert("Deleted");window.location='/addandmanagetest'</script>'''

@app.route("/deletequestion")
def deletequestion():
    id=request.args.get('id')
    print(id)
    qry="delete from question where Q_id=%s"
    iud(qry,id)
    return '''<script>alert("Deleted");window.location='/addandmanagequestions'</script>'''

@app.route("/edittest")
def edittest():
    id = request.args.get('id')
    session['Tsr_id'] = id
    qry="SELECT * FROM category"
    res=selectall(qry)
    qry1="SELECT * FROM `test` WHERE `T_id`=%s"

    res1 = selectone(qry1, id)
    return  render_template("expert/test edit.html",data=res,val=res1)

@app.route("/edittest1",methods=['post'])
def edittest1():
    test = request.form['textfield2']
    cat = request.form['select']
    qry = "UPDATE test SET  `Test_name`=%s,`Cat_id`=%s WHERE `T_id`=%s"
    va = (test,cat,session['Tsr_id'] )
    iud(qry, va)
    return '''<script>alert("Updated");window.location='/addandmanagetest'</script>'''


@app.route("/reply")
def reply():
    id=request.args.get('id')
    session['cid'] = id
    return render_template("admin/SEND REPLY.html")


@app.route("/reply1",methods=['post'])
def reply1():
    reply=request.form['textfield']
    qry="UPDATE  `complaint` SET `reply`=%s WHERE  `C_id`=%s"
    val=(reply, session['cid'])
    iud(qry,val)
    return '''<script>alert("sended");window.location='/viewcomplaint'</script>'''
@app.route("/addquestion",methods=['post'])
def addquestion():
    qry="select*from test"
    res=selectall(qry)

    return  render_template("expert/Add and manage questions  2.html",val=res)
app.run(debug=True)















