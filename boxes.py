import pygame
import random

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
        self.space = 10
        self.box_size = int(min((self.width - self.space * (self.size + 1)) / self.size, 60))
        self.font = pygame.font.Font('freesansbold.ttf', int(self.box_size / 2))
        self.left_border = (self.width - ((self.box_size * self.size) + (self.size - 1) * self.space)) // 2
        self.top_border = (self.height - self.box_size) // 2
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

    def swap(self, index1, index2):
        if index1 == index2:
            return
        list_nums = self.list_nums

        dist = abs(index1 - index2) - 1
        num1 = self.list_nums[index1]
        num2 = self.list_nums[index2]
        if index1 < index2:
            rect1 = self.rect_positions[num1]
            rect2 = self.rect_positions[num2]
        else:
            rect1 = self.rect_positions[num2]
            rect2 = self.rect_positions[num1]


        step = 10
        dist_to_target = self.box_size * 1.5
        ori_y = rect1.y

        while (rect1.y <= ori_y + dist_to_target):
            rect1.y += step
            rect2.y -= step
            self.draw_boxes(win)
            pygame.time.delay(50)

        ori_x = rect1.x
        target_x1 = ((dist + 1) * (self.box_size) + (dist + 1) * (self.space))
        ori_x2 = rect2.x

        while (rect1.x < ori_x + target_x1 - step):
            rect1.x += step
            rect2.x -= step
            self.draw_boxes(win)
            pygame.time.delay(50)

        rect1.x = ori_x + target_x1
        rect2.x = ori_x2 - target_x1

        ori_y = rect1.y

        while (rect1.y >= ori_y - dist_to_target):
            rect1.y -= step
            rect2.y += step
            self.draw_boxes(win)
            pygame.time.delay(50)

        num1_idx = self.list_nums.index(num1)
        num2_idx = self.list_nums.index(num2)
        tmp = self.list_nums[num1_idx]
        self.list_nums[num1_idx] = self.list_nums[num2_idx]
        self.list_nums[num2_idx] = tmp

    def bubble_sort(self):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(self.list_nums[:-1])):
                if int(self.list_nums[i]) > int(self.list_nums[i+1]):
                    self.swap(i, i+1)
                    is_sorted = False
    #Would be easier to show quicksort with splitting function
    def quick_sort(self, low, high):
        if low < high:
            pivot = self.partition(low, high)
            self.quick_sort(low, pivot - 1)
            self.quick_sort(pivot + 1, high)
       
    def partition(self, low, high):
        i = low + 1
        j = high
        while j >= i:
            if self.list_nums[i] > self.list_nums[low] and self.list_nums[j] < self.list_nums[low]:
                self.swap(i, j)
            if self.list_nums[i] < self.list_nums[low]:
                i += 1
            if self.list_nums[j] > self.list_nums[low]:
                j -= 1
        self.swap(low, i - 1)
        return i - 1
        


run = True

inputlist = [4,8,2,6,3,9,1,5,7,0]#list(range(10, 0, -1))
animation = Animation(inputlist)
animation.draw_boxes(win)
#animation.bubble_sort()
animation.quick_sort(0, len(inputlist) - 1)


# while run:
#     pygame.time.delay(10)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#
#     animation.draw_boxes(win)
#
# pygame.quit()