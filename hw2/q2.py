from tensorboard.backend.event_processing import event_accumulator
import matplotlib.pyplot as plot
import numpy as np

ea1 = event_accumulator.EventAccumulator('./Q2/q2_b_900__r_0.05__InvertedPendulum-v2_27-09-2021_04-05-29/events.out.tfevents.1632715533.c05057db9314',
 size_guidance={ # see below regarding this argument
      event_accumulator.COMPRESSED_HISTOGRAMS: 500,
      event_accumulator.IMAGES: 4,
      event_accumulator.AUDIO: 4,
      event_accumulator.SCALARS: 0,
      event_accumulator.HISTOGRAMS: 1,
 })


ea1.Reload()


tags = ea1.Tags()
print(tags)
print(ea1.Scalars)
eval_return1 = ea1.Scalars('Eval_AverageReturn')

eval1=[]
print(len(eval_return1))
for i in range(len(eval_return1)):
    eval1.append(eval_return1[i].value)


figure, ax = plot.subplots()

ax.set_xticks(np.arange(0, 100, 10))
#ax.set_yticks(np.arange(0, 100, 10))
ax.set_xlabel('number of iterations')
ax.set_ylabel('average_reward')
ax.set_title('Q2 with lr=0.05 b=900')
plot.plot(eval1, alpha = 0.8)
plot.legend()
plot.show()
