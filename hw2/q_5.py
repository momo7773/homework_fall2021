from tensorboard.backend.event_processing import event_accumulator
import matplotlib.pyplot as plot
import numpy as np

ea1 = event_accumulator.EventAccumulator('./q5/q5_b2000_r0.001_lambda_0__Hopper-v2_26-09-2021_01-40-08/events.out.tfevents.1632620408.499b7549f86c',
 size_guidance={ # see below regarding this argument
      event_accumulator.COMPRESSED_HISTOGRAMS: 500,
      event_accumulator.IMAGES: 4,
      event_accumulator.AUDIO: 4,
      event_accumulator.SCALARS: 0,
      event_accumulator.HISTOGRAMS: 1,
 })
ea2 = event_accumulator.EventAccumulator('./q5/q5_b2000_r0.001_lambda_0.99__Hopper-v2_26-09-2021_01-05-41/events.out.tfevents.1632618344.67a4e39ee3cc',
  size_guidance={ # see below regarding this argument
       event_accumulator.COMPRESSED_HISTOGRAMS: 500,
       event_accumulator.IMAGES: 4,
       event_accumulator.AUDIO: 4,
       event_accumulator.SCALARS: 0,
       event_accumulator.HISTOGRAMS: 1,
  })
ea3 = event_accumulator.EventAccumulator('./q5/q5_b2000_r0.001_lambda_0.95__Hopper-v2_26-09-2021_02-18-37/events.out.tfevents.1632622723.499b7549f86c',
  size_guidance={ # see below regarding this argument
       event_accumulator.COMPRESSED_HISTOGRAMS: 500,
       event_accumulator.IMAGES: 4,
       event_accumulator.AUDIO: 4,
       event_accumulator.SCALARS: 0,
       event_accumulator.HISTOGRAMS: 1,
  })
ea4 = event_accumulator.EventAccumulator('./q5/q5_b2000_r0.001_lambda_1__Hopper-v2_26-09-2021_01-58-46/events.out.tfevents.1632621529.499b7549f86c',
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
for i in range(len(eval_return1)):
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
ax.set_title('GAE Lambda')
plot.plot(eval1, label = 'lambda=0', alpha = 0.8)
plot.plot(eval2, label = 'lambda=0.99', alpha = 0.8)
plot.plot(eval3, label = 'lambda=0.95',alpha = 1)
plot.plot(eval4, label = 'lambda=0.1',alpha = 0.8)
plot.legend()
plot.show()
