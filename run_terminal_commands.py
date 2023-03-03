#!/bin/sh

#hsls (fix rf,eo, vary fairness methods)
#done
nohup python run_benchmark_multiplicity_fair.py -m rf -f eqodds -c eo -n 8 -i hsls -s 25 > output1.txt &
nohup python run_benchmark_multiplicity_fair.py -m rf -f original -c eo -n 8 -i hsls -s 25 > output4.txt &
nohup python run_benchmark_multiplicity_fair.py -m rf -f caleqodds -c eo -n 8 -i hsls -s 25 > output12.txt &

#running
nohup python run_benchmark_multiplicity_fair.py -m rf -f reduction -c eo -n 8 -i hsls -s 25 > output2.txt &
nohup python run_benchmark_multiplicity_fair.py -m rf -f roc -c eo -n 8 -i hsls -s 25 > output3.txt &

#doing: Fair Projection
#todo: Leveraging



#enem
#done
nohup python run_benchmark_multiplicity_fair.py -m rf -f eqodds -c eo -n 8 -i enem -s 25 > output5.txt &
nohup python run_benchmark_multiplicity_fair.py -m rf -f original -c eo -n 8 -i enem -s 25 > output8.txt &
nohup python run_benchmark_multiplicity_fair.py -m rf -f caleqodds -c eo -n 8 -i enem -s 25 > output13.txt &

#running
nohup python run_benchmark_multiplicity_fair.py -m rf -f reduction -c eo -n 8 -i enem -s 25 > output6.txt &
nohup python run_benchmark_multiplicity_fair.py -m rf -f roc -c eo -n 8 -i enem -s 25 > output7.txt &

#adult
#done
nohup python run_benchmark_multiplicity_fair.py -m rf -f eqodds -c eo -n 8 -i adult -s 25 > output9.txt &
nohup python run_benchmark_multiplicity_fair.py -m rf -f original -c eo -n 8 -i adult -s 25 > output12.txt &
nohup python run_benchmark_multiplicity_fair.py -m rf -f caleqodds -c eo -n 8 -i adult -s 25 > output14.txt &

#running
nohup python run_benchmark_multiplicity_fair.py -m rf -f reduction -c eo -n 8 -i adult -s 25 > output10.txt &
nohup python run_benchmark_multiplicity_fair.py -m rf -f roc -c eo -n 8 -i adult -s 25 > output11.txt &

#TODO: run fair projection on Adult 
nohup python run-mp.py --dataset adult 