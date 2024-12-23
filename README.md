Online Kargo Takip Sistemi

Bu proje, kullanıcı dostu bir kargo takip paneli oluşturmayı amaçlamaktadır. Karmaşık veri yapıları ve algoritmalar kullanılarak, müşteri ve kargo bilgilerini verimli bir şekilde yönetmek için geliştirilmiştir.

Özellikler

Müşteri Yönetimi: Müşteri bilgileri ve gönderim geçmişi linked list yapısı ile yönetilir.

Kargo Önceliklendirme: Priority queue algoritması ile teslimat sürelerine göre önceliklendirme yapılır.

Kargo Rotalama: Tree veri yapısı kullanılarak optimal rotalar oluşturulur.

Gönderim Geçmişi Sorgulama: Stack veri yapısı ile son gönderim geçmişine hızlı erişim sağlanır.

Durum Sorgulama: Binary search ve quick sort algoritmaları ile kargo durumları sorgulanır ve sıralanır.

Gerekli Bileşenler

Backend: Python 3.10 veya üzeri.

Frontend: Qt Designer kullanılarak geliştirilmiş bir kullanıcı arayüzü.

Kurulum Talimatları

1. Python Kurulumu

Projeyi çalıştırmak için Python 3.10 veya üzeri bir sürümün sisteminizde kurulu olduğundan emin olun.

Python'u indirmek için: Python Resmi Web Sitesi

2. Gerekli Kütüphanelerin Kurulumu

Gerekli Python kütüphanelerini kurmak için aşağıdaki komutu çalıştırın:

pip install -r requirements.txt

3. Kodun Çalıştırılması

Aşağıdaki adımları takip ederek projeyi çalıştırabilirsiniz:

main.py dosyasını çalıştırın:

python main.py

Uygulama arayüzü açıldığında, menüden gerekli işlemleri seçebilirsiniz.

Kullanım Kılavuzu

Müşteri Yönetimi

Yeni bir müşteri eklemek için "Müşteri Ekle" bölümüne gidin.

Mevcut bir müşterinin gönderim geçmişini görüntülemek için müşteri ID'sini girerek "Geçmiş Sorgula" seçeneğini kullanın.

Kargo Önceliklendirme

Gönderi bilgilerini girerek yeni bir kargo ekleyin.

"Kargo İşle" seçeneği ile en öncelikli kargoyu işleme alın.

Kargo Rotalama

Teslimat rotalarını görüntülemek için "Rota Göster" seçeneğini kullanın.

Gönderim Geçmişi

"Geçmiş Listele" seçeneği ile son gönderimlerinizi görüntüleyin.

Durum Sorgulama

Teslim edilen veya edilmeyen kargoları sorgulamak için "Durum Sorgula" seçeneğini kullanın.

Örnek Kod Parçacıkları

Tree Veri Yapısı Örneği

class TreeNode:
    def __init__(self, city_name, city_id):
        self.city_name = city_name
        self.city_id = city_id
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print(" " * level + f"{self.city_name} ({self.city_id})")
        for child in self.children:
            child.display(level + 2)

Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen aşağıdaki adımları takip edin:

Bu repoyu forklayın.

Yeni bir dal (branch) oluşturun: git checkout -b feature/isim

Değişikliklerinizi yapın ve commit edin: git commit -m 'Yeni özellik ekle'

Dallarınızı pushlayın: git push origin feature/isim

Pull Request oluşturun.

Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasını inceleyin.

