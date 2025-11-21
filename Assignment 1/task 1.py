import uuid

class Patient:
    """Stores patient data: Name, Age, and unique ID."""
    def __init__(self, name: str, age: int, patient_id: str):
        self.name = name
        self.age = age
        self.patient_id = patient_id

    def __str__(self):
        return f"ID: {self.patient_id} | Name: {self.name} | Age: {self.age}"

class Node:
    """Represents a node in the list, holding patient data and the next node reference."""
    def __init__(self, patient_data: Patient):
        self.data = patient_data
        self.next = None

class SinglyLinkedList:
    """Manages Patient records using a Singly Linked List."""
    def __init__(self):
        self.head = None

    def insert_patient_at_end(self, name: str, age: int):
        """
        Creates a new patient, assigns a unique ID, and inserts it at the end.
        Returns the generated ID.
        """
        # Generate a unique ID (first 8 chars of a UUID)
        patient_id = str(uuid.uuid4())[:8]
        new_patient = Patient(name, age, patient_id)
        new_node = Node(new_patient)

        if self.head is None:
            self.head = new_node
            print(f"-> Inserted Head: {new_patient.name} (ID: {patient_id})")
            return new_patient.patient_id

        # Traverse to the end
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        print(f"-> Inserted Tail: {new_patient.name} (ID: {patient_id})")
        return new_patient.patient_id


    def delete_patient_by_id(self, patient_id: str):
        """Deletes the node with the matching patient_id."""
        current = self.head
        previous = None

        # Case 1: Head is the target
        if current and current.data.patient_id == patient_id:
            self.head = current.next
            print(f"<- Deleted Head Patient (ID: {patient_id}).")
            return

        # Case 2: Search for the ID
        while current and current.data.patient_id != patient_id:
            previous = current
            current = current.next

        # Not found
        if current is None:
            print(f"!! Error: Patient ID '{patient_id}' not found.")
            return

        # Found: Unlink the node
        deleted_name = current.data.name
        previous.next = current.next
        print(f"<- Deleted Patient: {deleted_name} (ID: {patient_id}).")


    def display_patients(self):
        """Prints all patient records in the list."""
        print("\n--- Current Patient Registry ---")
        if self.head is None:
            print("The registry is empty.")
            return

        current = self.head
        while current:
            print(f"-> {current.data}")
            current = current.next
        print("--------------------------------")


# --- Example Usage ---

registry = SinglyLinkedList()
print("--- Starting Registry Operations ---")

# Insertion (saving IDs for later deletion)
id_a = registry.insert_patient_at_end("Alice Smith", 45)
id_b = registry.insert_patient_at_end("Bob Johnson", 72)
id_c = registry.insert_patient_at_end("Charlie Brown", 28)

registry.display_patients()

# Deletion
print("\n--- Deletion Operations ---")

# 1. Delete the middle item (Bob)
registry.delete_patient_by_id(id_b)
registry.display_patients()

# 2. Delete the new head (Alice)
registry.delete_patient_by_id(id_a)
registry.display_patients()

registry.display_patients()
