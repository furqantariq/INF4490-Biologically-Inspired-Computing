from util import *
import random
import time

def hillclimbing(distances, nCities):

    #initializing with random permutation
    path = random.sample(range(0,nCities), nCities)
    min_d = tour_distance(path, distances)

    while True:
        min_d2 = min_d
        min_d, path = hillclimb(path, min_d, distances)
        if min_d2 == min_d:
            break

    return path + path[:1], min_d



def hillclimb(path, min_d, distances):
    neighbours = find_neighbours(path)
    for i in neighbours:
        d = tour_distance(i, distances)
        if min_d > d:
            min_d = d
            path = i
            break
    return min_d, path

def find_neighbours(perm):
    neighbours = []
    for i in range(len(perm)-1):
        n = perm[:]
        n[i], n[i+1] = n[i+1], n[i]
        neighbours.append(n)
    return neighbours


if __name__ == "__main__":

    #Parameters
    num_of_cities = 10

    cities, distances = read_input("european_cities.csv", num_of_cities)

    file = open("out.txt", "w")
    for x in range(20):
        start_time = time.time()
        path, dist = hillclimbing(distances, num_of_cities)
        time_taken = time.time()-start_time
        file.write("{0};{1};{2};{3};\n".format(x, [cities[x] for x in path], dist, time_taken ))
        print("%s Seconds " % time_taken)
        print("--Output--")
        print([cities[x] for x in path], dist)

    file.close()
