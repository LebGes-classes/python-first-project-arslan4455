import sys

from Menu import (
    Menu,
)
from Renderer import (
    Renderer,
)
from InputHandler import (
    InputHandler,
)
from Maze import (
    Maze,
)
from Player import (
    Player,
)


class Game:
    """Основной класс игры, управляющий игровым процессом."""
    
    def __init__(self):
        """Инициализирует игровые компоненты."""
        
        self.menu = Menu()
        self.renderer = Renderer()
        self.input_handler = InputHandler()

    def start(self) -> None:
        """Запускает цикл с меню."""

        while True:
            self.menu.show()
            choice = self.menu.get_choice()

            if choice == "1":
                self.run()
            elif choice == "2":
                sys.exit()

    def run(self) -> None:
        """
        Запускает основной игровой процесс.
        
        Создает лабиринт и игрока, затем управляет игровым циклом
        до тех пор, пока игрок не найдет выход или не выйдет из игры.
        """

        maze = Maze(21, 21)
        player = Player(1, 1)

        while True:
            self.renderer.draw(maze, player)

            if maze.is_exit(player.x, player.y):
                print("🎉 Вы нашли выход!")
                input("Нажмите Enter...")
                break

            dx, dy = self.input_handler.get_move()
            player.move(dx, dy, maze)