from db import SessionLocal
from models import Building, Organization, Activity

db = SessionLocal()

# Очистка данных
db.query(Organization).delete()
db.query(Building).delete()
db.query(Activity).delete()

# Виды деятельности
activity_food = Activity(name="Еда")
activity_meat = Activity(name="Мясная продукция", parent=activity_food)
activity_milk = Activity(name="Молочная продукция", parent=activity_food)

activity_auto = Activity(name="Автомобили")
activity_cars = Activity(name="Легковые", parent=activity_auto)
activity_parts = Activity(name="Запчасти", parent=activity_cars)

db.add_all([activity_food, activity_meat, activity_milk, activity_auto, activity_cars, activity_parts])
db.flush()

# Здания
b1 = Building(address="Москва, Ленина 1", latitude=55.7558, longitude=37.6176)
b2 = Building(address="Новосибирск, Красный проспект 22", latitude=55.0415, longitude=82.9346)
b3 = Building(address="Екатеринбург, Блюхера 32/1", latitude=56.8519, longitude=60.6122)

db.add_all([b1, b2, b3])
db.flush()

# Организации
o1 = Organization(name="Рога и Копыта", phones="2-222-222,3-333-333", building=b1, activities=[activity_meat])
o2 = Organization(name="Молочная сказка", phones="8-900-123-45-67", building=b1, activities=[activity_milk])
o3 = Organization(name="АвтоМир", phones="8-923-666-13-13", building=b2, activities=[activity_cars, activity_parts])
o4 = Organization(name="Мясной рай", phones="333-999", building=b2, activities=[activity_meat])
o5 = Organization(name="Запчасти для всех", phones="700-700", building=b3, activities=[activity_parts])
o6 = Organization(name="Ферма", phones="8-800-555-35-35", building=b3, activities=[activity_food])

db.add_all([o1, o2, o3, o4, o5, o6])
db.commit()

print("Test data inserted successfully.")
