import numpy as np

class Bot:
    def __init__(self, env):
        self.env = env
        self.step = 0
        
        self.T_DROP = 60       
        self.T_PULL = 15       
        self.T_REST = 35       
        
        self.ACT_FETAL = [1.0, 1.0, 1.0, 1.0] 
        
        self.ACT_PULL_LEFT = [0.75, 0.0, 1.0, 1.0] 
        self.ACT_PULL_RIGHT = [0.0, 0.75, 1.0, 1.0] 
        
    def act(self):
        self.step += 1
        
        if self.step < self.T_DROP:
            return self.ACT_FETAL

        cycle_len = (self.T_PULL + self.T_REST) * 2
        t = (self.step - self.T_DROP) % cycle_len
        
        if t < self.T_PULL:
            return self.ACT_PULL_LEFT
            
        elif t < (self.T_PULL + self.T_REST):
            return self.ACT_FETAL
            
        elif t < (self.T_PULL + self.T_REST + self.T_PULL):
            return self.ACT_PULL_RIGHT
            
        else:
            return self.ACT_FETAL

    def observe(self, obs):
        pass