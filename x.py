def o1_1(*args):
    s="""3 2
3 3 4 5 6 7 8 9 3 3 3
6 3 7 5 6 8 8 9 1 2 1"""
    l = s.split("\n")
    for i in l[:-1]:
        yield(i+"\n")
    yield(l[-1])
class o1_2:
    s="""3 2
3 3 4 5 6 7 8 9 3 3 3
6 3 7 5 6 8 8 9 1 2 1"""
    fn=""
    def __init__(self, *args):
        self.fn = args[0]
        return None
    def read(self):
        return self.s
    def write(self, *args):
        print(self.fn + " <= ", *args)
    def close(self):
        return None
    def readlines(self):
        l = self.s.split("\n")
        for i in l[:-1]:
            yield(i+"\n")
        yield(l[-1])
f = o1_2("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
