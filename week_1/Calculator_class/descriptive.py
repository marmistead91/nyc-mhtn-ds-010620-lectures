import math
from math import sqrt

class Calculator:
    data = []
    def __init__(self, data):
        self.data = data 
        self.length = len(data)
        self.mean = self.calc_mean()
        self.median = self.med()
        self.variance = self.vari()
        self.stand_dev = self.calc_std()
    
    def add_data(self, added_data):
        if type(added_data) == list:
            self.data.extend(added_data)
        else: 
            self.data.append(added_data)
        self.__init__(self.data)

        
    def remove_data(self, removed_data):
        if type(removed_data) == list:
            for i in removed_data:
                self.data.remove(i)
        else:
            self.data.remove(removed_data)
        self.__init__(self.data)
    
    def calc_mean(self):
        avg = sum(self.data)/self.length
        self.mean = avg
        return avg

    def med(self):
        n = len(self.data) 
        self.data.sort() 
        if n % 2 == 0: 
            median1 = self.data[n//2] 
            median2 = self.data[n//2 - 1] 
            median = (median1 + median2)/2
        else: 
            median = self.data[n//2]
        self.median = median
        return median

    def vari(self):
        minus_avg_squared = []
        for i in self.data:
            x = (i - self.mean) ** 2
            minus_avg_squared.append(x)
        vari_final = (sum(minus_avg_squared))/(self.length - 1)
        self.variance = vari_final
        return vari_final

    def calc_std(self):
        vari = self.variance
        stand_devi = sqrt(vari)
        self.stand_dev = stand_devi
        return stand_devi
