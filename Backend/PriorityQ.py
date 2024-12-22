from informations import all_shipments

global queue
queue = []

class PriorityQueue:
    def __init__(self):
        global queue
        self.queue = queue

    def add_shipment(self, shipment):
        if shipment.delivery_status == "Delivered":
            shipment.delivery_duration = 0  # Teslim edilenlerin süresi 0 yapılır
        self.queue.append(shipment)
        self.queue.sort(key=lambda x: (x.delivery_duration == 0, x.delivery_duration))

    def display(self):
        print("\nQueue:")
        print("Priority queue (sorted by delivery duration):")
        for shipment in self.queue:
            if shipment.delivery_status == "Delivered":
                print(f"ID: {shipment.shipment_id}, Date: {shipment.shipment_date}, Status: {shipment.delivery_status}")
            else:
                print(f"ID: {shipment.shipment_id}, Date: {shipment.shipment_date}, Status: {shipment.delivery_status}, Duration: {shipment.delivery_duration} days")

# PriorityQueue örneği oluşturuluyor
priority_queue = PriorityQueue()

# informations.py'den gelen tüm gönderiler kuyruğa ekleniyor
for shipment in all_shipments:
    priority_queue.add_shipment(shipment)

# Kuyruk görüntüleniyor
priority_queue.display()

print("Zaman Karmaşıklığı Analizi:")
print("Kargo ekleme işlemi: O(n logn)")
print("Öncelikli kargo işleme: O(1)")