# المطلوب:
# كتابة برنامج للمعلمات، يقوم هذا البرنامج ب:
# ١- يظهر في البداية التعليمات للمعلمة، كالتالي:
# "Choose one: students_names, student_score, students_count"
# ٢- ثم يطلب من المعلمة ادخال المعلومات المطلوبة: اسم الطالب٫ اسم الصف٫ او كلاهما، بحسب المطلوب في ال function.
# ٣- البرنامج يحتوي على ثلاث functions:
# ١) students_names
# تظهر قائمة بأسماء الطلاب في الصف٫ تأخذ ١ argument: اسم الصف
# ٢) student_score
# تظهر مجموع علامات طالب في صف معين٫ تأخذ ٢ arguments: اسم الصف، واسم الطالب
# ٣) student_count
# تظهر عدد الطلاب في الصف، تأخذ ١ argument: اسم الصف
# ٤- بعد اظهار النتيجة نطلب من المعلمة إدخال done إذا انتهت ويغلق البرنامج٫ أو إدخال more لتقوم باختيار function اخرى لتنفيذها، فتظهر الرسالة الاولى:
# "Choose one: students_names, student_score, students_count"
# القواميس المستخدمة لتخزين المعلومات، أرجو نسخها كما هي:
# grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}
# grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}
# grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}
# قومي بتخزين الحل باسم week4.py باستخدام محرر النصوص
# ثم قومي برفع الملف في الاستمارة ادناه

grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}
grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}
grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}
def start():
    query=input("Choose one: students_names, student_score, students_count: ")
    if query=="students_names":
        students_names()
    elif query=="student_score":
        student_score()
    elif query=="students_count":
        student_count()
    else:
        print("Enter a valid input")

def q2():
    query2= input("Please type done if you finished, or more for another query: ")
    if query2=="done":
        exit()
    elif query2=="more":
        start()
    else:
        print("Input is not valid")

def students_names():
    class_name=input("Please Enter Class Name: ")
    if class_name=="grade_one":
        print(list(grade_one.keys()))
    elif class_name=="grade_two":
        print(list(grade_two.keys()))
    elif class_name=="grade_three":
        print(list(grade_three.keys()))
    else:
        print("Input is not valid")
    q2()

def student_score():
    class_name=input("Please Enter Class Name: ")
    student_name=input("Please Enter Student Name: ")
    if class_name=="grade_one":
        if student_name in grade_one:
            print (sum(grade_one.get(student_name)))
        else:
            print ("Name not found")
    elif class_name=="grade_two":
        if student_name in grade_two:
            print (sum(grade_two.get(student_name)))
        else:
            print ("Name not found")
    elif class_name=="grade_three":
        if student_name in grade_three:
            print (sum(grade_three.get(student_name)))
        else:
            print ("Name not found")
    else:
        print('Input is not valid')
    q2()

def student_count():
    class_name=input("Please Enter Class Name: ")
    if class_name=="grade_one":
        print(len(grade_one))
    elif class_name=="grade_two":
        print(len(grade_two))
    elif class_name=="grade_three":
        print(len(grade_three))
    else:
        print('Input is not valid')
    q2()
while True:
    start()
