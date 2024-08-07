import random
def get_user_move(heap):
    while True:
        try:
            sticks_to_remove = int(input(f"Enter sticks to remove (1 to {min(heap, heap // 2)}): "))
            if 1 <= sticks_to_remove <= min(heap, heap // 2):
                return sticks_to_remove
            else:
                print(f"Invalid input (1 to {min(heap, heap // 2)}).")
        except ValueError:
            print("Invalid input. Enter a valid number.")

def get_computer_move(heap):
    xor_sum = heap
    for i in range(heap):
        xor_sum ^= i
    max_sticks = min(heap, heap // 2) if xor_sum == 0 else min(heap // 2, heap)
    return random.randint(1, max_sticks)

def nim_game():
    heap = 40
    player_turn = 1
    while heap > 1:
        print(f"Current heap: {'|' * heap}")
        player_name = "User" if player_turn == 1 else "Computer"
        sticks_to_remove = get_user_move(heap) if player_turn == 1 else get_computer_move(heap)
        heap -= sticks_to_remove
        print(f"{player_name} removes {sticks_to_remove} sticks.")
        player_turn = 3 - player_turn
    winner = "User" if player_turn == 2 else "Computer"
    print(f"\n{winner} is the winner!")

if __name__ == "__main__":
    nim_game()