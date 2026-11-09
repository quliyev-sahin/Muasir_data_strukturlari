import time
from collections import deque


print("   AĞILLI ANBAR VƏ SİFARİŞ İDARƏETMƏ SİSTEMİ       ")


# 1. HASH TABLE (Chaining) - Məhsul Kataloqu

class WarehouseCatalog:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def add_product(self, sku, name, price):
        index = self._hash(sku)
        for item in self.table[index]:
            if item['sku'] == sku:
                item['name'] = name
                item['price'] = price
                return
        self.table[index].append({'sku': sku, 'name': name, 'price': price})

    def get_product(self, sku):
        index = self._hash(sku)
        for item in self.table[index]:
            if item['sku'] == sku:
                return item
        return None


# 2. BINARY SEARCH TREE (BST) - Sürətli Məhsul Axtarışı

class BSTNode:
    def __init__(self, product_id, name):
        self.id = product_id
        self.name = name
        self.left = None
        self.right = None

class ProductSearchTree:
    def __init__(self):
        self.root = None

    def insert(self, product_id, name):
        if not self.root:
            self.root = BSTNode(product_id, name)
        else:
            self._insert_rec(self.root, product_id, name)

    def _insert_rec(self, curr, product_id, name):
        if product_id < curr.id:
            if not curr.left: curr.left = BSTNode(product_id, name)
            else: self._insert_rec(curr.left, product_id, name)
        elif product_id > curr.id:
            if not curr.right: curr.right = BSTNode(product_id, name)
            else: self._insert_rec(curr.right, product_id, name)

    def search(self, product_id):
        return self._search_rec(self.root, product_id)

    def _search_rec(self, curr, product_id):
        if not curr or curr.id == product_id:
            return curr
        if product_id < curr.id:
            return self._search_rec(curr.left, product_id)
        return self._search_rec(curr.right, product_id)


# 3. STACK, QUEUE VƏ DEQUE - Sifariş və Əməliyyat İdarəetməsi

class OrderManagementSystem:
    def __init__(self):
        self.standard_queue = deque()  # Queue (FIFO) - Standart sifarişlər
        self.express_deque = deque()   # Deque - VIP / Təcili sifarişlər (həmçinin başdan/sondan əlavə)
        self.action_stack = []         # Stack (LIFO) - Əməliyyat tarixçəsi (Undo üçün)

    def place_order(self, customer, is_express=False):
        if is_express:
            self.express_deque.append(customer)
            print(f"[Express Queue] VIP Sifariş əlavə olundu: {customer}")
        else:
            self.standard_queue.append(customer)
            print(f"[Standard Queue] Sifariş növbəyə alındı: {customer}")

    def process_order(self):
        # Əvvəlcə təcili sifarişlərə baxılır
        if self.express_deque:
            cust = self.express_deque.popleft()
            print(f"--> [VIP] Çatdırılır: {cust}")
        elif self.standard_queue:
            cust = self.standard_queue.popleft()
            print(f"--> [Standart] Çatdırılır: {cust}")
        else:
            print("Növbədə gözləyən sifariş yoxdur.")

    def log_action(self, action):
        self.action_stack.append(action)
        print(f"[Stack Log] Əməliyyat qeydə alındı: {action}")

    def undo_last_action(self):
        if self.action_stack:
            last = self.action_stack.pop()
            print(f"[Stack Undo] Son əməliyyat ləğv edildi: {last}")
        else:
            print("Ləğv ediləcək əməliyyat yoxdur.")


# 4. LİNKED LIST - Məhsulun Daşınma İzləməsi

class TrackingNode:
    def __init__(self, location):
        self.location = location
        self.next = None
        self.prev = None

class ShipmentTracking:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_milestone(self, location):
        new_node = TrackingNode(location)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def print_forward(self):
        curr = self.head
        path = []
        while curr:
            path.append(curr.location)
            curr = curr.next
        print("Daşınma zənciri (İrəli):", " -> ".join(path))


# 5. DİNAMİK ARRAY - Günlük Logların Performans Testi

def run_dynamic_array_logs():
    print("\n--- 5. Dinamik Array Performans Testi (Günlük Loglar) ---")
    logs = []
    start = time.time()
    for i in range(10000):
        logs.append(f"Log_ID_{i}")
    end = time.time()
    print(f"10,000 log dinamik massivə sona əlavə edildi: {(end - start):.6f} san")



# TƏTBİQİN İŞƏ SALINMASI VƏ İNTEQRASİYASI

if __name__ == "__main__":
    # 1. Hash Table ilə Məhsul Kataloqu yaradaq
    catalog = WarehouseCatalog(capacity=3)
    catalog.add_product("SKU-101", "Noutbuk", 1500)
    catalog.add_product("SKU-102", "Siçan", 25)
    catalog.add_product("SKU-103", "Klaviatura", 50)
    print("1. Hash Table-dən məhsul oxunur (SKU-102):", catalog.get_product("SKU-102"))

    # 2. BST ilə Sürətli İndeksleme
    bst = ProductSearchTree()
    bst.insert(101, "Noutbuk")
    bst.insert(105, "Monitor")
    bst.insert(102, "Siçan")
    found = bst.search(105)
    print(f"2. BST Axtarış nəticəsi (ID 105): {found.name if found else 'Tapılmadı'}")

    # 3. Stack, Queue və Deque Sifariş İdarəetməsi
    oms = OrderManagementSystem()
    oms.log_action("Məhsul əlavə olundu: Noutbuk")
    oms.place_order("Elmir (Standart)")
    oms.place_order("Leyla (VIP Express)", is_express=True)
    
    print("\nSifarişlərin icra mərhələsi:")
    oms.process_order() # Əvvəlcə Express çıxacaq
    oms.process_order() # Sonra Standart
    
    oms.undo_last_action() # Stack yoxlaması

    # 4. Doubly Linked List ilə Daşınma İzləmə
    shipment = ShipmentTracking()
    shipment.add_milestone("Təchizatçı Anbarı")
    shipment.add_milestone("Logistika Mərkəzi")
    shipment.add_milestone("Müştəri Ünvanı")
    print("\n4. Linked List:")
    shipment.print_forward()

    # 5. Dinamik Array Logları
    run_dynamic_array_logs()