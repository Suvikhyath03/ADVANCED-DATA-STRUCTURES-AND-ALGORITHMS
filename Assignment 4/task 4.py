import sys
sys.setrecursionlimit(2000)

# -----------------------------------------------------------
# 1. RECURSIVE SOLUTION
# -----------------------------------------------------------

def hanoi_recursive(n, source, auxiliary, destination):
    """
    Solves the Towers of Hanoi problem using recursion.
    n : number of disks
    source : from pole
    auxiliary : helper pole
    destination : target pole
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move n-1 disks to auxiliary
    hanoi_recursive(n - 1, source, destination, auxiliary)

    # Move largest disk
    print(f"Move disk {n} from {source} to {destination}")

    # Move n-1 disks to destination
    hanoi_recursive(n - 1, auxiliary, source, destination)


# -----------------------------------------------------------
# 2. ITERATIVE STACK-BASED SOLUTION
# -----------------------------------------------------------

def _is_legal_move(source_stack, destination_stack):
    """Checks if moving top disk is legal."""
    if not source_stack:
        return False

    if not destination_stack:
        return True

    return source_stack[-1] < destination_stack[-1]


def _transfer_disk(source_stack, destination_stack, source_name, destination_name):
    """Moves a disk between stacks if legal."""
    if _is_legal_move(source_stack, destination_stack):
        disk = source_stack.pop()
        destination_stack.append(disk)
        print(f"Move disk {disk} from {source_name} to {destination_name}")
        return True
    return False


def hanoi_iterative_stack_based(n, source_name='A', auxiliary_name='B', destination_name='C'):
    """
    Solves Towers of Hanoi using stacks (iterative).
    """
    pole_a = list(range(n, 0, -1))
    pole_b = []
    pole_c = []

    poles = {
        source_name: pole_a,
        auxiliary_name: pole_b,
        destination_name: pole_c
    }

    total_moves = (2 ** n) - 1

    if n % 2 == 0:
        pole_names = [source_name, auxiliary_name, destination_name]
    else:
        pole_names = [source_name, destination_name, auxiliary_name]

    print(f"\nInitial State: A={pole_a}, B={pole_b}, C={pole_c}")

    for i in range(1, total_moves + 1):

        if i % 2 != 0:
            # Move disk 1 cyclically
            current_pole_index = (i // 2) % 3
            next_pole_index = (current_pole_index + 1) % 3

            p1 = pole_names[current_pole_index]
            p2 = pole_names[next_pole_index]

            if poles[p1] and poles[p1][-1] == 1:
                _transfer_disk(poles[p1], poles[p2], p1, p2)
            else:
                _transfer_disk(poles[p2], poles[p1], p2, p1)

        else:
            # Non-smallest-disk moves
            if _transfer_disk(poles[source_name], poles[auxiliary_name], source_name, auxiliary_name): continue
            if _transfer_disk(poles[auxiliary_name], poles[source_name], auxiliary_name, source_name): continue

            if _transfer_disk(poles[source_name], poles[destination_name], source_name, destination_name): continue
            if _transfer_disk(poles[destination_name], poles[source_name], destination_name, source_name): continue

            if _transfer_disk(poles[auxiliary_name], poles[destination_name], auxiliary_name, destination_name): continue
            if _transfer_disk(poles[destination_name], poles[auxiliary_name], destination_name, auxiliary_name): continue

    print(f"\nFinal State: A={poles[source_name]}, B={poles[auxiliary_name]}, C={poles[destination_name]}")


# -----------------------------------------------------------
# MAIN DRIVER CODE
# -----------------------------------------------------------

if __name__ == "__main__":
    NUMBER_OF_DISKS = 3

    print("=" * 50)
    print(f"TOWERS OF HANOI (N={NUMBER_OF_DISKS}) - RECURSIVE SOLUTION")
    print("=" * 50)
    hanoi_recursive(NUMBER_OF_DISKS, 'A', 'B', 'C')
    print("=" * 50)

    print("\n" * 2)

    print("=" * 50)
    print(f"TOWERS OF HANOI (N={NUMBER_OF_DISKS}) - ITERATIVE STACK-BASED SOLUTION")
    print("=" * 50)
    hanoi_iterative_stack_based(NUMBER_OF_DISKS, 'A', 'B', 'C')
    print("=" * 50)
