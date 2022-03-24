import pygame
from dataclasses import dataclass
import sorting_algorithms as sa
import sys
from enum import Enum


@dataclass
class Number:
    num: int
    rect: pygame.Rect
    text: pygame.Surface


class Animation:
    def __init__(self, list_nums, win):
        self.win = win
        self.scale = 0
        self.instructions = []
        self.nums = []
        self.split_index = []
        self.size = len(list_nums)
        self.empty_spaces = 0
        self.width, self.height = 1300, 700
        self.space = 10
        self.box_size = int(min((self.width - self.space * (self.size + 1)) / self.size, 60))
        self.font = pygame.font.Font('freesansbold.ttf', int(self.box_size / 2))
        self.left_border = (self.width - ((self.box_size * self.size) + (self.size - 1) * self.space)) // 2
        self.top_border = (self.height - self.box_size) // 2
        self.fps = 60
        for i, n in enumerate(list_nums):
            rect = pygame.Rect(self.left_border + (self.box_size + self.space) * i, self.top_border, self.box_size, self.box_size)
            text = self.font.render(str(list_nums[i]), True, 'white')
            text_rect = text.get_rect()
            text_rect.center = (self.left_border + (self.box_size + self.space) * i + self.box_size // 2), (self.top_border + self.box_size // 2)
            self.nums.append(Number(n, rect, text))

    def new_resize(self):
        self.box_size = (self.width - ((self.size + 1) * self.space) - (self.empty_spaces + 2) * self.box_size) // self.size 
        self.left_border = int((self.width - ((self.size * self.box_size) + ((self.size - 1) * self.space) + (self.empty_spaces * self.box_size))) / 2)
        offset = 0
        for i, n in enumerate(self.nums):
            rect = pygame.Rect(self.left_border + offset + (self.box_size + self.space) * i, self.top_border, self.box_size, self.box_size)
            self.font = pygame.font.Font('freesansbold.ttf', int(self.box_size / 2))
            text = self.font.render(str(self.nums[i].num), True, 'white')
            text_rect = text.get_rect()
            text_rect.center = (self.left_border + (self.box_size + self.space) * i + self.box_size // 2), (self.top_border + self.box_size // 2)
            self.nums[i] = (Number(self.nums[i].num, rect, text))
            if i in self.split_index and i != self.split_index[-1]:
                offset += self.box_size

    
    def draw_boxes(self):
        self.win.fill((0, 0, 0))
        for i, n in enumerate(self.nums):
            rect = n.rect
            pygame.draw.rect(self.win, 'red', rect)
            text = n.text
            text_rect = text.get_rect()
            text_rect.center = rect.center
            self.win.blit(text, text_rect)
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
            self.draw_boxes()
            pygame.time.delay(50)

        ori_x = rect1.x
        target_x1 = rect2.x
        target_x2 = rect1.x
        ori_x2 = rect2.x

        while rect1.x < target_x1 - step:
            pygame.event.pump()
            rect1.x += step
            rect2.x -= step
            self.draw_boxes()
            pygame.time.delay(50)

        rect1.x = target_x1
        rect2.x = target_x2

        ori_y = rect1.y

        while rect1.y >= ori_y - dist_to_target:
            pygame.event.pump()
            rect1.y -= step
            rect2.y += step
            self.draw_boxes()
            pygame.time.delay(50)

        tmp = self.nums[index1]
        self.nums[index1] = self.nums[index2]
        self.nums[index2] = tmp

    def new_split(self, index1):
        if index1 == (self.size - 1):
            index2 = index1
        else:
            index2 = index1 + 1
        self.split_index.append(index1)
        self.empty_spaces += 1
        step = 5
        self.left_border = self.left_border - self.box_size // 2
        if self.nums[0].rect.x - self.box_size // 2 <= 0 or (self.nums[self.size - 1].rect.x + self.box_size) + self.box_size // 2 >= self.width:
            self.new_resize()
        ori_x = self.nums[index1].rect.x
        while self.nums[index1].rect.x > ori_x - self.box_size // 2:
            pygame.event.pump()
            for index in range (index1 + 1):
                self.nums[index].rect.x -= step
            self.draw_boxes()
            pygame.time.delay(50)

        ori_x2 = self.nums[index2].rect.x
        while self.nums[index2].rect.x < ori_x2 + self.box_size // 2:
            pygame.event.pump()
            for index in range (index2, self.size, 1):
                self.nums[index].rect.x += step
            self.draw_boxes()
            pygame.time.delay(50)


    def combine(self, index1):
        if index1 == (self.size - 1):
            index2 = index1
        else:
            index2 = index1 + 1
        self.empty_spaces -= 1
        self.split_index.remove(index1)
        step = 5
        self.left_border = self.left_border + self.box_size // 2
        ori_x = self.nums[index1].rect.x
        while self.nums[index1].rect.x < ori_x + self.box_size // 2:
            pygame.event.pump()
            for index in range (index1 + 1):
                self.nums[index].rect.x += step
            self.draw_boxes()
            pygame.time.delay(50)


        ori_x2 = self.nums[index2].rect.x
        while self.nums[index2].rect.x > ori_x2 - self.box_size // 2:
            pygame.event.pump()
            for index in range (index2, self.size, 1):
                self.nums[index].rect.x -= step
            self.draw_boxes()
            pygame.time.delay(50)

    def bubble_sort(self, array):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(array[:-1])):
                if array[i] > array[i+1]:
                    self.instructions.append(("swap", i, i + 1))
                    self.switch(i, i + 1, array)
                    is_sorted = False

    def selection_sort(self, array):
        size = len(array)
        for step in range(size):
            min_index = step

            for i in range(step + 1, size):
                if array[i] < array[min_index]:
                    min_index = i
            
            self.instructions.append(("swap", step, min_index))
            self.switch(step, min_index, array)

    def insertion_sort(self, array):
        size = len(array)
        for index in range(1, size):
            current_value = array[index]
            current_position = index

            while current_position > 0 and array[current_position - 1] > current_value:                
                self.instructions.append(("swap", current_position, current_position - 1))
                self.switch(current_position, current_position - 1, array)
                current_position -= 1
                
            array[current_position] = current_value

    def quick_sort(self, low, high, array):
        if low < high:
            pivot = self.partition(low, high, array)
            if pivot != 0:
                self.instructions.append(("split", pivot - 1, 0))
            self.instructions.append(("split", pivot, 0))
            self.quick_sort(low, pivot - 1, array)
            self.quick_sort(pivot + 1, high, array)
    
    def partition(self, low, high, array):
        i = low + 1
        j = high
        while j >= i:
            if array[i] > array[low] and array[j] <= array[low]:
                self.instructions.append(("swap", i, j))
                self.switch(i, j, array)
            elif array[i] < array[low]:
                i += 1
            elif array[j] > array[low]:
                j -= 1
        if array[low] != array[i - 1]:
            self.instructions.append(("swap", low, i - 1))
            self.switch(low, i - 1, array)
        return i - 1

    def translate(self, nums, x, y, time):
        steps = int(self.fps * time / 1000)
        original_rects = [num.rect.copy() for num in nums]
        for i in range(1, steps + 1):
            new_x = i / steps * x
            new_y = i / steps * y
            for i, num in enumerate(nums):
                num.rect.topleft = (new_x + original_rects[i].x, new_y + original_rects[i].y)
            yield False

    def translate_absolute(self, num, x, y, time):
        original_pos = num.rect.copy()
        yield from self.translate([num], x - original_pos.x, y - original_pos.y, time)

    def merge(self, arr, a, b):
        a_idx = 0
        b_idx = 0
        leftmost = a[0].rect.left
        top = a[0].rect.top + self.space + self.box_size
        for i in range(len(a) + len(b)):
            if a_idx >= len(a):
                arr[i] = b[b_idx]
                b_idx += 1
            elif b_idx >= len(b):
                arr[i] = a[a_idx]
                a_idx += 1
            elif a[a_idx].num <= b[b_idx].num:
                arr[i] = a[a_idx]
                a_idx += 1
            else:
                arr[i] = b[b_idx]
                b_idx += 1
            yield from self.translate_absolute(arr[i], leftmost + (self.space + self.box_size) * i, top, 250)

    def merge_sort(self, arr=None):
        if arr is None:
            yield True
            arr = self.nums
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        yield from self.translate(arr, 0, -self.space - self.box_size, 250)
        yield True
        yield from self.merge_sort(left)
        yield from self.merge_sort(right)
        yield from self.merge(arr, left, right)
        yield True

    def heapifyFun(self, array, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and array[i] < array[left]:
            largest = left
        if right < n and array[largest] < array[right]:
            largest = right
        if largest != i:
            self.instructions.append(("swap", i, largest))
            self.switch(i, largest, array)
            self.heapifyFun(array, n, largest)
    
    def heap_sort(self, array):

        # If the user input a sorted array, just return
        # No need to do the swap animation
        if array == sorted(array):
            return

        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            self.heapifyFun(array, n, i)
        for i in range(n - 1, 0, -1):
            self.instructions.append(("swap", i, 0))
            self.switch(i, 0, array)
            self.heapifyFun(array, i, 0)

    def switch(self, i, j, array):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

    def step_through(self):
        self.instructions.append(("swap", 0, 0))
        x = 0
        while True:
            (l, i, j) = self.instructions[x]
            key = self.keypress()
            if key == "next" and x != len(self.instructions):
                if l == "swap":
                    self.swap(i, j)
                if l == "split":
                    self.new_split(i)
                if x < len(self.instructions) - 1:
                    x += 1
            if key == "previous" and x != 0:
                (lprev, iprev, jprev) = self.instructions[x - 1]
                if lprev == "swap":
                    self.swap(iprev, jprev)
                if lprev == "split":
                    self.combine(iprev)
                x -= 1

    def step_through_merge_sort(self):
        run = True
        clock = pygame.time.Clock()
        merge_sort = self.merge_sort()
        signal = None
        while True:
            try:
                signal = next(merge_sort)
            except StopIteration:
                pass
            if signal:
                self.keypress()
                continue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            if not run:
                break
            self.draw_boxes()
            clock.tick(self.fps)
    
    def keypress(self):
        while True:
            self.information_box()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sa.main()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.information_box()
                        return "next"
                    if event.key == pygame.K_LEFT:
                        self.information_box()
                        return "previous"
                    if event.key == pygame.K_m:
                        pygame.display.quit()
                        sa.main()
                        sys.exit()

    def information_box(self):
        # Create A Box
        width = 1300
        height = 700
        x = width - 250
        y = height - 675
        pygame.draw.rect(self.win, "white", (x,y,200,80))
 
        # Font Setup
        font = pygame.font.SysFont("Verdana", 15)
 
        # Menu Info
        menu_info = "M - Go to the main menu"
        menu = font.render(menu_info, True, "red")
        menu_rect = menu.get_rect(center=(x + 100, y + 20))
        self.win.blit(menu, menu_rect)
 
        # Left Key Info
        left_info = "Left Key - Previous Step"
        left = font.render(left_info, True, "red")
        left_rect = left.get_rect(center=(x + 95, y + 40))
        self.win.blit(left, left_rect)
 
        # Right Key Info
        rigth_info = "Right Key - Next Step"
        right = font.render(rigth_info, True, "red")
        right_rect = right.get_rect(center=(x + 85, y + 60))
        self.win.blit(right, right_rect)
 
        pygame.display.update()