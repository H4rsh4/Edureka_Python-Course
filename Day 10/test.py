import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

raw = cv2.imread('dogs.jpeg', -1)
type(raw)
cv2.imshow('bin', raw)