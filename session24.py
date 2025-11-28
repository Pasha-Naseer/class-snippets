import math
import requests
import datetime

url = r'https://wttr.in/tabriz?format=j1'
resp = requests.get(url)
data = resp.json()

# humidity
# observation_time - Elin
# uvIndex
# windspeedKmph
# weatherDesc - value
# 1.225 world density standard
# nanometer
print(data['current_condition'][0])

# print(data['current_condition'][0]['temp_C'])

# uvindex = int(data['current_condition'][0]['uvIndex'])
# if uvindex in range(0, 3):
#     print('این اشعه یووی برای بیشتر افراد ریسک خاصی ندارد، همچنین احتمال آفتاب سوختگی بسیار ضعیف می باشد مگر اینکه پوست خیلی حساسی داشته باشید.\nمراقبت های لازم:\nعینک آفتابی و کرم ضد آفتاب اختیاری می باشد.')
# uvindex ranges
# import math
# print(math.cos(math.radians(325)))

# observation_time
observation_time = data['current_condition'][0]['observation_time']


print(f"زمان ثبت اطلاعات هواشناسی\n{observation_time}")
print('لطفا با توجه به زمان ثبت اطلاعات هواشناسی و زمان کنونی از برنامه استفاده کنید!')
print('زمان کنونی')
current_time = datetime.datetime.now().time()
formatted_time = current_time.strftime("%I:%M %p")
print(formatted_time)

# humidity
print('-' * 50)
humidity = int(data['current_condition'][0]['humidity'])
print(f"درصد رطوبت هوا\n{humidity}%")
if humidity < 30:
    print('-' * 10)
    print('خطرات\n. خشکی پوست\n. خشکی لب\n. خشکی چشم\n. گلودرد\n. سرفه خشک\n. تحریک مجاری تنفسی و بدتر شدن آسم و آلرژی و...')
    print('-' * 50)
    print('توصیه ها\n. از دستگاه بخور استفاده کنید.\n. آب بیشتری بنوشید.\n. از مرطوب کننده های قوی برای پوست و لب ها استفاده کنید.\n. از قطره اشک مصنوعی مرطوب کنید.')
    print('-' * 50)
elif 50 > humidity >= 30:
    print('-' * 10)
    print('خطرات\nدر این محدوده مضرات و خطرات قابل توجهی وجود ندارد.')
    print('-' * 50)
    print('توصیه ها\nنیازی به اقدامات خاصی وجود ندارد.')
    print('-' * 50)
elif 70 > humidity >= 50:
    print('-' * 10)
    print('خطرات\n. احساس سنگینی و گرما.\n. تعریق زیاد و خشک شدن پوست.\n. افزایش رشد قارچ های پوستی و عفونت ها.\n. بدتر شدن علائم آسم و آلرژی.')
    print('-' * 50)
    print("توصیه ها\n. لباس های نخی و گشاد بپوشید.\n. دوش آب خنک بگیرید.\n. تهویه هوا را بهتر کنید.\n. اگر آلرژی یا آسم دارید مراقب رشد کپک باشید.")
    print('-' * 50)
elif humidity >= 70:
    print('-' * 10)
    print('خطرات\n. شدید ترین حالت مضرات رطوبت بالا.\n. خطر بالای گرمازدگی و مشکلات تنفسی.\n. شیوع گسترده آلرژی و آسم.\n. رشد شدید باکتری و ویروس.')
    print('-' * 50)
    print("توصیه ها\n. حتما تهویه را به حداکثر برسانید.\n. در صورت امکان از خانه خارج نشوید.\n. به محلی با رطوبت پایین بروید.\n. مراقب علائم گرمازدگی و مشکلات تنفسی باشید.\n. سطوح را به طور منظم با مواد ضدقارچ تمیز کنید تا از رشد کپک و قارچ جلوگیری شود.")
    print('-' * 50)
print()

# wind speed
print('-' * 50)
wind_speed = int(data['current_condition'][0]['windspeedKmph'])
# wind_speed = 400
print('سرعت وزش باد')
print(f"{wind_speed} کیلومتر بر ساعت")
print('-' * 10)
while True:
    try:
        weight = int(input("وزن خودتان را وارد کنید.\n(حالا وارد کن بهت میگم چرا)"))
    except ValueError:
        print("ورودی اشتباه!")
    else:
        if weight in range(1, 635):
            break
        else:
            print('لطفا وزن درستی را وارد کنید!')

wind_mass = (weight * 1000) / 0.98
wind_volume = (wind_mass / 1000000) * 1.225
wind_degree = int(data['current_condition'][0]['winddirDegree'])
# wind_degree = 0
cos_wind_degree = math.cos(math.radians(wind_degree))
kinetic_energy = (0.5 * wind_volume) * (wind_speed * (5/18)) ** 2
if kinetic_energy * cos_wind_degree > weight * 10:
    print("با توجه به بررسی های انجام شده توسط گروهی از دانشمندان در کلاس 69 اعم از پروفسور ارشان افتخاری(نجوم دان، اخترفیزیک دان، فیزیک دان) و پروفسور مهدی نصیرسلطانی(مهندس نرم افزار، اخترفیزیکدان، و دریاسالار)\nامروز در صورت خروج از خانه باد شما را خواهد برد!")
elif kinetic_energy * cos_wind_degree == weight * 10:
    print("با توجه به بررسی های انجام شده توسط گروهی از دانشمندان در کلاس 69 اعم از پروفسور ارشان افتخاری(نجوم دان، اخترفیزیک دان، فیزیک دان) و پروفسور مهدی نصیرسلطانی(مهندس نرم افزار، اخترفیزیکدان، و دریاسالار)\nامروز در صورت خروج از خانه شاید باد شما را ببرد!")
else:
    print("با توجه به بررسی های انجام شده توسط گروهی از دانشمندان در کلاس 69 اعم از پروفسور ارشان افتخاری(نجوم دان، اخترفیزیک دان، فیزیک دان) و پروفسور مهدی نصیرسلطانی(مهندس نرم افزار، اخترفیزیکدان، و دریاسالار)\nامروز در صورت خروج از خانه باد شما را نخواهد برد!")
