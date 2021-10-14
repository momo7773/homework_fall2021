from tensorboard.backend.event_processing import event_accumulator
import matplotlib.pyplot as plot
import numpy as np

ea1 = event_accumulator.EventAccumulator('./Q3/q3_b40000_r0.005_LunarLanderContinuous-v2_26-09-2021_05-36-24/events.out.tfevents.1632634584.be5c12c56a4a',
 size_guidance={ # see below regarding this argument
      event_accumulator.COMPRESSED_HISTOGRAMS: 500,
      event_accumulator.IMAGES: 4,
      event_accumulator.AUDIO: 4,
      event_accumulator.SCALARS: 0,
      event_accumulator.HISTOGRAMS: 1,
 })


ea1.Reload()

tags = ea1.Tags()
eval_return1 = ea1.Scalars('Eval_AverageReturn')
eval1 = []
for i in range(len(eval_return1)):
    eval1.append(eval_return1[i].value)


figure, ax = plot.subplots()

ax.set_xticks(np.arange(0, 300, 10))
#ax.set_yticks(np.arange(0, 100, 10))
ax.set_xlabel('number of iterations')
ax.set_ylabel('average_reward')
ax.set_title('LunarLandar')
plot.plot(eval1, alpha = 0.8)
#plot.legend()
plot.show()
