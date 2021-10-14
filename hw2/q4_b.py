from tensorboard.backend.event_processing import event_accumulator
import matplotlib.pyplot as plot
import numpy as np

ea1 = event_accumulator.EventAccumulator('./Q4/q4_b_30000__r_0.02__HalfCheetah-v2_26-09-2021_23-08-25/events.out.tfevents.1632697710.bb359f2c915e',
 size_guidance={ # see below regarding this argument
      event_accumulator.COMPRESSED_HISTOGRAMS: 500,
      event_accumulator.IMAGES: 4,
      event_accumulator.AUDIO: 4,
      event_accumulator.SCALARS: 0,
      event_accumulator.HISTOGRAMS: 1,
 })
ea2 = event_accumulator.EventAccumulator('./Q4/q4_b_30000__r_0.02__nnbaseline_HalfCheetah-v2_27-09-2021_01-31-44/events.out.tfevents.1632706304.c05057db9314',
  size_guidance={ # see below regarding this argument
       event_accumulator.COMPRESSED_HISTOGRAMS: 500,
       event_accumulator.IMAGES: 4,
       event_accumulator.AUDIO: 4,
       event_accumulator.SCALARS: 0,
       event_accumulator.HISTOGRAMS: 1,
  })
ea3 = event_accumulator.EventAccumulator('./Q4/q4_b_30000__r_0.02__rtg_HalfCheetah-v2_26-09-2021_23-37-54/events.out.tfevents.1632699479.bb359f2c915e',
  size_guidance={ # see below regarding this argument
       event_accumulator.COMPRESSED_HISTOGRAMS: 500,
       event_accumulator.IMAGES: 4,
       event_accumulator.AUDIO: 4,
       event_accumulator.SCALARS: 0,
       event_accumulator.HISTOGRAMS: 1,
  })
ea4 = event_accumulator.EventAccumulator('./Q4/q4_b_30000__r_0.02__rtg_nnbaseline_HalfCheetah-v2_27-09-2021_02-04-14/events.out.tfevents.1632708260.c05057db9314',
  size_guidance={ # see below regarding this argument
       event_accumulator.COMPRESSED_HISTOGRAMS: 500,
       event_accumulator.IMAGES: 4,
       event_accumulator.AUDIO: 4,
       event_accumulator.SCALARS: 0,
       event_accumulator.HISTOGRAMS: 1,
  })


ea1.Reload()
ea2.Reload()
ea3.Reload()
ea4.Reload()




tags = ea1.Tags()
print(tags)
print(ea1.Scalars)
eval_return1 = ea1.Scalars('Eval_AverageReturn')
eval_return2 = ea2.Scalars('Eval_AverageReturn')
eval_return3 = ea3.Scalars('Eval_AverageReturn')
eval_return4 = ea4.Scalars('Eval_AverageReturn')
eval1 = []
eval2 = []
eval3 = []
eval4=[]
print(len(eval_return4))
for i in range(len(eval_return4)):
    eval1.append(eval_return1[i].value)
    eval2.append(eval_return2[i].value)
    eval3.append(eval_return3[i].value)
    eval4.append(eval_return4[i].value)


print(eval3)
figure, ax = plot.subplots()

ax.set_xticks(np.arange(0, 300, 10))
#ax.set_yticks(np.arange(0, 100, 10))
ax.set_xlabel('number of iterations')
ax.set_ylabel('average_reward')
ax.set_title('Q4_b with b=30000, lr=0.02')
plot.plot(eval1, label = 'vanilla', alpha = 0.8)
plot.plot(eval2, label = 'nn_baseline', alpha = 0.8)
plot.plot(eval3, label = 'rtg',alpha = 1)
plot.plot(eval4, label = 'rtg_nn_baseline',alpha = 0.8)
plot.legend()
plot.show()
