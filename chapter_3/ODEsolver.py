class RK4:
    def __init__(self, func1, func2, x0, v0, t0, w0, h) -> None:
        self.func1 = func1
        self.func2 = func2
        self.x = [x0]
        self.v = [v0]
        self.t = [t0]
        self.w0 = w0
        self.xCurr = x0
        self.vCurr = v0
        self.tCurr = t0
        self.h = h
    def nextStep(self):
        k11 = self.h*self.func1(self.xCurr, self.vCurr, self.tCurr)
        k21 = self.h*self.func2(self.xCurr, self.vCurr, self.tCurr, self.w0)
        k12 = self.h*self.func1(self.xCurr+k11/2, self.vCurr+k21/2, self.tCurr+self.h/2)
        k22 = self.h*self.func2(self.xCurr+k11/2, self.vCurr+k21/2, self.tCurr+self.h/2, self.w0)
        k13 = self.h*self.func1(self.xCurr+k12/2, self.vCurr+k22/2, self.tCurr+self.h/2)
        k23 = self.h*self.func2(self.xCurr+k12/2, self.vCurr+k22/2, self.tCurr+self.h/2, self.w0)
        k14 = self.h*self.func1(self.xCurr+k13, self.vCurr+k23, self.tCurr+self.h)
        k24 = self.h*self.func2(self.xCurr+k13, self.vCurr+k23, self.tCurr+self.h, self.w0)
  
        self.xCurr += (k11+2*k12+2*k13+k14)/6
        self.vCurr += (k21+2*k22+2*k23+k24)/6
        self.tCurr += self.h

        self.x.append(self.xCurr)
        self.v.append(self.vCurr)
        self.t.append(self.tCurr)
    def solve(self, N):
        for i in range(N):
            self.nextStep()
    def get(self):
        return self.x,self.v,self.t