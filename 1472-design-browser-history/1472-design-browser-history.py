class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.stack = [homepage]
        self.bac = []

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.stack.append(url)
        self.bac = []
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        steps = min(steps, len(self.stack)-1)
        while steps != 0:
            self.bac.append(self.stack.pop())
            steps-=1
        return self.stack[-1]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        steps = min(steps, len(self.bac))
        while steps != 0:
            self.stack.append(self.bac.pop())
            steps-=1
        return self.stack[-1]
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)