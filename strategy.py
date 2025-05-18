class Strategy:
    def __init__(self):
        self.rsi_l, self.rsi_u = 30, 70
        self.rsi_period = 14
        self.sma_period = 50
        self.atr_period = 14

    def set_RSI(self, lower: int, upper: int, period: int):
        self.rsi_l = lower
        self.rsi_u = upper
        self.rsi_period = period

    def set_SMA(self, period: int):
        self.sma_period = period

    def set_ATR(self, period: int):
        self.atr_period = period

    def show_strategy(self):
        return f'''
        RSI bounds: {self.rsi_l}, {self.rsi_u}
        RSI period: {self.rsi_period}
        SMA period: {self.sma_period}
        ATR period: {self.atr_period}
        '''
    
if __name__ == '__main__':
    print('\nDefault strategy:')
    s = Strategy()
    print(s.show_strategy())