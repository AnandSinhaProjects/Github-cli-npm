import requests
import click

@click.group()

def cli():
    pass

@cli.command()
@click.argument('username')
def user(useername):
    r = requests.get('https://api.github.com/users/{}'.format(username)).json()
    name = r['name']
    repos = r['public_repos']
    bio = r['bio']
    # print(f'Name: {name}, Repos: {repos}, Bio: {bio}')
    print('Name: {}, Repos: {}, Bio: {}'.format(name, repos, bio))


@cli.command()
@click.argument('username')
def repos(username):
    r = requests.get('https://api.github.com/users/{}/repos'.format(username)).json()
    for i in range(len(r)):
        print(r[i]['name'])


def calculate_percentage(langs, lang, total_bytes):
    result = langs[lang] * 100 / total_bytes
    return round(result, 2)


def convert_to_percentage(langs):
    total_bytes = sum(langs.values())
    return {lang: calculate_percentage(langs, lang, total_bytes) for (lang, v) in langs.items()}


@cli.command()
@click.argument('username')
@click.argument('reponame')
def languages(username, reponame):
    r = requests.get('https://api.github.com/repos/{}/{}/languages'.format(username, reponame)).json()
    change_r = convert_to_percentage(r)
    for key, value in change_r.items():
        print('{}: {}%'.format(key, value))