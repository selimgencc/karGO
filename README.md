# Online Kargo Takip Sistemi

Bu proje, kullanıcı dostu bir kargo takip paneli oluşturmayı amaçlamaktadır. Karmaşık veri yapıları ve algoritmalar kullanılarak, müşteri ve kargo bilgilerini verimli bir şekilde yönetmek için geliştirilmiştir.

## Özellikler

- **Müşteri Yönetimi**: Kargo bilgileri ve gönderim geçmişi linked list yapısı ile yönetilir.
- **Kargo Önceliklendirme**: Priority queue algoritması ile teslimat sürelerine göre önceliklendirme yapılır.
- **Kargo Rotalama**: Tree veri yapısı kullanılarak optimal rotalar oluşturulur.
- **Gönderim Geçmişi Sorgulama**: Stack veri yapısı ile son gönderim geçmişine hızlı erişim sağlanır.
- **Durum Sorgulama**: Binary search ve quick sort algoritmaları ile kargo durumları sorgulanır ve sıralanır.

## Gerekli Bileşenler

1. **Backend**: Python 3.10 veya üzeri.
2. **Frontend**: Qt Designer kullanılarak geliştirilmiş bir kullanıcı arayüzü.

## Kurulum Talimatları

### 1. Python Kurulumu

Projeyi çalıştırmak için Python 3.10 veya üzeri bir sürümün sisteminizde kurulu olduğundan emin olun.

- Python'u indirmek için: [Python Resmi Web Sitesi](https://www.python.org)

### 2. Gerekli Kütüphanelerin Kurulumu

Gerekli Python kütüphanelerini kurmak için aşağıdaki komutu çalıştırın:

```bash
pip install -r requirements.txt
```

### 3. Kodun Çalıştırılması

Aşağıdaki adımları takip ederek projeyi çalıştırabilirsiniz:

1. `main.py` dosyasını çalıştırın:
   ```bash
   python main.py
   ```
2. Uygulama arayüzü açıldığında, menüden gerekli işlemleri seçebilirsiniz.

## Kullanım Kılavuzu

### Müşteri Yönetimi

- Yeni bir müşteri eklemek için "Müşteri Ekle" bölümüne gidin.
- Mevcut bir müşterinin gönderim geçmişini görüntülemek için müşteri ID'sini girerek "Geçmiş Sorgula" seçeneğini kullanın.

### Kargo Önceliklendirme

- Gönderi bilgilerini girerek yeni bir kargo ekleyin.
- "Kargo İşle" seçeneği ile en öncelikli kargoyu işleme alın.

### Kargo Rotalama

- Teslimat rotalarını görüntülemek için "Rota Göster" seçeneğini kullanın.

### Gönderim Geçmişi

- "Geçmiş Listele" seçeneği ile son gönderimlerinizi görüntüleyin.

### Durum Sorgulama

- Teslim edilen veya edilmeyen kargoları sorgulamak için "Durum Sorgula" seçeneğini kullanın.


## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen aşağıdaki adımları takip edin:

1. Bu repoyu forklayın.
2. Yeni bir dal (branch) oluşturun: `git checkout -b feature/isim`
3. Değişikliklerinizi yapın ve commit edin: `git commit -m 'Yeni özellik ekle'`
4. Dallarınızı pushlayın: `git push origin feature/isim`
5. Pull Request oluşturun.



Bu projede https://github.com/anjalp/Minimalistic-Flat-Modern-GUI-Template UI template'i kullanılmıștır



