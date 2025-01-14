#CS 285 HW2 Policy Gradient
This readme includes detailed command to run question 1-5

##Command for Q1
Network learning rate: 5e all other settings follow the default
```
python cs285/scripts/run_hw2.py --env_name CartPole-v0 -n 100 -b 1000 \
    -lr 0.005 -dsa --exp_name q1_sb_no_rtg_dsa
python cs285/scripts/run_hw2.py --env_name CartPole-v0 -n 100 -b 1000 \
    -lr 0.005 -rtg -dsa --exp_name q1_sb_rtg_dsa
python cs285/scripts/run_hw2.py --env_name CartPole-v0 -n 100 -b 1000 \
    -lr 0.005 -rtg --exp_name q1_sb_rtg_na
python cs285/scripts/run_hw2.py --env_name CartPole-v0 -n 100 -b 5000 \
    -lr 0.005 -dsa --exp_name q1_lb_no_rtg_dsa
python cs285/scripts/run_hw2.py --env_name CartPole-v0 -n 100 -b 5000 \
    -lr 0.005 -rtg -dsa --exp_name q1_lb_rtg_dsa
python cs285/scripts/run_hw2.py --env_name CartPole-v0 -n 100 -b 5000 \
    -lr 0.005 -rtg --exp_name q1_lb_rtg_na
```


##Command for Q2
```
python cs285/scripts/run_hw2.py --env_name InvertedPendulum-v2 \
   --ep_len 1000 --discount 0.9 -n 100 -l 2 -s 64 -b 900 -lr 0.05 -rtg \
   --exp_name q2_b<900>_r<0.05>
```

##Command for Q3
```
python cs285/scripts/run_hw2.py \
    --env_name LunarLanderContinuous-v2 --ep_len 1000
    --discount 0.99 -n 100 -l 2 -s 64 -b 40000 -lr 0.005 \
    --reward_to_go --nn_baseline --exp_name q3_b40000_r0.005
```

##Command for Q4
substitute r with [0.005,0.01,0.02]; b with [10000,30000,50000]
the best performance happens when r=0.02, b=30000
```
python cs285/scripts/run_hw2.py --env_name HalfCheetah-v2 --ep_len 150 \
    --discount 0.95 -n 100 -l 2 -s 32 -b <b> -lr <r> -rtg --nn_baseline \
--exp_name q4_search_b<b>_lr<r>_rtg_nnbaseline
```
use r=0.02, b=30000 run the following
```
python cs285/scripts/run_hw2.py --env_name HalfCheetah-v2 --ep_len 150 \
    --discount 0.95 -n 100 -l 2 -s 32 -b 30000 -lr 0.02 \
    --exp_name q4_b<30000>_r<0.02>
python cs285/scripts/run_hw2.py --env_name HalfCheetah-v2 --ep_len 150 \
    --discount 0.95 -n 100 -l 2 -s 32 -b 30000 -lr 0.02 -rtg \
--exp_name q4_b<30000>_r<0.02>_rtg
python cs285/scripts/run_hw2.py --env_name HalfCheetah-v2 --ep_len 150 \
    --discount 0.95 -n 100 -l 2 -s 32 -b 30000 -lr 0.02 --nn_baseline \
    --exp_name q4_b<30000>_r<0.02>_nnbaseline
python cs285/scripts/run_hw2.py --env_name HalfCheetah-v2 --ep_len 150 \
    --discount 0.95 -n 100 -l 2 -s 32 -b 30000 -lr 0.02 -rtg --nn_baseline \
    --exp_name q4_b<30000>_r<0.02>_rtg_nnbaseline
```

##Command for Q5
sustitute lambda with [0,0.95,0.99,1]
```
python cs285/scripts/run_hw2.py \
    --env_name Hopper-v2 --ep_len 1000
--discount 0.99 -n 300 -l 2 -s 32 -b 2000 -lr 0.001 \
--reward_to_go --nn_baseline --action_noise_std 0.5 --gae_lambda < > \ --exp_name q5_b2000_r0.001_lambda< >
```
