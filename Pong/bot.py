from envpong import PongLogic
import random

# Random bot
class BotRight:
    def __init__(self, env):
        self.env = env
        
        # This bot doesn't require an initial observation
        self.obs = None
    
    def act(self):
        action = random.choice([PongLogic.PaddleMove.DOWN, PongLogic.PaddleMove.STILL, PongLogic.PaddleMove.UP])  
        return action
    
    def observe(self, obs):
        self.obs = obs
        
        
# Ball tracking bot
class BotLeft:
    def __init__(self, env):
        self.env = env
        self.obs = [0]*len(env.observation_space.sample())
        self.target_y = 0.5 
    
    def predict_impact(self, ball_x, ball_y, ball_vx, ball_vy, paddle_x):
        if ball_vx >= 0:
            return 0.5

        if abs(ball_vx) < 0.00001: return 0.5
        
        time_to_reach = (paddle_x - ball_x) / ball_vx
    
        impact_y = ball_y + (ball_vy * time_to_reach)
        
        while impact_y < 0 or impact_y > 1:
            if impact_y < 0:
                impact_y = -impact_y
            if impact_y > 1:
                impact_y = 2 - impact_y
                
        return impact_y

    def act(self):
        p1_y = self.obs[1]      
        p1_x = self.obs[0]      
        ball_x = self.obs[8]    
        ball_y = self.obs[9]    
        ball_vx = self.obs[10]  
        ball_vy = self.obs[11]  

        impact_y = self.predict_impact(ball_x, ball_y, ball_vx, ball_vy, p1_x)
        
        offset = 0.03 

        if ball_vy > 0:
            self.target_y = impact_y - offset
        else:
            self.target_y = impact_y + offset

        self.target_y = max(0, min(1, self.target_y))
        
        threshold = 0.01 
        
        if p1_y < self.target_y - threshold:
            return PongLogic.PaddleMove.UP
        elif p1_y > self.target_y + threshold:
            return PongLogic.PaddleMove.DOWN
        else:
            return PongLogic.PaddleMove.STILL
    
    def observe(self, obs):
        self.obs = obs