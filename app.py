import requests
import sys


def get_players():
    response = requests.get('https://mach-eight.uc.r.appspot.com/')
    return response.json()['values']


if __name__ == '__main__':
    user_input = int(sys.argv[1])
    counter = 0
    players = get_players()
    results = []
    for i in players:
        for a in players:
            full_name_a = a['first_name'] + ' ' + a['last_name']
            full_name_i = i['first_name'] + ' ' + i['last_name']
            full_word = full_name_a + ' ' + full_name_i
            if full_name_a == full_name_i:
                continue
            else:
                result = ' '.join(sorted(full_word.split()))
                if result in results:
                    continue
                summation = int(i['h_in']) + int(a['h_in'])
                if summation == user_input:
                    results.append(' '.join(sorted(full_word.split())))
                    print(full_name_a + ' ' + full_name_i)
                    counter += 1
                else:
                    continue
    if counter == 0:
        print('No matches found')
