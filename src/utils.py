import os

class Simulation():
    def __init__(self=None, 
                 time=None, 
                 n_intersections=None, 
                 n_streets=None,
                 n_cars=None,
                 reward=None):
        pass

    def print_ready_streets(self, list_streets):
        for street in list_streets:
            print(f'{street.name}: {street.line}')

    def read_header(self, filepath):
        f = open(f'{filepath}/header.in', "r")
        _ = f.readline().split()
        self.time = int(_[0])
        self.n_intersections = int(_[1])
        self.n_streets = int(_[2])
        self.n_cars = int(_[3])
        self.reward = int(_[4])
        print(self.time)
        return self    

    def read_all_streets(self, filepath):
        streets_dict = dict()
        f = open(f'{filepath}/streets.in', "r")
        for i,line in enumerate(f):
            _ = line.split()
            streets_dict[i] = Street(
            name = _[2],
            length = _[3],
            int_from = _[0],
            int_to = _[1]
            )
        return streets_dict

    def read_all_cars(self, filepath):
        cars_dict = dict()
        f = open(f'{filepath}/cars.in', "r")
        for i,line in enumerate(f):
            _ = line.split()
            cars_dict[i] = Car(
            name = i+1,
            path = _[1:] 
            )
        return cars_dict


class Street():
    def __init__(self, name, length, int_from, int_to):
        self.name = name
        self.length = int(length)
        self.int_from = int_from
        self.int_to = int_to
        self.line = [0 for i in range(self.length)]  

    def get_street_ready(self, cars_dict):
        for i in range(len(cars_dict)): 
            if cars_dict[i].start_pos == self.name:
                for j in range(self.length-1, -1, -1):
                    if self.line[j] != 0:
                        pass
                    else:
                        self.line[j] = cars_dict[i].name
                        break
        return self

class Car():
    def __init__(self,name=None, path=None):
        self.name = name
        self.start_pos = path[0] 
        self.path = path
        self.end_pos = path[-1] 


class TrafficLight():
    def __init__(self,name, time, actual_street, next_streets):
        self.name = name
        self.time = time
        self.actual_street = actual_street
        self.next_streets = next_streets


if __name__ == "__main__":
    sim = Simulation()
    sim.read_header(os.path.join(os.path.realpath('..'), 'data/test'))
    streets_dict =  sim.read_all_streets(os.path.join(os.path.realpath('..'), 'data/test'))
    cars_dict =  sim.read_all_cars(os.path.join(os.path.realpath('..'), 'data/test'))
    print(sim.time)
    print(streets_dict[4].name)
    print(streets_dict[2].length)
    print(streets_dict[1].int_to)
    print(streets_dict[4].get_street_ready(cars_dict).line)
    print(streets_dict[2].get_street_ready(cars_dict).line)
    print(streets_dict[0].get_street_ready(cars_dict).line)
    print(cars_dict[0].path)
    print(cars_dict[1].path)
    print(cars_dict[1].end_pos)
