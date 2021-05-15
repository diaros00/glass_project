from django.shortcuts import render,redirect
from .models import Defect , modelGlass
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import UserProfile
from django.core.files.storage import FileSystemStorage




def hello(request):
    #Query
    data_defect = Defect.objects.all()
    data_glass = modelGlass.objects.all()
    return render(request,'index.html',{'defects':data_defect,'modelGlasss':data_glass})

def createForm(request):
    return render(request,'form.html')


def loginForm(request):
    return render(request,'login.html')

def addUser(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    department = request.POST['department']
    shift = request.POST['shift']
    username = request.POST['username']
    password = request.POST['password']
    rePassword = request.POST['rePassword']


    if password == rePassword :
        if User.objects.filter(username=username).exists():
            messages.error(request,'UserName นี้มีคนใช้แล้ว')
          
            return redirect('/createForm')
        else:  
            user = User.objects.create_user(
            username = username,
            password = password,
            first_name = firstname,
            last_name = lastname


            )
            user.save()

            profile = UserProfile.objects.create(
            user_id=user.id,
            department = department,
            shift =  shift

            )
            profile.save()
          

            messages.success(request,'ลงทะเบียนเรียบร้อย')
            return redirect('/')
            
    else:
        messages.error(request,'password ไม่ตรงกัน')
        return redirect('/createForm')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
 
    
    #check username password
    user = auth.authenticate(username=username,password=password)

    if user is not None :
        auth.login(request,user)
        return redirect('/home')
    else :
        messages.error(request, 'username หรือ password ไม่ถูกต้อง')
        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')



def addDefect(request):
    defect_name = request.POST['defect_name']

    defect_add = Defect.objects.create(
            defect_name = defect_name

            )
    defect_add.save()

    messages.success(request,'Add defect successfully.')

    return redirect('/home')


def addModel(request):
    
    model_code = request.POST['model_code']
    model_name = request.POST['model_name']
    model_desc = request.POST['model_desc']
   

    model_add = modelGlass.objects.create(
    model_code = model_code,
    model_name = model_name,
    model_desc = model_desc

    )
    


    file_img = request.FILES['img']
    file_img_name = request.FILES['img'].name
    fs = FileSystemStorage()
    filename = fs.save(file_img_name,file_img)
    upload_file_url = fs.url(filename)


    model_add.model_image = upload_file_url
    model_add.save()

    messages.success(request,'Add Model successfully.')

    return redirect('/home')

def collector(request):
    data_defect = Defect.objects.all()
    data_glass = modelGlass.objects.all()
    
    return render(request,'collector.html',{'defects':data_defect,'modelGlasss':data_glass})


def choose_defect_on_glass(request):
    data_defect = Defect.objects.all()
    datepick = request.POST['datepicker']
    shift = request.POST['shift']
    inputModelDesc = request.POST['inputModelDesc']
    # filter โดย ID ของ modelGlass แล้วมาเก็บใน objModelDesc โดยดึง ทั้งแถวมาเลย
    objModelDesc = modelGlass.objects.get(id=inputModelDesc)

    # data_defect = Defect.objects.all()
    # data_glass = modelGlass.objects.all()
    # objModelDesc.model_desc    objModelDesc.model_name    objModelDesc.model_code     เรียกชื่อ attribute (หัว column) โดย ใส่ .

   

    return render(request,'choose_defect_on_glass.html',{'shift':shift,'datepick':datepick,
    'inputModelDesc':objModelDesc.model_desc,
    'inputModelName':objModelDesc.model_name,
    'inputModelCode':objModelDesc.model_code,
    'inputModelImage':objModelDesc.model_image,
    'defects':data_defect})

def add_defect(request):
    
    data_defect = Defect.objects.all()

    datepick = request.POST['datepick']
    shift = request.POST['shift']

    inputModelDesc = request.POST['inputModelDesc']
    inputModelName = request.POST['inputModelName']
    inputModelCode = request.POST['inputModelCode']
    inputModelImage = request.POST['inputModelImage']
    inputDefectP11 = request.POST['inputDefectP11']
    inputDefectP12 = request.POST['inputDefectP12']
    objModeldefect = Defect.objects.get(id=inputDefectP12)
    

    # data_defect = Defect.objects.all()
    # data_glass = modelGlass.objects.all()

    # objModelDesc.model_desc    objModelDesc.model_name    objModelDesc.model_code     เรียกชื่อ attribute (หัว column) โดย ใส่ .
    messages.success(request,'Add defect > ' + objModeldefect.defect_name + ' < in model > ' + inputModelCode + ' < successfully.')
    return render(request,'choose_defect_on_glass.html',{'shift':shift,'datepick':datepick,
    'inputModelDesc':inputModelDesc,
    'inputModelName':inputModelDesc,
    'inputModelCode':inputModelCode,
    'inputModelImage':inputModelImage,
    'defects':data_defect,
    'inputDefectP12_return':objModeldefect.defect_name })

    

    





