class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_after(self, target_data, data):
        current = self.head
        while current is not None:
            if current.data == target_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def delete_node(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                print("Element tapıldı.")
                return True
            current = current.next
        print("Element tapılmadı.")
        return False

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        print(f"List length = {count}")
        return count

    def find_min_max(self):
        if self.head is None:
            return None, None
        min_val = self.head.data
        max_val = self.head.data
        current = self.head.next
        while current is not None:
            if current.data < min_val:
                min_val = current.data
            if current.data > max_val:
                max_val = current.data
            current = current.next
        print(f"Minimum: {min_val}")
        print(f"Maksimum: {max_val}")
        return min_val, max_val

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class StudentNode:
    def __init__(self, student_id, student_name, gpa):
        self.student_id = student_id
        self.student_name = student_name
        self.gpa = gpa
        self.next = None

class StudentRegistry:
    def __init__(self):
        self.head = None

    def add_student(self, student_id, student_name, gpa):
        new_node = StudentNode(student_id, student_name, gpa)
        new_node.next = self.head
        self.head = new_node

    def delete_student(self, student_id):
        if self.head is None:
            return
        if self.head.student_id == student_id:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.student_id == student_id:
                current.next = current.next.next
                return
            current = current.next

    def show_all(self):
        current = self.head
        while current:
            print(current.student_id, current.student_name, current.gpa)
            current = current.next

    def show_high_gpa(self):
        current = self.head
        while current:
            if current.gpa > 80:
                print(current.student_id, current.student_name, current.gpa)
            current = current.next

    def search_by_name(self, name):
        current = self.head
        found = False
        while current:
            if current.student_name.lower() == name.lower():
                print(current.student_id, current.student_name, current.gpa)
                found = True
            current = current.next
        if not found:
            print("tapilmadi")

    def count_students(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"Cəmi tələbə: {count}")
        return count


l = LinkedList()
l.insert_at_end(10)
l.insert_at_end(20)
l.insert_at_end(40)
l.insert_after(20, 30)
l.display()

l.delete_node(30)
l.display()

l.search(20)
l.search(99)

l2 = LinkedList()
for val in [11, 22, 33, 44, 55]:
    l2.insert_at_end(val)
l2.length()

l3 = LinkedList()
for val in [23, 8, 91, 15, 42]:
    l3.insert_at_end(val)
l3.find_min_max()

l4 = LinkedList()
for val in [10, 20, 30, 40, 50]:
    l4.insert_at_end(val)
l4.reverse()
l4.display()

sr = StudentRegistry()
sr.add_student(1, "Ali", 85)
sr.add_student(2, "Leyla", 92)
sr.add_student(3, "Vaqif", 75)

sr.show_all()
sr.show_high_gpa()
sr.search_by_name("Ali")
sr.count_students()
sr.delete_student(3)
sr.count_students()

empty_list = LinkedList()
empty_list.length()
empty_list.search(99)
empty_list.find_min_max()

test_l = LinkedList()
test_l.insert_at_end(10)
test_l.insert_at_end(20)
test_l.display()
test_l.delete_node(99)
test_l.display()