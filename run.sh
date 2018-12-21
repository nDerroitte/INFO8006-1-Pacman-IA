#!/bin/bash

echo ------
echo HMINIMAX
echo large dumby
python3 run.py --ghostagent dumby --layout large_adv --agentfile hminimax.py
echo large greedy
python3 run.py --ghostagent greedy --layout large_adv --agentfile hminimax.py
echo large smarty
python3 run.py --ghostagent smarty --layout large_adv --agentfile hminimax.py

echo medium dumby
python3 run.py --ghostagent dumby --layout medium_adv --agentfile hminimax.py
echo medium greedy
python3 run.py --ghostagent greedy --layout medium_adv --agentfile hminimax.py
echo medium smarty
python3 run.py --ghostagent smarty --layout medium_adv --agentfile hminimax.py

echo small dumby
python3 run.py --ghostagent dumby --layout small_adv --agentfile hminimax.py
echo small greedy
python3 run.py --ghostagent greedy --layout small_adv --agentfile hminimax.py
echo small smarty
python3 run.py --ghostagent smarty --layout small_adv --agentfile hminimax.py
echo ------
echo MINIMAX

echo small dumby
python3 run.py --ghostagent dumby --layout small_adv --agentfile minimax.py
echo small greedy
python3 run.py --ghostagent greedy --layout small_adv --agentfile minimax.py
echo small smarty
python3 run.py --ghostagent smarty --layout small_adv --agentfile minimax.py

echo ------
echo ALPHABETA
echo small dumby
python3 run.py --ghostagent dumby --layout small_adv --agentfile alphabeta.py
echo small greedy
python3 run.py --ghostagent greedy --layout small_adv --agentfile alphabeta.py
echo small smarty
python3 run.py --ghostagent smarty --layout small_adv --agentfile alphabeta.py
echo ------

