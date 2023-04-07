ALGORİTMA ANALİZİ VE TASARIMI DERSİ 1. KISA SINAV 2. BÖLÜM ÖDEVİ
Hazırlayam: Berkay Aydın 1210505048


Python programlam dili kullanılarak yazılan kodda kelimeler önceden belirlenmiş olup kod çalıştırıldığında hangi kelimenin kaç kez geçtiği ekrana yazdırılmaktadır.
Kodun sorunsuzca çalışabilmesi için Alice in Wonderland metninin dosya.txt adında kod ile aynı klasörde olması gerekmetedir. Bu dosya yolu kod üzerinden değiştirilebilmektedir..


Çift yönlü arama algoritmasının amacı, bir sıralı veya düzensiz veri kümesinde belirli bir öğeyi hızlı bir şekilde bulmaktır. Bu algoritma, veri kümesini iki yönden de tarar ve hızlı bir şekilde hedeflenen öğeyi bulabilmek için iki yönlü hareket eder.

Çalışma şekli şu adımları içerir:

Başlangıçta, veri kümesinin ortasında veya başka bir belirli bir konumda bulunan bir referans öğesi seçilir referans öğesi, hedeflenen öğe ile karşılaştırılır.Eğer referans öğesi hedeflenen öğeye eşitse, arama tamamlanmıştır ve hedeflenen öğe bulunmuştur.Eğer referans öğesi hedeflenen öğeden küçükse, referans öğesinin sağındaki bölgeye bakılır ve arama bu bölgede devam eder.Eğer referans öğesi hedeflenen öğeden büyükse, referans öğesinin solundaki bölgeye bakılır ve arama bu bölgede devam eder.
Arama, hedeflenen öğe bulunana kadar bu adımları tekrarlar veya veri kümesi tamamen taranıncaya kadar devam eder.

Çalışma zamanı analizi için, en iyi, en kötü ve ortalama sınırlar aşağıdaki gibi belirlenebilir:

*En İyi Durum: Hedeflenen öğenin referans öğesi olarak seçildiği durumdur. Bu durumda arama bir adımda bulunur ve zaman karmaşıklığı O(1)'dir.

*En Kötü Durum: Veri kümesi tamamen taranması gerektiği durumdur. Örneğin, hedeflenen öğe veri kümesinin ortasında bulunuyorsa veya veri kümesi tamamen rastgele sıralanmışsa, en kötü durum zaman karmaşıklığı O(n)'dir, n veri kümesindeki öğe sayısını temsil eder.

*Ortalama Durum: Veri kümesinin rastgele seçildiği ve herhangi bir özel düzen içermediği varsayıldığında, çift yönlü arama algoritmasının ortalama durum zaman karmaşıklığı O(log n)'dir.

Bu sınırlar, algoritmanın performansını tahmin etmek için kullanılabilir ve çift yönlü arama algoritmasının veri kümesindeki hedeflenen öğeyi hızlı bir şekilde bulma yeteneğini belirler.


Çift yönlü arama algoritmasının matematiksel ve asimptotik analizi için Boyer-Moore algoritması örnek kullanılabilir. Boyer-Moore algoritması, bir metin içinde bir kalıbın eşleşmesini bulmak için çift yönlü bir yaklaşım kullanır ve karakter kaydırma ve kelime kaydırma adı verilen iki farklı strateji kullanarak hızlı bir şekilde eşleşmeyi bulmayı hedefler.

Matematiksel Analiz:

Boyer-Moore algoritmasının zaman karmaşıklığı, metnin uzunluğuna (n) ve kalıbın uzunluğuna (m) bağlıdır. Algoritma, karakter kaydırma ve kelime kaydırma stratejilerini kullanarak eşleşme bulmayı hızlandırır.

Karakter Kaydırma Stratejisi: Kalıp ile metin arasında eşleşmeyen bir karakter bulunduğunda, kalıbı doğrudan bu karakterin sağ tarafına kaydırır. Bu durumda kaydırma işlemi sabit bir adımda gerçekleştirilir ve O(1) karmaşıklığı vardır.

Kelime Kaydırma Stratejisi: Kalıp ile metin arasında eşleşmeyen bir kelime bulunduğunda, kalıbı kelimenin sağ tarafına kaydırır. Kelime kaydırma stratejisi, bir karakterin birden fazla eşleşme bulunma olasılığını dikkate alır ve kaydırma miktarını daha fazla azaltabilir. Bu durumda kaydırma işlemi O(m) karmaşıklığına sahiptir.

Boyer-Moore algoritmasının en iyi durumu, eşleşmenin hemen başta bulunduğu durumdur ve karakter kaydırma stratejisi kullanıldığında bu durumda zaman karmaşıklığı O(1)'dir. En kötü durum ise kalıpın her karakteri metin içinde eşleşmediğinde ve kelime kaydırma stratejisi kullanıldığında oluşur ve bu durumda zaman karmaşıklığı O(nm)'dir.

Asimptotik Analiz:
*En İyi Durum: O(1)
*En Kötü Durum: O(nm)
*Ortalama Durum: O(nm)

Sonuç olarak, Boyer-Moore algoritması çift yönlü bir arama algoritmasıdır ve karakter kaydırma ve kelime kaydırma stratejilerini kullanarak eşleşme bulmayı hızlandırır. Zaman karmaşıklığı, metnin uzunluğu ve kalıbın uzunluğuna bağlı olarak değişir ve en iyi durumda O(1), en kötü durumda O(nm) karmaşıklığına sahiptir.
