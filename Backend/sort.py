from bisect import bisect_left
from informations import all_shipments

def binary_search_shipments(shipments, shipment_id):
    """
    Teslim edilmiş kargoları ID'ye göre binary search algoritması ile bulur.
    
    Args:
        shipments (list): Kargoların ID'ye göre sıralı listesi.
        shipment_id (int): Aranan kargo ID'si.

    Returns:
        Shipment: Bulunan kargo objesi veya None.
    """
    left, right = 0, len(shipments) - 1
    while left <= right:
        mid = (left + right) // 2
        if shipments[mid].shipment_id == shipment_id:
            return shipments[mid]
        elif shipments[mid].shipment_id < shipment_id:
            left = mid + 1
        else:
            right = mid - 1
    return None

def merge_sort_shipments(shipments):
    """
    Teslim edilmemiş kargoları teslimat süresine göre merge sort ile sıralar.

    Args:
        shipments (list): Teslim edilmemiş kargoların listesi.

    Returns:
        list: Teslimat süresine göre sıralanmış kargo listesi.
    """
    if len(shipments) > 1:
        mid = len(shipments) // 2
        left_half = shipments[:mid]
        right_half = shipments[mid:]

        merge_sort_shipments(left_half)
        merge_sort_shipments(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].delivery_duration < right_half[j].delivery_duration:
                shipments[k] = left_half[i]
                i += 1
            else:
                shipments[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            shipments[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            shipments[k] = right_half[j]
            j += 1
            k += 1

    return shipments

def quick_sort_shipments(shipments):
    """
    Teslim edilmemiş kargoları teslimat süresine göre quick sort ile sıralar.

    Args:
        shipments (list): Teslim edilmemiş kargoların listesi.

    Returns:
        list: Teslimat süresine göre sıralanmış kargo listesi.
    """
    if len(shipments) <= 1:
        return shipments
    pivot = shipments[len(shipments) // 2]
    left = [x for x in shipments if x.delivery_duration < pivot.delivery_duration]
    middle = [x for x in shipments if x.delivery_duration == pivot.delivery_duration]
    right = [x for x in shipments if x.delivery_duration > pivot.delivery_duration]
    return quick_sort_shipments(left) + middle + quick_sort_shipments(right)

def display_sorted_shipments(shipments, title="Sorted Shipments"):
    """
    Sıralı kargo listesini ekrana yazdırır.

    Args:
        shipments (list): Sıralı kargoların listesi.
        title (str): Yazdırılacak başlık.
    """
    print(f"\n{title}:")
    for shipment in shipments:
        print(shipment)

# Zaman karmaşıklığı analizleri:
# Merge Sort: O(n log n) - Her bölme işlemi O(log n), birleştirme O(n) olduğu için toplamda O(n log n).
# Quick Sort: Ortalama O(n log n), en kötü durumda O(n^2) - Pivot seçimine bağlıdır.

def main():
    # Teslim edilmemiş kargoları al ve teslimat süresine göre merge sort ile sırala
    undelivered_shipments = [s for s in all_shipments if s.delivery_status != "Delivered"]
    sorted_undelivered = merge_sort_shipments(undelivered_shipments)
    display_sorted_shipments(sorted_undelivered, "Merge Sort - Undelivered Shipments")

    # Teslim edilmiş kargoları ID'ye göre sırala
    delivered_shipments = sorted(
        [s for s in all_shipments if s.delivery_status == "Delivered"],
        key=lambda x: x.shipment_id
    )

    # Kullanıcıdan arama yapmak için kargo ID'sini al
    try:
        search_id = int(input("\nPlease enter the Shipment ID to search: "))
    except ValueError:
        print("Invalid input! Please enter a numeric ID.")
        return

    # Binary search ile arama yap
    found_shipment = binary_search_shipments(delivered_shipments, search_id)
    if found_shipment:
        print(f"\nBinary Search - Found Shipment: ID={found_shipment.shipment_id}, Status={found_shipment.delivery_status}, Duration={found_shipment.delivery_duration} days")
    else:
        print(f"\nBinary Search - Shipment with ID={search_id} not found.")

# Ana fonksiyonu çalıştır
if __name__ == "__main__":
    main()
