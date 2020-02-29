from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from api.models import Ip_list, User_code


def index(request):
    input_code = request.GET['code']  # Входящий код  на проверку
    codes = User_code.objects.all()
    for code in codes:
        print(input_code)
        print(code.code)

        if input_code == code.code: #если код валидный
            if request.path.find(r"bad_ip") != -1:
                json = [{"ip": ip.ip, "type": ip.type} for ip in Ip_list.objects.filter(type=False)]
                print(json)
                return JsonResponse(json, safe=False)
            elif request.path.find(r"good_ip") != -1:
                json = [{"ip": ip.ip, "type": ip.type} for ip in Ip_list.objects.filter(type=True)]
                return JsonResponse(json, safe=False)
            elif request.path.find(r"all_ip") != -1:
                json = [{"ip": ip.ip, "type": ip.type} for ip in Ip_list.objects.filter()]
                return JsonResponse(json, safe=False)
            elif request.path.find(r"which_ip") != -1:
                input_ip = request.GET['ip'] # Входящий Ip  на проверку
                for ip in Ip_list.objects.filter(type=False): # Возьмем плохие ip
                    if input_ip == ip.ip: # Если входящий плохой
                        return HttpResponse('False')
                        break
                else:
                    return HttpResponse('True')
            elif request.path.find(r"is_ip_bad") != -1:
                input_ip = request.GET['ip']  # Входящий Ip  жалоба
                s = Ip_list(ip=input_ip, type=False)
                s.save()
                return HttpResponse('Your ip add in bad base')
            else:

                documentation = 'doc.html'
                return HttpResponse(f"""There are bad ip here, 
                check out the API documentation at:<a href="{documentation}">HERE</a>
                For all questions you can contact:
                 <b>@DoctorXR</b>""")
        else:
            pass
    else:
        return HttpResponse("доступ запрещен, неверный SecretKey")

