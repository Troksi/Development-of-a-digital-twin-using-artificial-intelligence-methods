import time


class PauseForLimit:
    def __init__(self, limit, pause_time=20):
        self.count = 0
        self.pause_time = pause_time
        self.limit = limit

    def reg_stap(self):
        if self.count % self.limit == 0:
            time.sleep(self.pause_time)
        self.count += 1

# # Пример использования:
# function_caller = PauseForLimit(3,5)

# for i in range(10):
#     print(i)
#     function_caller.reg_stap()

# function_caller = PauseForLimit(3,5)

# dict_t={}
# for i in range(10):
#     dict_t[i]=i*10

# for i,el in enumerate(dict_t.values()):
#     function_caller.reg_stap()
#     print(i,el)
# print(dict_t)