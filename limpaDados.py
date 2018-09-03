import json

with open("alunos.json", "r") as read_file:
    data = json.load(read_file)

pages = []
pages_brute_data = []
brute_data_fragments = []

for x in range(len(data)):
  pages.append(data[x])

for x in range(len(pages)):
  page = pages[x]
  brute_data = page['data']
  pages_brute_data.append(brute_data)

for x in range(len(pages_brute_data)):
  brute_data = pages_brute_data[x]
  for y in range(len(brute_data)):
    brute_data_fragments.append(brute_data[y])

