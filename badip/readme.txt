Получить все ip GET:
/api/all_ip
>>>
Получить хорошие ip GET:
/api/good_ip
>>>
Получить плохие ip GET:
/api/bad_ip
>>>
Проверить ip GET:
/api/which_ip/?ip=192.168.1.6
>>> True (Не числится в базе или хороший)
>>> False (Числится в базе, плохой с жалобами)
Отправит жалобу на ip GET:
/api/is_ip_bad/?ip=192.168.1.6
>>> Your ip add in bad base