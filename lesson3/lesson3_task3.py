from address import Address
from mailing import Mailing

to_address=Address("105187","Москва","Лечебная","3","23")
from_address=Address("454108","Челябинск","Пограничная","25","200")

mailing=Mailing(to_address,from_address,"1500","IDK32547852")

print (
    f"Отправление {mailing.track} из {mailing.from_address.index},"
    f"{mailing.from_address.city},{mailing.from_address.street},"
    f"{mailing.from_address.home}-"
    f"{mailing.from_address.room} в {mailing.to_address.index},"
    f"{mailing.to_address.city},{mailing.to_address.street},"
    f"{mailing.to_address.home}-"
    f"{mailing.to_address.room}."
    f"Стоимость {mailing.cost} рублей."
)