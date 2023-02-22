
class bow_tie:
    def __init__(self,a,b,d,theta,t,freq,plasma_freq,damping_f):
        self.a = a
        self.b = b
        self.d = d
        self.theta = theta
        self.thicness = t
        self.eps_re = 1 - plasma_freq ** 2 / (freq ** 2 + damping_f ** 2)
        self.eps_im = plasma_freq**2 * damping_f**2 / (freq*(plasma_freq**2 + damping_f**2))
        self.eps = complex(self.eps_re,self.eps_im)