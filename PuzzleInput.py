from urllib import request


class ReadInput:
    data = ""

    def __init__(self, day):
        try:
            f = open(f"input/day{day}.txt")
            self.data = f.read().split("\n")
            f.close()
        except FileNotFoundError:
            link = "https://adventofcode.com/2021/day/%s/input" % day
            req = request.Request(link)
            req.add_header('Cookie', 'session=53616c7465645f5ff0e30cdabfc35a14068d564c8509509df88578c940c697709502bddebd4c3d5ec2952613cd8e0567')
            f = request.urlopen(req)
            self.data = f.read().decode('utf-8').split("\n")
            f.close()
            f = open(f"input/day{day}.txt", "w+")
            for line in self.data:
                f.write("%s\n" % line)
            f.close()
