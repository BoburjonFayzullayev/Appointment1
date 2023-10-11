# Appoinment 

Bu proyekt tibbiy ko'rik va davolanishdagi bemorlarni uchrashuvga tayinlash uchun ishlab chiqildi. Uchrashuv shifokor tomonidan yaratiladi va tegishli hujjatlarni o'z ichiga oladi.
Ushbu hujjat bemor, shifokor, tashxis hamda bemor murojaat qilishi kerak b'lgan muassasa haqida ma'lumotlar bo`ladi.


## O'rnating

Proyektni o'rnating:

1. Bu proyektni o'zingizning kompyuteringizda yoki serverda yuklab oling.
2. Proyekt katalogiga o'ting `cd proyekt_nomi`.
3. Virtual muhitni yaratish uchun `python -m venv venv` komandasi orqali o'zingiz uchun yangi virtual muhit yarating.
4. Virtual muhitni faollashtirish uchun (Windows uchun) `venv\Scripts\activate`, (Mac/Linux uchun) `source venv/bin/activate` komandalarini ishga tushiring.
5. Proyektning talqinlarini o'rnatish uchun `pip install -r requirements.txt` komandasini bajarib chiqing.

## Sozlashlar

Proyekt sozlashlari:

1. `settings.py` faylini oching va proyekt sozlashlarini sozlang.
2. Ma'lumotlar bazasini o'rnatish va migroatsiyalarni bajarish uchun `python manage.py migrate` komandasini ishga tushiring.

## Ishga tushirish

Proyektni ishga tushirish:

1. `python manage.py runserver` komandasi orqali loyihani ishga tushiring.
2. Brauzeringizda [http://http://127.0.0.1:8000/api/](http://localhost:8000/api/) manzilini oching va API ga kirishingiz mumkin.

## API Tavsifi

Bu proyekt ...
Bu API quyidagi ma'lumotlarni qo'llab-quvvatlayadi:

* `id` (integer): Ma'lumotning identifikatori.
* `identifier_system` (string): Ma'lumot identifikatsiyasi uchun tizim manzili (URL).
* `identifier_value` (string): Ma'lumot identifikatsiyasi uchun qiymat (20 belgidan kam bo'lishi kerak).
* `patient` (string): Kasallik ro'yxatdan o'tkazilgan kasalning identifikatori (10 raqamdan tashkil topgan, "1-9" orqali boshlanishi shart).
* `practitioner` (string): Davolanayotgan shifokorning identifikatori (10 raqamdan tashkil topgan, "1-9" orqali boshlanishi shart).
* `organization` (string): Davolangan tashkilotning identifikatori (10 raqamdan tashkil topgan, "1-9" orqali boshlanishi shart).

## Endpoynlar

### `POST /api/`

Bu endpoyni orqali yangi ma'lumotni yuborish mumkin. Ma'lumotlarni yuborish uchun quyidagi JSONni foydalaning:

```json
{
    "id": 1,
    "identifier_system": "https://example.com",
    "identifier_value": "123456",
    "patient": "9876543210",
    "practitioner": "1234567890",
    "organization": "2345678901"
}
```
 ## Qo'llanmalar
Bu proyekt yaratishda quyidagi qo'llanmalardan foydalanildi:

Django Framework
Django REST framework