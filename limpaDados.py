import json

with open("alunos.json", "r") as read_file:
    data = json.load(read_file)

pages = []
pages_brute_data = []
brute_data_fragments = []
fragment_pieces = []
students = []

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

for x in range(len(brute_data_fragments)):
  fragment = brute_data_fragments[x]
  for y in range(len(fragment)):
    fragment_pieces.append(fragment[y])

for x in range(len(fragment_pieces)):
  piece = fragment_pieces[x]
  if(len(piece['text']) > 16):
    students.append(piece['text'])

print(students)
print(len(students))

