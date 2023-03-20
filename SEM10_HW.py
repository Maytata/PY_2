count=0
humans= []
robots = []
for i in data.values:
  if i == 'human':
    humans.append(1)
  else:
    humans.append(0)
  if i == 'robot':
    robots.append(1)
  else:
    robots.append(0)

summary={'human':humans, 'robot':robots}
data_dum=pd.DataFrame(summary)
data_dum
