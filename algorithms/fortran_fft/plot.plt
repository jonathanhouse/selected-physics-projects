# plot.plt
set term png
set output "plot.png"
set title "FFT of pitches.txt"
m = "data.txt"
plot m using 1:2 with lines title ""