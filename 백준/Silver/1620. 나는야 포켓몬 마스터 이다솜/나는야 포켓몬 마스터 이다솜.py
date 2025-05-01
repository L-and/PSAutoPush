import sys

n, m = map(int, sys.stdin.readline().strip().split())

pokemonList = list()
sortedPokemonList = list()

for i in range(n): # 포켓몬들을 입력받음
    pokemonList.append(sys.stdin.readline().strip())
pokemonDict = {}

for i, v in enumerate(pokemonList):
    pokemonDict[v] = i


targetPokemonList = list()
for i in range(m): # 문제들을 입력받음
    targetPokemonList.append(sys.stdin.readline().strip())

for i in range(m): # 정답 출력
    if targetPokemonList[i].isdigit():
        print(pokemonList[int(targetPokemonList[i]) - 1])
    else:
        print(pokemonDict[targetPokemonList[i]] + 1)


