""" Variables """
FIRST_NAME = 'نام'
LAST_NAME = 'نام خانوادگی'
AGE = 'سن'
EMAIL = 'EMAIL'
PHONE = 'شماره تلفن'
PERSONAL_ID = 'شماره شناسنامه'
USERNAME = 'EMAIL'
PASSWORD = 'PASSWORD'
PHOTO = 'عکس'
ADDRESS = 'آدرس'
BIRTHDAY = 'تاریخ تولد'
ENTRY_DATE = 'تاریخ ورود'
STUDY_FIELD = 'رشته تحصیلی'
USERNAME_HELP_TEXT = 'حداکثر ۱۵۰ حرف و میتواند شامل حروف و اعداد و @/./+/-/_ باشد'
PHONE_HELP_TEXT = 'شماره تلفن خود را بدون صفر وارد کنید. مانند : ۹۱۲۱۲۳۴۵۶۷'
PHOTO_HELP_TEXT = 'انتخاب عکس اختیاری است'
REGISTER_DATE = 'تاریخ ثبت نام'
REGISTER_CONFIRM = 'تایید ثبت نام'
MAX_UNITS = 'حداکثر تعداد واحد'
USER_TYPE = 'USER_TYPE'

""" Errors """
INVALID_USERNAME = 'نام کاربری در سیستم موجود است'
INVALID_PHONE = 'شماره تماس در سیستم موجود است'
INVALID_EMAIL = 'ایمیل در سیستم موجود است'
INVALID_FORM = 'لطفا مقادیر فیلد های فرم را به درستی پر کنید'
INVALID_PERSON_ID = 'شماره شناسنامه در سیستم موجود است'
INVALID_USERNAME_PASSWORD = 'نام کاربری یا رمز عبور اشتباه است'
INVALID_LEVEL = 'شما اجازه ی دسترسی به این سطح کاربری را ندارید'
INVALID_RENT_COUNT = 'شما نمیتوانید بیشتر از 5 کتاب امانت بگیرید'
RENT_REMAIN = 'تعداد انتخاب های باقیمانده ی شما: '
""" Register Confirmation """
REGISTER_SUCCESS = 'ثبت نام شما با موفقیت انجام شد'

""" DAYS NAME """
SATURDAY = 'شنبه', 'saturday'
SUNDAY = 'یک شنبه', 'sunday'
MONDAY = 'دو شنبه', 'monday'
THURSDAY = 'سه شنبه', 'thursday'
WEDNESDAY = 'چهارشنبه', 'wednesday'
TUESDAY = 'پنج شنبه', 'tuesday'

""" Choose user's type """
USER_TYPE_CHOICES = [
    ('manager', 'مدیر'),
    ('customer', 'مشتری'),
    ('employee', 'کارمند'),
]

USER_TYPE_REVERSE = {
    'رییس': 'boss',
    'کارمند': 'staff',
    'استاد': 'teacher',
    'دانشجو': 'student',
}
