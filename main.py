import random

class Schedule:
    def __init__(self):
        self.num_of_lessons = 0
        self.name_for_lessons = {}
        self.basic_rus_9_lessons = {'Math':6, 
                              'Physics':4, 
                              'Chemistry':3,
                              'Biology':3,
                              'English':5,
                              'Russian':3,
                              'Kazakh language':4,}
        self.profile_rus_9_lessons = {
                              'Geography':2,
                              'History':1,
                              'IT':2,
                              'History of Kazakhstan':2,
                              'Law':1,
                              'Literature':2}
        self.dop_rus_9_lessons = {
                              'Dombyra':1,
                              'PE':2,
                              'Art':2
                                }
        self.lessons_daily = set()
        self.Monday = []
        self.Tuesday = []
        self.Wednesday = []
        self.Thursday = []
        self.Friday = []
        self.method = ['basic', 'profile', 'dop']
        self.current_method = 'basic'
        self.used_methods = []
        self.shuffled = []
        self.week = [self.Monday, self.Tuesday, self.Wednesday, self.Thursday, self.Friday]
        self.num_of_day = 0
    def first_pair(self, num_of_day):
        self.current_method = random.choice(self.method)
        self.used_methods.append(self.current_method)
        if self.current_method == 'basic':
            return self.basic(num_of_day)
        elif self.current_method == 'profile':
            return self.profile(num_of_day)
        elif self.current_method == 'dop':
            return self.dop(num_of_day)
    def second_pair(self,num_of_day):
        while self.current_method in self.used_methods:
            self.current_method = random.choice(self.method)
        if self.current_method == 'basic':
            return self.basic(num_of_day)
        elif self.current_method == 'profile':
            return self.profile(num_of_day)
        elif self.current_method == 'dop':
            return self.dop(num_of_day)
    def third_pair(self,num_of_day):
        while self.current_method in self.used_methods:
            self.current_method = random.choice(self.method)
        if self.current_method == 'basic':
            return self.basic(num_of_day)
        elif self.current_method == 'profile':
            return self.profile(num_of_day)
        elif self.current_method == 'dop':
            return self.dop(num_of_day)
    def fourth_pair(self,num_of_day):
        self.current_method = random.choice(self.method)
        if self.current_method == 'basic':
            return self.basic(num_of_day)
        elif self.current_method == 'profile':
            return self.profile(num_of_day)
        elif self.current_method == 'dop':
            return self.dop(num_of_day)
    def make_schedule_day(self, num_of_day):
        self.first_pair(num_of_day)
        self.second_pair(num_of_day)
        self.third_pair(num_of_day)
        self.fourth_pair(num_of_day)
        self.day = {
            'first pair:':self.first_pair(num_of_day),
            'second pair:':self.second_pair(num_of_day),
            'third pair:':self.third_pair(num_of_day),
            'fourth pair:':self.fourth_pair(num_of_day)
        }
        return self.day
    def make_schedule_week(self):
        self.week = [self.make_schedule_day(0), self.make_schedule_day(1), self.make_schedule_day(2), self.make_schedule_day(3), self.make_schedule_day(4)]
        return self.week
    def basic(self, num_of_day):
        self.basicc = list(self.basic_rus_9_lessons.keys())
        self.shuffled = random.shuffle(self.basicc)
        self.Monday.append(self.basicc[0])
        self.Tuesday.append(self.basicc[1])
        self.Wednesday.append(self.basicc[2])
        self.Thursday.append(self.basicc[3])
        self.Friday.append(self.basicc[4])
        return self.week[num_of_day]
    def profile(self, num_of_day):
        self.cprofile = list(self.profile_rus_9_lessons.keys())
        self.shuffled = random.shuffle(self.cprofile)
        self.Monday.append(self.cprofile[0])
        self.Tuesday.append(self.cprofile[1])
        self.Wednesday.append(self.cprofile[2])
        self.Thursday.append(self.cprofile[3])
        self.Friday.append(self.cprofile[4])
        return self.week[num_of_day]
    def dop(self, num_of_day):
        self.dops = list(self.dop_rus_9_lessons.keys())
        self.shuffled = random.shuffle(self.dops)
        self.Monday.append(self.dops[0])
        self.Tuesday.append(self.dops[1])
        self.Wednesday.append(self.dops[2])
        return self.week[num_of_day]
something = Schedule()
print(something.make_schedule_week())
