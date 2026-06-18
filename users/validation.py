import re

def validate_phone_number(phone_number: str) -> str | None:
    # Faqat raqamlarni qoldiramiz
    clean_phone = re.sub(r'\D', '', str(phone_number))

    # Raqam uzunligini tekshirish va xalqaro kodni (998) yuklash
    if len(clean_phone) == 12 and clean_phone.startswith("998"):
        res = clean_phone
    elif len(clean_phone) == 9:
        res = "998" + clean_phone
    else:
        return None

    # O'zbekistondagi barcha faol mobil va shahar operatorlari prefikslari (2026-yil holatiga)
    # Beeline, Ucell, Mobiuz, Uztelecom, Humans va shahar raqamlari
    valid_prefixes = {
        # Mobil operatorlar
        '33', '88', '90', '91', '93', '94', '95', '97', '98', '99', 
        '20', '77', '50', '55', '70', '75', '10', '11', '12',
        # Shahar va hududiy raqamlar (ixtiyoriy, agar kerak bo'lsa)
        '71', '55', '61', '62', '65', '66', '67', '69', '72', '73', '74', '76', '79'
    }
    
    # Prefiksni tekshirish (3- va 4-indekslar)
    if res[3:5] in valid_prefixes:
        # Agar xohlasangiz, bu yerda "+" belgisi bilan qaytarishingiz mumkin: f"+{res}"
        return res
    
    return None


import re

def validate_https_url(url):
    # Faqat https:// bilan boshlanadigan URL andozasi
    https_pattern = re.compile(
        r'^https://'  # Qat'iy ravishda faqat https:// bilan boshlanishi shart
        r'(?:(?:[A-Z0-7](?:[A-Z0-7-]{0,61}[A-Z0-7])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-7-]{2,}\.?)|' # Domen (masalan: kun.uz)
        r'localhost|' # Yoki localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # Yoki IP manzil
        r'(?::\d+)?' # Ixtiyoriy port (:8000)
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )
    
    if re.match(https_pattern, url):
        return True
    return False
