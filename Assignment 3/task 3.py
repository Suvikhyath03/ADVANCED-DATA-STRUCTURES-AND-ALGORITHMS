import sys
# Higher recursion limit (not required for this example, but safe)
sys.setrecursionlimit(2000)


class UndoRedoSystem:
    """
    Implements an Undo-Redo system using two stacks:
    1. undo_stack  – main history of actions
    2. redo_stack  – stores undone actions
    """

    def __init__(self):
        self.undo_stack = []   # Current action history
        self.redo_stack = []   # Undone actions stored here

    def push(self, action: str):
        """
        Performs a new action.
        Adds to undo stack and clears redo stack.
        """
        self.undo_stack.append(action)
        # Any new action clears redo history
        self.redo_stack.clear()
        self.display_state(f"Action '{action}' performed.")

    def undo(self):
        """
        Undo last action.
        Move top of undo stack → redo stack.
        """
        if not self.undo_stack:
            self.display_state("Cannot undo. History is empty.")
            return

        last_action = self.undo_stack.pop()
        self.redo_stack.append(last_action)
        self.display_state(f"Action '{last_action}' undone.")

    def redo(self):
        """
        Redo last undone action.
        Move top of redo stack → undo stack.
        """
        if not self.redo_stack:
            self.display_state("Cannot redo. No actions have been undone.")
            return

        undone_action = self.redo_stack.pop()
        self.undo_stack.append(undone_action)
        self.display_state(f"Action '{undone_action}' redone.")

    def display_state(self, operation: str):
        """
        Shows both stacks after every operation.
        """
        print(f"\n--- {operation} ---")
        print(f"Undo History: {self.undo_stack}")
        print(f"Redo Buffer:  {self.redo_stack}")
        print("-" * 30)


# ---------------- Example Demo ----------------

if __name__ == "__main__":
    system = UndoRedoSystem()
    print("Starting Simplified Undo/Redo Demo")

    # 1. Perform actions
    system.push("A")
    system.push("B")
    system.push("C")

    # 2. Undo last action
    system.undo()

    # 3. Redo the undone action
    system.redo()
