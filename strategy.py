class Strategy:
    def __init__(self):
        self.rsi_l, self.rsi_u = 30, 70
        self.rsi_interval = 14
        self.sma_slow_interval = 24
        self.sma_fast_interval = 10
        self.atr_interval = 14

    def set_rsi(self, lower: int, upper: int, interval: int):
        self.rsi_l = lower
        self.rsi_u = upper
        self.rsi_interval = interval

    def set_sma(self, slow_interval: int, fast_interval: int):
        self.sma_slow_interval = slow_interval
        self.sma_fast_interval = fast_interval

    def set_atr(self, interval: int):
        self.atr_interval = interval

    def show_strategy(self):
        return f'''
        RSI bounds: {self.rsi_l}, {self.rsi_u}
        RSI interval: {self.rsi_interval}
        SMA interval (slow): {self.sma_slow_interval}
        SMA interval (fast): {self.sma_fast_interval}
        ATR interval: {self.atr_interval}
        '''
    
if __name__ == '__main__':
    print('\nDefault strategy:')
    s = Strategy()
    print(s.show_strategy())