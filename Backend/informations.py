all_shipments = []  # Bu liste tüm gönderileri tutar

# Gönderi (Shipment) sınıfı
class Shipment:
    def __init__(self, shipment_id, shipment_date, delivery_status, delivery_duration):
        self.shipment_id = shipment_id  # Gönderi ID
        self.shipment_date = shipment_date  # Gönderi Tarihi
        self.delivery_status = delivery_status  # Teslim Durumu
        self.delivery_duration = delivery_duration  # Teslim Süresi (gün cinsinden)

    def __str__(self):
        return f"ID: {self.shipment_id}, Date: {self.shipment_date}, Status: {self.delivery_status}, Duration: {self.delivery_duration} days"


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
        else:
            print("Last 5 shipments:")
            for shipment in reversed(self.stack):  # Yığının en üstündeki gönderiden başlayarak listele
                print(shipment)


# Müşteri sınıfı
class Customer:
    customers_list = []  # Tüm müşterileri saklamak için bir sınıf değişkeni (array list)

    def __init__(self, customerID, name, surname):
        self.customerID = customerID
        self.name = name
        self.surname = surname
        self.shipment_history_list = LinkedList()  # Linked List başlangıcı
        self.shipment_history_stack = Stack()  # Yığın (stack) kargo geçmişi

    @classmethod
    def addCustomer(cls, customerID, name, surname):
        new_customer = cls(customerID, name, surname)
        cls.customers_list.append(new_customer)
        print(
            f"New customer added: ID={new_customer.customerID}, Name={new_customer.name}, Surname={new_customer.surname}")

    @classmethod
    def listCustomers(cls):
        if not cls.customers_list:
            print("No customers found.")
        else:
            print("Customer List:")
            for customer in cls.customers_list:
                print(f"ID={customer.customerID}, Name={customer.name}, Surname={customer.surname}")

    def addShipment(self, shipment_id, shipment_date, delivery_status, delivery_duration):
        shipment = Shipment(shipment_id, shipment_date, delivery_status, delivery_duration)


        # Global gönderi listesine ekleme
        all_shipments.append(shipment)

        # Linked List'e gönderi ekleme
        self.shipment_history_list.add(shipment)

        # Stack'e gönderiyi ekleme (Son 5 gönderi)
        self.shipment_history_stack.push(shipment)

    def listAllShipments(self):
        print(f"All shipments for {self.name} {self.surname}:")
        self.shipment_history_list.display()  # Tüm gönderileri Linked List üzerinden listele
        print(" ") # Bir satır boşluk bırak")

    def listLastShipments(self):
        print(f"Last shipments for {self.name} {self.surname}:")
        self.shipment_history_stack.get_last_shipments()  # Son 5 gönderiyi Stack üzerinden listele
        print(" ") # Bir satır boşluk bırak


# Tüm gönderileri listeleyen fonksiyon
def listAllShipments():
    if not all_shipments:
        print("No shipments found.")
    else:
        print("All Shipments:")
        for shipment in all_shipments:
            print(shipment)


# Yeni müşteri ekleme
Customer.addCustomer(1, "Ahmet", "Yılmaz")
Customer.addCustomer(2, "Ayşe", "Kara")

# Gönderi ekleme
customer1 = Customer.customers_list[0]

customer1.addShipment(101, "2024-12-10", "Delivered", 3)
customer1.addShipment(102, "2024-12-12", "Not Delivered", 5)
customer1.addShipment(103, "2024-12-14", "Delivered", 2)
customer1.addShipment(104, "2024-12-15", "Delivered", 4)
customer1.addShipment(105, "2024-12-16", "Not Delivered", 3)
customer1.addShipment(106, "2024-12-17", "Delivered", 1)
Customer.customers_list[0].addShipment(107, "2024-12-18", "Delivered", 2)

customer2 = Customer.customers_list[1]
customer2.addShipment(201, "2024-12-11", "Delivered", 2)
customer2.addShipment(202, "2024-12-13", "Delivered", 3)
customer2.addShipment(203, "2024-12-15", "Not Delivered", 4)

# Müşterilerin tüm kargo gönderimlerini listeleme
customer1.listAllShipments()
customer2.listAllShipments()

# Müşterilerin son 5 kargo gönderimini listeleme
customer1.listLastShipments()
customer2.listLastShipments()

# Tüm gönderileri listeleme
listAllShipments()