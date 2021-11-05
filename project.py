import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

mathlist = df["math score"].tolist()
readlist= df["reading score"].tolist()
writelist = df["writing score"].tolist()

mathmean = statistics.mean(mathlist)
mathmedian = statistics.median(mathlist)
mathmode = statistics.mode(mathlist)

readmean = statistics.mean(readlist)
readmedian = statistics.median(readlist)
readmode = statistics.mode(readlist)

writemean = statistics.mean(writelist)
writemedian = statistics.median(writelist)
writemode = statistics.mode(writelist)

print("\n")

print(" Mean, Median, Mode of math score is: {},{},{}".format(mathmean , mathmedian , mathmode))
print(" Mean, Median, Mode of reading score is: {},{},{}".format(readmean , readmedian , readmode))
print(" Mean, Median, Mode of writing score is: {},{},{}".format(writemean , writemedian , writemode))

print("\n")

std = statistics.stdev(mathlist)
std2 = statistics.stdev(readlist)
std3 = statistics.stdev(writelist)

math_first_std_start, math_first_std_end = mathmean - std, mathmean + std
math_second_std_start, math_second_std_end = mathmean - (2 * std), mathmean + (2 * std)
math_third_std_start, math_third_std_end = mathmean - (3 * std), mathmean + (3 * std)

read_first_std_start, read_first_std_end = readmean - std2 , readmean + std2
read_second_std_start, read_second_std_end = readmean - (2 * std2), readmean + (2 * std2)
read_third_std_start, read_third_std_end = readmean - (3 * std2), readmean + (3 * std2)

write_first_std_start, write_first_std_end = writemean - std3, writemean + std3
write_second_std_start, write_second_std_end = writemean - (2 * std3), writemean + (2 * std3)
write_third_std_start, write_third_std_end = writemean - (3 * std3), writemean + (3 * std3)

mathlistWithin1std = [result for result in mathlist if result>math_first_std_start and result<math_first_std_end]
mathlistWithin2std = [result for result in mathlist if result>math_second_std_start and result<math_second_std_end]
mathlistWithin3std = [result for result in mathlist if result>math_third_std_start and result<math_third_std_end]

readlistWithin1std = [result for result in readlist if result>read_first_std_start and result<read_first_std_end]
readlistWithin2std = [result for result in readlist if result>read_second_std_start and result<read_second_std_end]
readlistWithin3std = [result for result in readlist if result>read_third_std_start and result<read_third_std_end]

writelistWithin1std = [result for result in writelist if result>write_first_std_start and result<write_first_std_end]
writelistWithin2std = [result for result in writelist if result>write_second_std_start and result<write_second_std_end]
writelistWithin3std = [result for result in writelist if result>write_third_std_start and result<write_third_std_end]

print("{} % of math score data lies within 1 std deviation ".format(len(mathlistWithin1std)* 100.0 / len(mathlist) ) )
print("{} % of math score data lies within 2 std deviation ".format(len(mathlistWithin2std)* 100.0 / len(mathlist) ) )
print("{} % of math score data lies within 3 std deviation ".format(len(mathlistWithin3std)* 100.0 / len(mathlist) ) )

print("\n")

print("{} % of reading score data lies within 1 std deviation ".format(len(readlistWithin1std)* 100.0 / len(readlist) ) )
print("{} % of reading score data lies within 2 std deviation ".format(len(readlistWithin2std)* 100.0 / len(readlist) ) )
print("{} % of reading score data lies within 3 std deviation ".format(len(readlistWithin3std)* 100.0 / len(readlist) ) )

print("\n")

print("{} % of writing score data lies within 1 std deviation ". format(len(writelistWithin1std)* 100.0 / len(writelist) ) ) 
print("{} % of writing score data lies within 2 std deviation ". format(len(writelistWithin2std)* 100.0 / len(writelist) ) )
print("{} % of writing score data lies within 3 std deviation ". format(len(writelistWithin3std)* 100.0 / len(writelist) ) )

print("\n")

fig = ff.create_distplot([readlist], ["Result"], show_hist=False)

fig.add_trace(go.Scatter(x = [readmean, readmean], y = [0, 0.17], mode = "lines+markers", name = "Mean"))
fig.add_trace(go.Scatter(x = [read_first_std_start, read_first_std_start], y = [0, 0.17], mode = "lines+markers", name="Stadard Deviation 1 start "))
fig.add_trace(go.Scatter(x = [read_first_std_end, read_first_std_end], y = [0, 0.17], mode = "lines+markers", name="Stadard Deviation 1 end"))
fig.add_trace(go.Scatter(x = [read_second_std_start, read_second_std_start], y = [0, 0.17], mode = "lines+markers", name="Standard deviation 2 start" ))
fig.add_trace(go.Scatter(x = [read_second_std_end, read_second_std_end], y = [0, 0.17], mode = "lines+markers", name="Standard deviation 2 end" ))
fig.add_trace(go.Scatter(x = [read_third_std_start, read_third_std_start], y = [0, 0.17], mode = "lines+markers", name="Standard deviation 3 start" ))
fig.add_trace(go.Scatter(x = [read_third_std_end, read_third_std_end], y = [0, 0.17], mode = "lines+markers", name="Standard deviation 3 end" ))

fig.show()