all_shipments = []  # Bu liste tüm gönderileri tutar
customers_list = []  # Global müşteri listesi

from Backend.treeCities import find_delivery_time_to_city, root
import random

# Gönderi (Shipment) sınıfı
class Shipment:
    def __init__(self, shipment_id, shipment_date, delivery_status, target_city):
        self.shipment_id = shipment_id  # Gönderi ID
        self.shipment_date = shipment_date  # Gönderi Tarihi
        self.delivery_status = delivery_status  # Teslim Durumu
        self.target_city = target_city  # Hedef şehir
        self.delivery_duration = find_delivery_time_to_city(root, target_city)  # Teslim süresi (gün cinsinden)

    def __str__(self):
        return f"ID: {self.shipment_id}, Date: {self.shipment_date}, Status: {self.delivery_status}, Target City: {self.target_city}, Duration: {self.delivery_duration} days"

# Linked List (Bağlı Liste) sınıfı
class LinkedList:
    class Node:
        def __init__(self, shipment):
            self.shipment = shipment  # Kargo gönderisi
            self.next = None  # Sonraki düğüm

    def __init__(self):
        self.head = None  # Bağlantılı listenin başlangıcı

    def add(self, shipment):
        new_node = self.Node(shipment)
        if self.head is None:
            self.head = new_node  # Liste boşsa, ilk öğeyi ekle
        else:
            current = self.head
            while current.next:  # Liste sonuna kadar git
                current = current.next
            current.next = new_node  # Yeni öğeyi listenin sonuna ekle

    def display(self):
        current = self.head
        while current:
            print(current.shipment)
            current = current.next

# Yığın (Stack) sınıfı
class Stack:
    def __init__(self):
        self.stack = []  # Yığın, bir liste olarak tutuluyor

    def push(self, shipment):
        if len(self.stack) >= 5:  # Eğer yığındaki öğe sayısı 5'ten fazla ise, ilk öğeyi çıkar
            self.stack.pop(0)  # Yığının en altındaki öğeyi çıkar (FIFO prensibi ile)
        self.stack.append(shipment)  # Yeni gönderi yığının üstüne eklenir

    def pop(self):
        if len(self.stack) == 0:  # Yığın boşsa hata mesajı ver
            print("Error: No shipment history found!")
        else:
            return self.stack.pop()  # Yığının en üstündeki öğeyi çıkar

    def get_last_shipments(self):
        if len(self.stack) == 0:  # Eğer yığın boşsa
            print("Error: No shipment history found!")
            return []  # Boş bir liste döndür
        else:
            print("Last 5 shipments:")
            return self.stack  # Yığındaki tüm öğeleri döndür

# Müşteri sınıfı
class Customer:
    def __str__(self):
         return f"ID: {self.customerID}, Name: {self.name}, Surname: {self.surname}"

    def __init__(self, customerID, name, surname):
        self.customerID = customerID
        self.name = name
        self.surname = surname
        self.shipment_history_list = LinkedList()  # Linked List başlangıcı
        self.shipment_history_stack = Stack()  # Yığın (stack) kargo geçmişi

    @classmethod
    def addCustomer(cls, name, surname):
        # 4 haneli rastgele bir customerID oluştur
        customerID = random.randint(1000, 9999)
        new_customer = cls(customerID, name, surname)
        customers_list.append(new_customer)  # Global müşteri listesine ekleme
        print(f"New customer added: ID={new_customer.customerID}, Name={new_customer.name}, Surname={new_customer.surname}")

    @classmethod
    def listCustomers(cls):
        if not customers_list:
            print("No customers found.")
        else:
            print("Customer List:")
            for customer in customers_list:
                print(f"ID={customer.customerID}, Name={customer.name}, Surname={customer.surname}")

    def addShipment(self, shipment_date, delivery_status, target_city):
        
        # 4 haneli rastgele bir shipment_id oluştur
        shipment_id = random.randint(1000, 9999)
        shipment = Shipment(shipment_id, shipment_date, delivery_status, target_city)

        # Global gönderi listesine ekleme
        all_shipments.append(shipment)

        # Linked List'e gönderi ekleme
        self.shipment_history_list.add(shipment)

        # Stack'e gönderiyi ekleme (Son 5 gönderi)
        self.shipment_history_stack.push(shipment)

    def listAllShipments(self):
        print(f"All shipments for {self.name} {self.surname}:")
        self.shipment_history_list.display()  # Tüm gönderileri Linked List üzerinden listele
        print(" ") 

    def listLastShipments(self):
        print(f"Last shipments for {self.name} {self.surname}:")
        self.shipment_history_stack.get_last_shipments()  # Son 5 gönderiyi Stack üzerinden listele
        print(" ") 

# Yeni müşteri ekleme
Customer.addCustomer("Ahmet", "Yılmaz")
Customer.addCustomer("Ayşe", "Kara")
Customer.addCustomer("Mirza", "Sincap")
Customer.addCustomer("Mirza", "Şakirson")
Customer.addCustomer("Selim", "Genç")
Customer.addCustomer("Ebru", "Aydın")
Customer.addCustomer("Fatma", "Demir")
Customer.addCustomer("Hakan", "Çelik")
Customer.addCustomer("Mehmet", "Arslan")
Customer.addCustomer("Zeynep", "Şahin")
Customer.addCustomer("Ali", "Kaya")
Customer.addCustomer("Ayhan", "Koç")
Customer.addCustomer("Sevgi", "Yıldız")
Customer.addCustomer("İbrahim", "Öztürk")
Customer.addCustomer("Elif", "Yılmaz")
Customer.addCustomer("Berk", "Kurt")
Customer.addCustomer("Deniz", "Güneş")
Customer.addCustomer("Canan", "Polat")
Customer.addCustomer("Emre", "Aslan")
Customer.addCustomer("Sibel", "Keskin")
Customer.addCustomer("Kemal", "Ekinci")
Customer.addCustomer("Gizem", "Şimşek")
Customer.addCustomer("Onur", "Bulut")
Customer.addCustomer("Betül", "Ceylan")
Customer.addCustomer("Serkan", "Gök")
Customer.addCustomer("Merve", "Karaca")
Customer.addCustomer("Mustafa", "Bozkurt")
Customer.addCustomer("Tuğçe", "Turan")
Customer.addCustomer("Özlem", "Kılıç")
Customer.addCustomer("Yusuf", "Çetin")
Customer.addCustomer("Burak", "Acar")
Customer.addCustomer("Esra", "Uçar")
Customer.addCustomer("Ece", "Erdoğan")
Customer.addCustomer("Pelin", "Yalçın")
Customer.addCustomer("Cem", "Erol")

customer1 = customers_list[0]
customer1.addShipment("2024-12-10", "Not Delivered", "Eskişehir")
customer1.addShipment("2024-12-12", "Not Delivered", "Afyonkarahisar")
customer1.addShipment("2024-12-14", "Not Delivered", "Bolu")
customer1.addShipment("2024-12-15", "Delivered", "Karabük")
customer1.addShipment("2024-12-16", "Not Delivered", "Tekirdağ")
customer1.addShipment("2024-12-17", "Not Delivered", "Bilecik")
customer1.addShipment("2024-12-18", "Delivered", "Kırklareli")

customer2 = customers_list[1]
customer2.addShipment("2024-12-19", "Delivered", "Kırklareli")
customer2.addShipment("2024-12-20", "Not Delivered", "Tekirdağ")
customer2.addShipment("2024-12-21", "Delivered", "Kocaeli")
customer2.addShipment("2024-12-22", "Not Delivered", "Edirne")
customer2.addShipment("2024-12-23", "Not Delivered", "Yalova")
customer2.addShipment("2024-12-24", "Delivered", "Bursa")
customer2.addShipment("2024-12-25", "Not Delivered", "Sakarya")
customer2.addShipment("2024-12-26", "Delivered", "Bilecik")
customer2.addShipment("2024-12-27", "Not Delivered", "Bolu")
customer2.addShipment("2024-12-28", "Delivered", "Düzce")
customer2.addShipment("2024-12-29", "Not Delivered", "Balıkesir")
customer2.addShipment("2024-12-30", "Not Delivered", "Kütahya")
customer2.addShipment("2024-12-31", "Delivered", "Çanakkale")
customer2.addShipment("2025-01-01", "Not Delivered", "Manisa")
customer2.addShipment("2025-01-02", "Delivered", "İzmir")
customer2.addShipment("2025-01-03", "Not Delivered", "Uşak")
customer2.addShipment("2025-01-04", "Delivered", "Afyonkarahisar")
customer2.addShipment("2025-01-05", "Not Delivered", "Eskişehir")
customer2.addShipment("2025-01-06", "Not Delivered", "Ankara")
customer2.addShipment("2025-01-07", "Delivered", "Karabük")
customer2.addShipment("2025-01-08", "Not Delivered", "Zonguldak")

customer3 = customers_list[2]
customer3.addShipment("2024-12-16", "Delivered", "Manisa")
customer3.addShipment("2024-12-17", "Delivered", "Zonguldak")
customer3.addShipment("2024-12-18", "Delivered", "Kütahya")

customer1.listAllShipments()
customer1.listLastShipments()

class ShipmentSorter:
    @staticmethod
    def quicksort_shipments(shipments):
        """
        Quicksort algoritması ile kargo listesini kargo ID'sine göre küçükten büyüğe sıralar.

        Args:
            shipments (list): Sıralanacak kargo listesi.

        Returns:
            list: Sıralanmış kargo listesi.
        """
        if len(shipments) <= 1:
            return shipments
        pivot = shipments[0]
        lesser = [shipment for shipment in shipments[1:] if shipment.shipment_id <= pivot.shipment_id]
        greater = [shipment for shipment in shipments[1:] if shipment.shipment_id > pivot.shipment_id]
        return ShipmentSorter.quicksort_shipments(lesser) + [pivot] + ShipmentSorter.quicksort_shipments(greater)

    @staticmethod
    def sort_shipments_by_id():
        """
        all_shipments listesini kargo ID'sine göre küçükten büyüğe sıralar.
        """
        global all_shipments
        all_shipments = ShipmentSorter.quicksort_shipments(all_shipments)
        

    @staticmethod
    def binary_search_by_id(target_id):
        """
        Binary search ile all_shipments listesinden kargo ID'sine göre arama yapar.

        Args:
            target_id (int): Aranacak kargo ID.

        Returns:
            Shipment: Bulunan kargo objesi veya None.
        """
        low = 0
        high = len(all_shipments) - 1

        while low <= high:
            mid = (low + high) // 2
            current_shipment = all_shipments[mid]

            if current_shipment.shipment_id == target_id:
                return current_shipment
            elif current_shipment.shipment_id < target_id:
                low = mid + 1
            else:
                high = mid - 1

        return None  # Kargo bulunamadı