class Monster:
    def __init__(self):
        self.hit_points = 10
        self.defense = 32

    def attack(self, direction):
        print('I am attacking from the ', direction)
        print('  => I have ', self.hit_points, 'HP')


class Spider(Monster):
    TYPES = ('Wolf', 'Black Widow', 'Tarantula')

    def __init__(self, spider_type):
        super(Spider, self).__init__()

        self.spider_type = spider_type
        if spider_type == 'Wolf':
            self.hit_points = 100
        else:
            self.hit_points = 80


class Rat(Monster):
    def __init__(self):
        self.hit_points = 35


spider = Spider('Wolf')
spider.attack('South')
spider.foo = 42
print("Spider's HP:", spider.hit_points)


rizzo = Rat()
print("Rizzo's HP:", rizzo.hit_points)


daddy_longs = {
    'hit_points':45,
}
daddy_longs['hit_points']
