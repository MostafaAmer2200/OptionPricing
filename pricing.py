from math import log, exp, sqrt, pi
from scipy.stats import norm


class Opricing:
    def __init__(self, S, K, T, r, sigma):
        """
        S: Spot price of underlying asset
        K: Strike Price
        T: Time to maturity 
        r: Risk free rate
        sigma: volatility of the asset`

        This class will be responsible for` pricing
        put and call options
        """
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma

    def _d1(self):
        """
        D1: Part of black scholes equation
        """
        return (log(self.S / self.K) + (self.r + self.sigma**2 / 2)*self.T) / self.sigma * sqrt(self.T)
    def _d2(self):
        """
        D2: Part of black scholes equation
        """
        return self._d1() - self.sigma * sqrt(self.T)
    def get_call(self):
        """
        Gets call option price
        """
        return self.S * norm.cdf(self._d1()) - self.K * exp(-self.r*self.T) * norm.cdf(self._d2())
    def get_put(self):
        """
        Gets put option price
        """
        return self.K*exp(-self.r*self.T)-self.S+self.get_call()


    
if __name__ == "__main__":

    S_0 = float(input("Enter Spot Price S(0): "))
    K = float(input("Enter Strike Price K: "))
    T = float(input("Enter time T: "))
    r = float(input("Enter interest rate r: "))
    sigma = float(input("Enter standard deviation sigma: "))

    price_call = Opricing(S_0, K, T, r , sigma).get_call()
    price_put = Opricing(S_0, K, T, r , sigma).get_put()
    print(f"Option Call Price: {price_call}")
    print(f"Option Put Price: {price_put}")


    
    
