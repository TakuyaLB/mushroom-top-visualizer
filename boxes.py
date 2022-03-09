import pygame
from dataclasses import dataclass
import random

pygame.init()


win = pygame.display.set_mode((1300, 700))

pygame.display.set_caption("Boxes")


@dataclass
class Number:
    num: int
    rect: pygame.Rect
    text: pygame.Surface


class Animation:
    def __init__(self, list_nums):
        #self.keypress = ""
        self.instructions = []
        self.nums = []
        self.size = len(list_nums)
        self.width, self.height = 1300, 700
        self.space = 10
        self.box_size = int(min((self.width - self.space * (self.size + 1)) / self.size, 60))
        self.font = pygame.font.Font('freesansbold.ttf', int(self.box_size / 2))
        self.left_border = (self.width - ((self.box_size * self.size) + (self.size - 1) * self.space)) // 2
        self.top_border = (self.height - self.box_size) // 2
        for i, n in enumerate(list_nums):
            rect = pygame.Rect(self.left_border + (self.box_size + self.space) * i, self.top_border, self.box_size, self.box_size)
            text = self.font.render(str(list_nums[i]), True, 'white')
            text_rect = text.get_rect()
            text_rect.center = (self.left_border + (self.box_size + self.space) * i + self.box_size // 2), (self.top_border + self.box_size // 2)
            self.nums.append(Number(n, rect, text))

    def draw_boxes(self, win):
        win.fill((0, 0, 0))
        for i, n in enumerate(self.nums):
            rect = n.rect
            pygame.draw.rect(win, 'red', rect)
            text = n.text
            text_rect = text.get_rect()
            text_rect.center = rect.center
            win.blit(text, text_rect)
        pygame.display.update()

    def swap(self, index1, index2):
        if index1 == index2:
            return

        dist = abs(index1 - index2) - 1
        if index1 < index2:
            rect1 = self.nums[index1].rect
            rect2 = self.nums[index2].rect
        else:
            rect1 = self.nums[index2].rect
            rect2 = self.nums[index1].rect


        step = 10
        dist_to_target = self.box_size * 1.5
        ori_y = rect1.y

        while rect1.y <= ori_y + dist_to_target:
            pygame.event.pump()
            rect1.y += step
            rect2.y -= step
            self.draw_boxes(win)
            pygame.time.delay(50)

        ori_x = rect1.x
        target_x1 = ((dist + 1) * self.box_size + (dist + 1) * self.space)
        ori_x2 = rect2.x

        while rect1.x < ori_x + target_x1 - step:
            pygame.event.pump()
            rect1.x += step
            rect2.x -= step
            self.draw_boxes(win)
            pygame.time.delay(50)

        rect1.x = ori_x + target_x1
        rect2.x = ori_x2 - target_x1

        ori_y = rect1.y

        while rect1.y >= ori_y - dist_to_target:
            pygame.event.pump()
            rect1.y -= step
            rect2.y += step
            self.draw_boxes(win)
            pygame.time.delay(50)

        tmp = self.nums[index1]
        self.nums[index1] = self.nums[index2]
        self.nums[index2] = tmp

    def bubble_sort(self):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(self.nums[:-1])):
                if self.nums[i].num > self.nums[i+1].num:
                    self.swap(i, i+1)
                    is_sorted = False
    #Would be easier to show quicksort with splitting function
    def quick_sort(self, low, high, array):
        if low < high:
            pivot = self.partition(low, high, array)
            self.quick_sort(low, pivot - 1, array)
            self.quick_sort(pivot + 1, high, array)
        else:
            print("here2")
            self.step_through()
       
    def partition(self, low, high, array):
        i = low + 1
        j = high
        while j >= i:
            print(array[i], array[j], array[low])
            if array[i] > array[low] and array[j] <= array[low]:
                print("swap")
                self.instructions.append((i, j))
                print(self.instructions)
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
            if array[i] <= array[low]:
                print("i")
                i += 1
            if array[j] > array[low]:
                print("j")
                j -= 1
        self.instructions.append((low, i - 1))
        print("here")
        temp = array[i - 1]
        array[i - 1] = array[low]
        array[low] = temp
        return i - 1

    def step_through(self):
        print(self.instructions)
        #print(self.keypress)
        for (i, j) in self.instructions:
            if self.keypress() == "next" and self.instructions.index((i, j)) != len(self.instructions) - 1:
                self.swap(i, j)
            if self.keypress() == "previous" and self.instructions.index((i, j)) != 0:
                (iprev, jprev) = self.instructions(self.instructions.index((i, j)) - 1)
                self.swap(iprev, jprev)

    def keypress(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        return "next"
                    if event.key == pygame.K_LEFT:
                        return "previous"
                    if event.key == pygame.K_m:
                        pygame.quit()
        


run = True

# unsorted = [random.randint(0, 100) for i in range(10)]
unsorted = [4, 1, 5, 6, 2, 5, 3, 7, 8]
#print(unsorted)
animation = Animation(unsorted)
animation.draw_boxes(win)
#animation.bubble_sort()
animation.quick_sort(0, len(unsorted) - 1, unsorted)

'''
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                animation.keypress = "next"
            if event.key == pygame.K_LEFT:
                animation.keypress = "previous"
            if event.key == pygame.K_m:
                run = False
'''

    #animation.draw_boxes(win)

pygame.quit()