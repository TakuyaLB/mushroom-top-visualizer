import pygame

pygame.init()


win = pygame.display.set_mode((1300, 700))

pygame.display.set_caption("Boxes")


class Animation:
    def __init__(self, list_nums):
        self.list_nums = list_nums
        self.size = len(self.list_nums)
        self.rect_positions = {}
        self.text_objects = {}
        self.width, self.height = 1300, 700
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.space = 10
        self.box_size = 60
        self.left_border, self.top_border = (self.width - ((self.box_size * self.size) + ((self.size - 1) * self.space))) // 2, (self.height - self.box_size) // 2
        for i, n in enumerate(list_nums):
            self.rect_positions[n] = pygame.Rect(self.left_border + (self.box_size + self.space) * i, self.top_border, self.box_size, self.box_size)
            text = self.font.render(str(list_nums[i]), True, 'white')
            text_rect = text.get_rect()
            text_rect.center = (self.left_border + (self.box_size + self.space) * i + self.box_size // 2), (self.top_border + self.box_size // 2)
            self.text_objects[list_nums[i]] = text

    def draw_boxes(self, win):
        win.fill((0, 0, 0))
        for i, n in enumerate(self.list_nums):
            pygame.draw.rect(win, 'red', self.rect_positions[n])
            text = self.text_objects[n]
            text_rect = text.get_rect()
            text_rect.center = self.rect_positions[n].center
            win.blit(text, text_rect)
        pygame.display.update()

    def move_down(self, num1, dist):
        rect = self.rect_positions.get(num1)

        x1, y1, x2, y2 = self.rect_positions[num1]
        step = 100

        print(y1)

        rect.y += step
        self.draw_boxes(win)
        pygame.time.delay(1000)

        target_x1 = ((dist + 1) * (self.box_size) + (dist + 1) * (self.space))
        rect.x += target_x1
        self.draw_boxes(win)
        pygame.time.delay(1000)

        rect.y -= step
        self.draw_boxes(win)
        pygame.time.delay(1000)

    def move_up(self, num1, dist):
        rect = self.rect_positions[num1]

        x1, y1, x2, y2 = self.rect_positions[num1]
        step = 100

        rect.y -= step
        self.draw_boxes(win)
        pygame.time.delay(1000)

        target_x1 = ((dist + 1) * (self.box_size) + (dist + 1) * (self.space))
        rect.x -= target_x1
        self.draw_boxes(win)
        pygame.time.delay(1000)

        rect.y += step
        self.draw_boxes(win)
        pygame.time.delay(1000)

    def swap(self, num1, num2):
        list_nums = self.list_nums

        dist = abs(list_nums.index(num1) - list_nums.index(num2)) - 1
        if list_nums.index(num1) < list_nums.index(num2):
            rect1 = self.rect_positions.get(num1)
            rect2 = self.rect_positions.get(num2)
        else:
            rect1 = self.rect_positions.get(num2)
            rect2 = self.rect_positions.get(num1)


        step = 100

        rect1.y += step
        rect2.y -= step
        self.draw_boxes(win)
        pygame.time.delay(1000)

        target_x1 = ((dist + 1) * (self.box_size) + (dist + 1) * (self.space))
        rect1.x += target_x1
        rect2.x -= target_x1
        self.draw_boxes(win)
        pygame.time.delay(1000)

        rect1.y -= step
        rect2.y += step
        self.draw_boxes(win)
        pygame.time.delay(1000)

run = True

animation = Animation([str(i) for i in range(1,7)])
animation.draw_boxes(win)
animation.swap('6', '1')
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    animation.draw_boxes(win)

pygame.quit()