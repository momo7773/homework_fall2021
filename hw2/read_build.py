from tensorboard.backend.event_processing import event_accumulator
import matplotlib.pyplot as plot
import numpy as np

ea1 = event_accumulator.EventAccumulator('./Q1/events.out.tfevents.sm_c1',
 size_guidance={ # see below regarding this argument
      event_accumulator.COMPRESSED_HISTOGRAMS: 500,
      event_accumulator.IMAGES: 4,
      event_accumulator.AUDIO: 4,
      event_accumulator.SCALARS: 0,
      event_accumulator.HISTOGRAMS: 1,
 })
ea2 = event_accumulator.EventAccumulator('./Q1/events.out.tfevents.sm_c2',
  size_guidance={ # see below regarding this argument
       event_accumulator.COMPRESSED_HISTOGRAMS: 500,
       event_accumulator.IMAGES: 4,
       event_accumulator.AUDIO: 4,
       event_accumulator.SCALARS: 0,
       event_accumulator.HISTOGRAMS: 1,
  })
ea3 = event_accumulator.EventAccumulator('./Q1/events.out.tfevents.sm_c3',
  size_guidance={ # see below regarding this argument
       event_accumulator.COMPRESSED_HISTOGRAMS: 500,
       event_accumulator.IMAGES: 4,
       event_accumulator.AUDIO: 4,
       event_accumulator.SCALARS: 0,
       event_accumulator.HISTOGRAMS: 1,
  })

ea4 = event_accumulator.EventAccumulator('./Q1/events.out.tfevents.lg_c1',
   size_guidance={ # see below regarding this argument
        event_accumulator.COMPRESSED_HISTOGRAMS: 500,
        event_accumulator.IMAGES: 4,
        event_accumulator.AUDIO: 4,
        event_accumulator.SCALARS: 0,
        event_accumulator.HISTOGRAMS: 1,
   })

ea5 = event_accumulator.EventAccumulator('./Q1/events.out.tfevents.lg_c2',
    size_guidance={ # see below regarding this argument
         event_accumulator.COMPRESSED_HISTOGRAMS: 500,
         event_accumulator.IMAGES: 4,
         event_accumulator.AUDIO: 4,
         event_accumulator.SCALARS: 0,
         event_accumulator.HISTOGRAMS: 1,
    })
ea6 = event_accumulator.EventAccumulator('./Q1/events.out.tfevents.lg_c3',
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
ea5.Reload()
ea6.Reload()

tags = ea1.Tags()
print(tags)
eval_return1 = ea1.Scalars('Eval_AverageReturn')
eval_return2 = ea2.Scalars('Eval_AverageReturn')
eval_return3 = ea3.Scalars('Eval_AverageReturn')

eval_return4 = ea4.Scalars('Eval_AverageReturn')
eval_return5 = ea5.Scalars('Eval_AverageReturn')
eval_return6 = ea6.Scalars('Eval_AverageReturn')
#print(eval_return[0].value)

eval1 = []
eval2 = []
eval3 = []

eval4 = []
eval5 = []
eval6 = []
for i in range(len(eval_return1)):
    eval1.append(eval_return1[i].value)
    eval2.append(eval_return2[i].value)
    eval3.append(eval_return3[i].value)

    eval4.append(eval_return4[i].value)
    eval5.append(eval_return5[i].value)
    eval6.append(eval_return6[i].value)

figure, ax = plot.subplots()

ax.set_xticks(np.arange(0, 100, 10))
#ax.set_yticks(np.arange(0, 100, 10))
ax.set_xlabel('number of iterations')
ax.set_ylabel('average_reward')
ax.set_title('Small Batch')
plot.plot(eval1, label = 'no_rtg_dsa', alpha = 0.8)
plot.plot(eval2, label = 'rtg_dsa', alpha = 0.5)
plot.plot(eval3, label = 'rtg_na',alpha = 0.4)
plot.legend()
plot.show()
