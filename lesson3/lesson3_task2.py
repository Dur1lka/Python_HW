from smartphone import Smartphone

catalog= [
    Smartphone("Iphone","VIIProMax","+79356873368"),
    Smartphone("Samsung","SUltra","+79258475824"),
    Smartphone("Honor","MagicV","+79212586535"),
    Smartphone("Xiaomi","MixFlip","+79356483265"),
    Smartphone("Huawei","MateXT","+79254873621")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")