class Node:
    """A single node in the circular linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    """Circular list of patients for a round-robin check-up system."""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        """Adds a new patient to the circular list."""
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
            return

        last = self.head
        while last.next is not self.head:
            last = last.next

        last.next = new_node
        new_node.next = self.head

    def create_from_list(self, patient_list):
        """Creates a circular list from a Python list."""
        if not patient_list:
            print("Input list is empty. Nothing created.")
            return

        self.head = None

        for patient in patient_list:
            self.append(patient)

        print(f"Successfully created Circular Linked List with {len(patient_list)} patients.")

    def display(self):
        """Displays the circular list."""
        if self.is_empty():
            print("The patient list is empty.")
            return

        patients = []
        current = self.head

        while True:
            patients.append(current.data)
            current = current.next
            if current is self.head:
                break

        print("\n--- Current Check-Up Order (Circular Cycle) ---")
        print(" -> ".join(patients) + f" -> ({self.head.data})")
        print("----------------------------------------------")
        print(f"Total Patients: {len(patients)}")

    def insert_after(self, target_data, new_data):
        """Inserts new_data after target_data."""
        if self.is_empty():
            print("Cannot insert: List is empty.")
            return False

        current = self.head

        while True:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                print(f"Inserted '{new_data}' after '{target_data}'.")
                return True

            current = current.next
            if current is self.head:
                break

        print(f"Insertion failed: '{target_data}' not found.")
        return False

    def delete(self, data_to_delete):
        """Deletes the first occurrence of data."""
        if self.is_empty():
            print("Deletion failed: List is empty.")
            return False

        current = self.head
        prev = None

        while True:
            if current.data == data_to_delete:
                break
            prev = current
            current = current.next

            if current is self.head:
                print(f"Deletion failed: '{data_to_delete}' not found.")
                return False

        # Case 1: Only one node
        if current is self.head and current.next is self.head:
            self.head = None
            print(f"Deleted '{data_to_delete}'. The list is now empty.")
            return True

        # Case 2: Deleting head
        if current is self.head:
            last = self.head
            while last.next is not self.head:
                last = last.next

            self.head = current.next
            last.next = self.head
            print(f"Deleted Head: '{data_to_delete}'. New head is '{self.head.data}'.")
            return True

        # Case 3: Delete normal node
        prev.next = current.next
        print(f"Deleted '{data_to_delete}'.")
        return True


# ---------------- DEMO EXAMPLE ----------------

if __name__ == "__main__":
    print("--- Circular Linked List Demo: Round-Robin Check-Up System ---")

    cll = CircularLinkedList()
    
    # Indian patient names
    initial_patients = ["P1: Rahul", "P2: Meena", "P3: Karthik"]

    print("\n[Action 1] Creating the list:")
    cll.create_from_list(initial_patients)
    cll.display()

    print("\n[Action 2] Insert 'P4: Aishwarya' after 'P2: Meena':")
    cll.insert_after("P2: Meena", "P4: Aishwarya")
    cll.display()

    print("\n[Action 3] Delete 'P3: Karthik':")
    cll.delete("P3: Karthik")
    cll.display()
