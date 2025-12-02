import math
import requests
import datetime

url = r'https://wttr.in/tabriz?format=j1'
resp = requests.get(url)
data = resp.json()

# humidity
# observation_time
# uvIndex
# windspeedKmph
# weatherDesc - value
# 1.225 is world density standard
# nanometer
print(data['current_condition'][0])

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
