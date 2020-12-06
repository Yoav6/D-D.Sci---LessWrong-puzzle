# an answer to this post
# https://www.lesswrong.com/posts/HsxT2cpPWYzTg9tpY/d-and-d-sci

import csv

my_stats = {'cha': 4, 'str': 6, 'con': 14, 'dex': 13, 'int': 13, 'wis': 13}
score = {'cha': 0, 'str': 0, 'con': 0, 'dex': 0, 'int': 0, 'wis': 0}

print(max(my_stats))


with open('D&D_sci.csv', 'r') as f:
    rows = list(csv.reader(f))

    for row in rows[1:]:
        for index, number in enumerate(row[:-1]):
            row[index] = int(number)
    for i in range(10):
        for row in rows:
            if row[-1] == 'succeed':
                if row[1] < my_stats['cha']:
                    score['cha'] -= 1
                elif row[1] > my_stats['cha']:
                    score['cha'] += 1

                if row[1] < my_stats['str']:
                    score['str'] -= 1
                elif row[1] > my_stats['str']:
                    score['str'] += 1

                if row[1] < my_stats['con']:
                    score['con'] -= 1
                elif row[1] > my_stats['con']:
                    score['con'] += 1

                if row[1] < my_stats['dex']:
                    score['dex'] -= 1
                elif row[1] > my_stats['dex']:
                    score['dex'] += 1

                if row[1] < my_stats['int']:
                    score['int'] -= 1
                elif row[1] > my_stats['int']:
                    score['int'] += 1

                if row[1] < my_stats['wis']:
                    score['wis'] -= 1
                elif row[1] > my_stats['wis']:
                    score['wis'] += 1
            elif row[-1] == 'fail':
                if row[1] > my_stats['cha']:
                    score['cha'] -= 1
                elif row[1] < my_stats['cha']:
                    score['cha'] += 1

                if row[1] > my_stats['str']:
                    score['str'] -= 1
                elif row[1] < my_stats['str']:
                    score['str'] += 1

                if row[1] > my_stats['con']:
                    score['con'] -= 1
                elif row[1] < my_stats['con']:
                    score['con'] += 1

                if row[1] > my_stats['dex']:
                    score['dex'] -= 1
                elif row[1] < my_stats['dex']:
                    score['dex'] += 1

                if row[1] > my_stats['int']:
                    score['int'] -= 1
                elif row[1] < my_stats['int']:
                    score['int'] += 1

                if row[1] > my_stats['wis']:
                    score['wis'] -= 1
                elif row[1] < my_stats['wis']:
                    score['wis'] += 1
        print(score)
        my_stats[max(score, key=score.get)] += 1
        print(my_stats)
        score = {'cha': 0, 'str': 0, 'con': 0, 'dex': 0, 'int': 0, 'wis': 0}

print(f'\nThe final stats are\n{my_stats}')





