import pandas as pd
import numpy as np

anime = pd.read_csv('m29/anime.csv')

rating = pd.read_csv('m29/rating.csv')


anime_modified = anime.set_index('name')