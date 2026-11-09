import time
import random
from collections import deque

# 1. ARRAY VƏ DİNAMİK ARRAY (PERFORMANS TESTİ)
def run_array_benchmark():
    print("--- 1. Array və Dynamic Array Performans Testi ---")
    sizes = [1000, 10000, 50000]
    
    for n in sizes:
        
        start = time.time()
        dyn_arr = []
        for i in range(n):
            dyn_arr.append(i)
        end = time.time()
        print(f"Həcm: {n:5d} | Sona əlavə (append): {(end - start):.6f} san")

        
        limit = min(n, 5000) 
        start = time.time()
        dyn_arr_front = []
        for i in range(limit):
            dyn_arr_front.insert(0, i)
        end = time.time()
        print(f"Həcm: {limit:5d} | Əvvəle əlavə (insert(0)): {(end - start):.6f} san")
        print("-" * 55)
    print()


# 2. SINGLY VƏ DOUBLY LINKED LIST

class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = SinglyNode(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

def run_linked_list_demo():
    print("--- 2. Singly və Doubly Linked List Demo ---")
    s_list = SinglyLinkedList()
    s_list.append(10)
    s_list.append(20)
    print("Singly Linked List yaradıldı və elementlər əlavə olundu: 10 -> 20")

    d_list = DoublyLinkedList()
    d_list.append(100)
    d_list.append(200)
    print("Doubly Linked List yaradıldı: 100 <-> 200 (Həm irəli, həm geri hərəkət mümkündür)")
    print()


# 3. STACK, QUEUE VƏ DEQUE TƏTBİQLƏRİ

def run_stack_queue_deque_demo():
    print("--- 3. Stack, Queue və Deque Tətbiqləri ---")
    
    # A) Stack (LIFO) - Mötərizələrin balansının yoxlanılması
    def is_balanced(expression):
        stack = []
        for char in expression:
            if char in "({[":
                stack.append(char)
            elif char in ")}]":
                if not stack: return False
                top = stack.pop()
                if (top == '(' and char != ')') or \
                   (top == '{' and char != '}') or \
                   (top == '[' and char != ']'):
                    return False
        return len(stack) == 0

    expr = "{[a + (b * c)] - d}"
    print(f"Stack tətbiqi (Mötərizə yoxlama): '{expr}' balanslıdırmı? -> {is_balanced(expr)}")

    # B) Queue (FIFO) - Printer Növbəsi Simulyasiyası
    print("\nQueue tətbiqi (Printer Növbəsi):")
    printer_queue = deque()
    printer_queue.append("Sened_1.pdf")
    printer_queue.append("Hesabat.docx")
    print("Növbəyə əlavə olundu:", list(printer_queue))
    print("Çap edilir:", printer_queue.popleft())
    print("Növbədə qalanlar:", list(printer_queue))

    # C) Deque (Double-ended Queue) - Palindrom yoxlanılması
    def check_palindrome(word):
        d = deque(word)
        while len(d) > 1:
            if d.popleft() != d.pop():
                return False
        return True
    
    word = "radar"
    print(f"\nDeque tətbiqi (Palindrom yoxlama): '{word}' sözü palindromdursa -> {check_palindrome(word)}")
    print()

# 4. HASH TABLE (CHAINING ÜSULU İLƏ COLLISION HƏLLİ)
class HashTableChaining:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

def run_hash_table_demo():
    print("--- 4. Hash Table (Chaining Collision Həlli) ---")
    ht = HashTableChaining(capacity=3) # Kiçik həcm seçirik ki, collision (toqquşma) tez baş versin
    ht.insert("Alma", 5)
    ht.insert("Banan", 10)
    ht.insert("Gilas", 15)
    ht.insert("Nar", 20) # Eyni bucket-ə düşmə ehtimalını artırırıq

    print("Alma:", ht.get("Alma"))
    print("Banan:", ht.get("Banan"))
    print("Nar:", ht.get("Nar"))
    print("Daxili Struktur (Chaining Bucket-ləri):", ht.table)
    print()

# 5. BINARY SEARCH TREE (BST)
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = BSTNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, curr, key):
        if key < curr.key:
            if not curr.left:
                curr.left = BSTNode(key)
            else:
                self._insert_rec(curr.left, key)
        elif key > curr.key:
            if not curr.right:
                curr.right = BSTNode(key)
            else:
                self._insert_rec(curr.right, key)

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, curr, key):
        if not curr or curr.key == key:
            return curr is not None
        if key < curr.key:
            return self._search_rec(curr.left, key)
        return self._search_rec(curr.right, key)

    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, curr, key):
        if not curr:
            return curr
        if key < curr.key:
            curr.left = self._delete_rec(curr.left, key)
        elif key > curr.key:
            curr.right = self._delete_rec(curr.right, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            
            # İki övladı olan qovşaq üçün sağ alt ağacın ən kiçik elementini tapırıq
            curr.key = self._min_value(curr.right)
            curr.right = self._delete_rec(curr.right, curr.key)
        return curr

    def _min_value(self, curr):
        while curr.left:
            curr = curr.left
        return curr.key

def run_bst_demo():
    print("--- 5. Binary Search Tree (BST) Demo ---")
    bst = BST()
    elements = [50, 30, 70, 20, 40, 60, 80]
    for el in elements:
        bst.insert(el)
    
    print(f"Ağaca əlavə edildi: {elements}")
    print(f"40 nömrəli element tapıldımı? -> {bst.search(40)}")
    
    bst.delete(30)
    print("30 silindi. İndi 30 axtarılır ->", bst.search(30))
    print()

if __name__ == "__main__":
    run_array_benchmark()
    run_linked_list_demo()
    run_stack_queue_deque_demo()
    run_hash_table_demo()
    run_bst_demo()