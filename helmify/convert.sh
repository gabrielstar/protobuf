awk 'FNR==1 && NR!=1  {print "---"}{print}' ./source/*.yaml | helmify mychart