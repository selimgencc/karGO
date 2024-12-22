# informations.py
from Backend.treeCities import find_delivery_time_to_city, root

all_shipments = []  # Bu liste tüm gönderileri tutar
customers_list = []  # Global müşteri listesi

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
    def addCustomer(cls, customerID, name, surname):
        new_customer = cls(customerID, name, surname)
        customers_list.append(new_customer)  # Global müşteri listesine ekleme
        print(
            f"New customer added: ID={new_customer.customerID}, Name={new_customer.name}, Surname={new_customer.surname}")

    @classmethod
    def listCustomers(cls):
        if not customers_list:
            print("No customers found.")
        else:
            print("Customer List:")
            for customer in customers_list:
                print(f"ID={customer.customerID}, Name={customer.name}, Surname={customer.surname}")

    def addShipment(self, shipment_id, shipment_date, delivery_status, target_city):
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
        print(" ") # Bir satır boşluk bırak

    def listLastShipments(self):
        print(f"Last shipments for {self.name} {self.surname}:")
        self.shipment_history_stack.get_last_shipments()  # Son 5 gönderiyi Stack üzerinden listele
        print(" ") # Bir satır boşluk bırak

# Örnek kullanımlar
Customer.addCustomer(1, "Ahmet", "Yılmaz")
Customer.addCustomer(2, "Ayşe", "Kara")

customer1 = customers_list[0]
customer1.addShipment(101, "2024-12-10", "Not Delivered", "Balıkesir")
customer1.addShipment(102, "2024-12-12", "Delivered", "Tekirdağ")

# Yeni müşteri ekleme
Customer.addCustomer(1, "Ahmet", "Yılmaz")
Customer.addCustomer(2, "Ayşe", "Kara")
Customer.addCustomer(3, "mirza", "sincap")
Customer.addCustomer(4, "mirza", "şakirson")
Customer.addCustomer(5,"gözlüklü şirin","GENÇ")

# Gönderi ekleme
customer1 = customers_list[0]
customer1.addShipment(101, "2024-12-10", "Not Delivered", "Eskişehir")
customer1.addShipment(102, "2024-12-12", "Not Delivered", "Afyonkarahisar")
customer1.addShipment(103, "2024-12-14", "Not Delivered", "Bolu")
customer1.addShipment(104, "2024-12-15", "Delivered", "Karabük")
customer1.addShipment(105, "2024-12-16", "Not Delivered", "Tekirdağ")
customer1.addShipment(106, "2024-12-17", "Not Delivered", "Bilecik")
customer1.addShipment(107, "2024-12-18", "Delivered", "Kırklareli")

customer2 = customers_list[1]
customer2.addShipment(201, "2024-12-11", "Delivered", "İzmir")
customer2.addShipment(202, "2024-12-13", "Delivered", "Uşak")
customer2.addShipment(203, "2024-12-15", "Not Delivered", "Edirne")

customer3 = customers_list[2]
customer3.addShipment(204, "2024-12-16", "Delivered", "Manisa")
customer3.addShipment(205, "2024-12-17", "Delivered", "Zonguldak")
customer3.addShipment(206, "2024-12-18", "Delivered", "Kütahya")

customer1.listAllShipments()
customer1.listLastShipments()
