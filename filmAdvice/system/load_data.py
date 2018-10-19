import csv
import os
from filmAdvice.movie.models import Movie


def load_movie_data():
    current_pat = os.getcwd()
    with open(current_pat + '/filmAdvice/system/movies.dat', encoding='utf-8') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title::Genres'.split('::'), delimiter='\t')

    for row in reader:
        print(row)
        # m = Movie(title=row['Title'], genre=row['Genres'])
        # m.save()
    return reader
