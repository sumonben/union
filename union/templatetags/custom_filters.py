from django import template
from datetime import date

register = template.Library()

BENGALI_MONTHS = {
    1: 'জানুয়ারী', 2: 'ফেব্রুয়ারী', 3: 'মার্চ', 4: 'এপ্রিল', 
    5: 'মে', 6: 'জুন', 7: 'জুলাই', 8: 'আগস্ট', 9: 'সেপ্টেম্বর', 
    10: 'অক্টোবর', 11: 'নভেম্বর', 12: 'ডিসেম্বর'
}

@register.filter
def eng_to_bengali_digits(number):
    """Converts English digits in a string/number to Bengali digits."""
    eng_digits = "0123456789"
    ben_digits = "০১২৩৪৫৬৭৮৯"
    translated = str(number).translate(str.maketrans(eng_digits, ben_digits))
    return translated

@register.filter
def custom_date_format_bn(value):
    if not isinstance(value, date):
        return value

    day = eng_to_bengali_digits(value.day)
    month = BENGALI_MONTHS[value.month]
    year = eng_to_bengali_digits(value.year)

    return f"{day} {month}, {year}"
