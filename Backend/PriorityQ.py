from informations import all_shipments

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.delivered_shipments = []

    def add_shipment(self, shipment):
        if shipment.delivery_status == "Not Delivered":
            self.queue.append(shipment)
            self.queue.sort(key=lambda x: x.delivery_duration)
        elif shipment.delivery_status == "Delivered":
            self.delivered_shipments.append(shipment)

    def next_shipment(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def display(self):
        print("Next shipment to process:")
        next_shipment = self.next_shipment()
        if next_shipment:
            print(next_shipment)
        else:
            print("No shipments in the queue.")

        print("\nRemaining queue:")
        print("Priority queue (sorted by delivery duration):")
        for shipment in self.queue:
            print(shipment)

        print("\nDelivered shipments:")
        for shipment in self.delivered_shipments:
            print(f"ID: {shipment.shipment_id}, Date: {shipment.shipment_date}, Status: {shipment.delivery_status}")

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