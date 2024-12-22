class CityNode:
    def __init__(self, city_name, city_id):
        self.city_name = city_name  # Şehir Adı
        self.city_id = city_id  # Şehir ID
        self.children = []  # Alt şehirler (çocuk düğümler)

    def add_child(self, child_node):
        self.children.append(child_node)  # Alt şehir ekleme




def print_tree(node, level=0):
    print(' ' * level * 4 + f"{node.city_name} (ID: {node.city_id})")
    for child in node.children:
        print_tree(child, level + 1)


def find_delivery_time_to_city(node, target_city, current_days=1):
    # Hedef şehri bulmaya çalışıyoruz
    if node.city_name == target_city:
        print(f"{target_city} şehrine teslimat süresi: {current_days} gün")
        return current_days

    # Çocuk şehirlerde arama yapıyoruz
    for child in node.children:
        delivery_time = find_delivery_time_to_city(child, target_city, current_days + 1)
        if delivery_time is not None:
            return delivery_time

    # Eğer şehir bulunmazsa None döner
    return None


# Örnek ağacın oluşturulması
root = CityNode("İstanbul", 1)
city1 = CityNode("Kırklareli", 2)
city2 = CityNode("Tekirdağ", 3)
city3 = CityNode("Kocaeli", 4)
city4 = CityNode("Edirne", 5)
city5 = CityNode("Yalova", 6)
city6 = CityNode("Bursa", 7)
city7 = CityNode("Sakarya", 8)
city8 = CityNode("Bilecik", 9)
city9 = CityNode("Bolu", 10)
city10 = CityNode("Düzce", 11)
city11 = CityNode("Balıkesir", 12)
city12 = CityNode("Kütahya", 13)
city13 = CityNode("Çanakkale", 14)
city14 = CityNode("Manisa", 15)
city15 = CityNode("İzmir", 16)
city16 = CityNode("Uşak", 17)
city17 = CityNode("Afyonkarahisar", 18)
city18 = CityNode("Eskişehir", 19)
city19 = CityNode("Ankara", 20)
city20 = CityNode("Karabük", 21)
city21 = CityNode("Zonguldak", 22)

root.add_child(city2)
root.add_child(city3)
city2.add_child(city4)
city2.add_child(city1)
city3.add_child(city5)
city3.add_child(city6)
city3.add_child(city7)
city6.add_child(city11)
city6.add_child(city12)
city7.add_child(city8)
city7.add_child(city9)
city7.add_child(city10)
city11.add_child(city13)
city11.add_child(city14)
city11.add_child(city15)
city12.add_child(city16)
city12.add_child(city17)
city8.add_child(city18)
city9.add_child(city19)
city9.add_child(city20)
city10.add_child(city21)

# Ağacın görsel çıktısı
print_tree(root)

# Balıkesir şehri için teslimat süresi hesapla
find_delivery_time_to_city(root, "Zonguldak")
