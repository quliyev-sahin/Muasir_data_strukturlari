# Muasir_data_strukturlari
Data structure task
Bu konsol tətbiqi proqramlaşdırmanın ən təməl 5 strukturunu və alqoritmini bir araya gətirərək, onların real həyat ssenarilərində necə istifadə olunduğunu, daxili iş mexanizmlərini və performans fərqlərini əyani şəkildə nümayiş etdirmək üçün dizayn edilmişdir.Tətbiqin funksiyaları, struktur seçimlərinin əsasları və performans ölçümlərinin nəticələri aşağıdakı kimidir:

1. Array və Dynamic ArrayArray (Sabit həcmli): Yaddaşda sərt (ardıcıl) yer tutur. İndeks ilə birbaşa müraciət sürətlidir ($O(1)$), lakin ölçünü dəyişmək çətindir.Dynamic Array: Ölçüsü dolduqda avtomatik olaraq daha böyük yaddaş sahəsi ayırır və mövcud elementləri köçürür.Sonuna əlavə etmək (append): Amortizasiya olunmuş şəkildə $O(1)$ vaxt aparır.Əvvəle və ya orta yerə əlavə etmək (insert): Bütün sonrakı elementlərin sağa sürüşdürülməsi tələb olunduğu üçün $O(n)$ vaxt tələb edir.

2. Singly və Doubly Linked ListSingly Linked List: Hər qovşaq özündən sonrakı elementin ünvanını (next) saxlayır. Yaddaşa qənaətcildir, lakin yalnız irəliyə doğru hərəkət etmək mümkündür.Doubly Linked List: Hər qovşaq həm sonrakı (next), həm də əvvəlki (prev) qovşağın ünvanını saxlayır. Geriyə hərəkət və silmə əməliyyatları daha rahatdır, lakin əlavə yaddaş tələb edir.

3. Stack, Queue və Deque TətbiqləriStack (LIFO - Son girən ilk çıxır): Mötərizələrin düzgün açılıb-bağlanmasını yoxlamaq (syntax parsing) üçün idealdır.Queue (FIFO - İlk girən ilk çıxır): Printer növbələri və ya tapşırıq planlayıcılarında (Task Scheduler) istifadə olunur.Deque (Double-ended Queue): Hər iki ucundan element əlavə edib-çıxarmağa imkan verir. Palindrom yoxlanılması və ya "Browser History" (geri-irəli düymələri) üçün əlverişlidir.

4. Hash Table (Chaining üsulu)Hash funksiyası eyni indeksə düşən (collision) fərqli açarları birbaşa üst-üstə yazmır. Həmin indeksdə bir zəncir (linked list və ya siyahı) yaradaraq elementləri orada saxlayır.Axtarış və əlavə etmə zamanı əgər toqquşma azdırsa vaxt mürəkkəbliyi ortalama $O(1)$, ən pis halda isə $O(n)$ olur.

5. Binary Search Tree (BST) və Sıralanmış Verilənlərin TəsiriƏməliyyatlar: Əlavə etmə (insert), Axtarış (search) və Silmə (delete) orta hesabla $O(\log n)$ mürəkkəbliyə malikdir.Sıralanmış verilənlərin əlavə edilməsinin təsiri: Əgər ağaca elementlər artıq sıralanmış şəkildə (məsələn: 10, 20, 30, 40, 50) əlavə olunarsa, ağac balansını itirərək çubuqvari (skewed tree) formaya düşür. Nəticədə ağacın hündürlüyü $n$-ə bərabər olur və bütün əməliyyatların sürəti $O(n)$-ə (adi siyahı kimi) enir. Bunun qarşısını almaq üçün AVL və ya Qırmızı-Qara ağaclar (Self-balancing trees) istifadə olunur.


------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bu 5 mövzunu bir araya gətirmək üçün real həyat ssenarisinə əsaslanan "Ağıllı Anbar və Sifariş İdarəetmə Sistemi" (Smart Warehouse & Order Management System) adlı vahid konsol tətbiqi dizayn edilmişdir:

1.Hash Table (Chaining): Məhsulların kataloqunda SKU (məhsul kodu) vasitəsilə məlumatların sürətli ($O(1)$) axtarışı və toqquşmaların idarə edilməsi üçün.

2.Binary Search Tree (BST): Anbarda məhsulların ID və ya qiymətə görə indekslənməsi və sürətli filtrlənməsi üçün.

3.Queue və Deque: Müştəri sifarişlərinin növbəsi (Standart sifarişlər üçün Queue, təcili VIP sifarişlər üçün isə həm əvvəldən, həm sondan idarə olunan Deque).

4.Stack: Anbarda edilən son əməliyyatların (məsələn, məhsul əlavəetmə/silmə) Undo (Geri al) mexanizmi ilə idarə olunması üçün.

5.Array & Dynamic Array: Gün sonu hesabatlarının və toplu məlumatların yaddaşda saxlanılması və performans analizi üçün.

6.Singly / Doubly Linked List: Məhsulun anbar daxilində daşınma mərhələlərinin (təchizatçı $\to$ rəf $\to$ qablaşdırma) izlənməsi üçün.

Tətbiqin İşləmə Mexanizminin Qısa İzahı:
Bu konsol tətbiqi işə düşdükdə anbar sistemində eyni anda 5 mühüm struktur işləyir:

Hash Table anbara gələn məhsul kodlarını dərhal tapır.

BST məhsul ID-lərinə görə iyerarxik axtarış təmin edir.

Queue & Deque müştəri sifarişlərini prioritetə uyğun olaraq (normal və təcili) növbəyə qoyub icra edir.

Stack işçinin etdiyi son əməliyyatı yadda saxlayır və lazım gəldikdə geri (Undo) qaytarır.

Doubly Linked List məhsulun çatdırılma mərhələlərini səliqəli şəkildə bir-birinə bağlayır, Dynamic Array isə sistem loglarını yüksək sürətlə qeydə alır.
