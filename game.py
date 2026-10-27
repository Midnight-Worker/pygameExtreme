import pygame

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1800, 1080))
        self.clock = pygame.time.Clock()
        self.running = True

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
