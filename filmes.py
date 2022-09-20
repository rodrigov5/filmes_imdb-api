import csv, imdb

ia = imdb.IMDb()


codes = [20880628, 10872600, 3501632, 9419884, 7131622]
colums = ['imdbID', 'title', 'year', 'genres', 'kind']

movies = []
for i in codes:
    aux = []
    code = f'{i}'
    series = ia.get_movie(code)
    for j in range(len(codes)):
        aux.append(series.data[colums[j]])
    movies.append(aux)

for i in movies:
    print(i)

with open('PlanilhaFilmes.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(colums)
    write.writerows(movies)

