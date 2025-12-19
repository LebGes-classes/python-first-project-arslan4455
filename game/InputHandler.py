import sys


class InputHandler:
    """Класс для обработки пользовательского ввода во время игры."""
    
    MOVES = {
        "w": (0, -1),
        "s": (0, 1),
        "a": (-1, 0),
        "d": (1, 0),
    }

    def get_move(self) -> tuple[int, int]:
        """
        Получает и обрабатывает ввод пользователя для движения.
        
        Returns:
            tuple[int, int]: Кортеж (dx, dy) представляющий направление движения
        """

        key = input("Ваш ход (WASD, Q): ").lower()

        if key == "q":
            sys.exit()
            
        return self.MOVES.get(key, (0, 0))

