import sys # for Command Line Arguments
from jeanCV import skinDetector


imageName = sys.argv[1]

detector = skinDetector("face1")
detector.find_skin()