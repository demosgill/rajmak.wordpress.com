__author__ = 'raj'

import sys
import random
from vector import Vector
from cluster import Cluster
from utils import euclidean_distance


class KMeans:
    def __init__(self, k):
        self.k = k
        self.iterations = 0
        self.max_iterations = 100
        self.vectors = list()
        self.initial_vectors = list()
        self.clusters = list()

    def progress(self):
        self.iterations += 1
        print self.iterations

    def add_vector(self, vid, vector_array):
        self.vectors.append(Vector(vid, vector_array))

    def initialize(self):
        self.initial_vectors = random.sample(self.vectors, self.k)
        self.clusters = [Cluster(cid, vector) for cid, vector in enumerate(self.initial_vectors)]

    def run(self):
        while self.iterations <= self.max_iterations:
            self.progress()
            for vector in self.vectors:
                smallest_distance = 0
                belongs_to = 0
                for cid, cluster in enumerate(self.clusters):
                    distance = euclidean_distance(vector.co_ords, cluster.centroid)
                    if cid == 0:
                        smallest_distance = distance
                        belongs_to = cid
                    if distance < smallest_distance:
                        belongs_to = cid
                        smallest_distance = distance
                self.clusters[belongs_to].add_vector_to_cluster(vector)
        return self.clusters


if __name__ == "__main__":
    titles = open("sample_input.txt").readlines()
    kmeans = KMeans(20)

    for _vid, _vector_array in enumerate(sys.stdin):
        kmeans.add_vector(_vid, eval(_vector_array))
    kmeans.initialize()

    for _cluster in kmeans.run():
        for v in _cluster.vectors:
            print titles[v.vid].strip()
        print "-" * 10