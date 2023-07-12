array = [
  {'database':82, 'network': 90, 'security': 80},
  {'database':60, 'network': 86, 'security': 70},
  {'database':70, 'network': 90, 'security': 50},
  {'database':80, 'network': 80, 'security': 90},
]

high_score_count = 0

for x in array:
  for y in x.values():
    if y > 80:
      high_score_count += 1

print(high_score_count)