from countminsketch import CountMinSketch

if __name__ == '__main__':
    cm = CountMinSketch(m = 16, d=4)
    cm.add("hello")
    cm.add("hello")
    cm.add("hello")
    cm.add("hello")
    cm.add("test")
    cm.add("test")
    cm.add("test")
    cm.add("test")
    print(cm.query("hello"))
    print(cm.tables)