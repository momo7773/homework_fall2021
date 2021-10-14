from tensorboard.backend.event_processing import event_accumulator
import matplotlib.pyplot as plot
import numpy as np

ea1 = event_accumulator.EventAccumulator('./Q4/q4_search_b_10000__lr_0.01__rtg_nnbaseline_HalfCheetah-v2_26-09-2021_18-19-54/events.out.tfevents.1632680399.bb359f2c915e',
 size_guidance={ # see below regarding this argument
      event_accumulator.COMPRESSED_HISTOGRAMS: 500,
      event_accumulator.IMAGES: 4,
      event_accumulator.AUDIO: 4,
      event_accumulator.SCALARS: 0,
      event_accumulator.HISTOGRAMS: 1,
 })
ea2 = event_accumulator.EventAccumulator('./Q4/q4_search_b_10000__lr_0.02__rtg_nnbaseline_HalfCheetah-v2_26-09-2021_18-32-34/events.out.tfevents.1632681158.bb359f2c915e',
  size_guidance={ # see below regarding this argument
       event_accumulator.COMPRESSED_HISTOGRAMS: 500,
       event_accumulator.IMAGES: 4,
       event_accumulator.AUDIO: 4,
       event_accumulator.SCALARS: 0,
       event_accumulator.HISTOGRAMS: 1,
  })
ea3 = event_accumulator.EventAccumulator('./Q4/q4_search_b_10000__lr_0.005__rtg_nnbaseline_HalfCheetah-v2_26-09-2021_18-05-48/events.out.tfevents.1632679555.bb359f2c915e',
  size_guidance={ # see below regarding this argument
       event_accumulator.COMPRESSED_HISTOGRAMS: 500,
       event_accumulator.IMAGES: 4,
       event_accumulator.AUDIO: 4,
       event_accumulator.SCALARS: 0,
       event_accumulator.HISTOGRAMS: 1,
  })
ea4 = event_accumulator.EventAccumulator('./Q4/q4_search_b_30000__lr_0.01__rtg_nnbaseline_HalfCheetah-v2_26-09-2021_19-19-32/events.out.tfevents.1632683977.bb359f2c915e',
  size_guidance={ # see below regarding this argument
       event_accumulator.COMPRESSED_HISTOGRAMS: 500,
       event_accumulator.IMAGES: 4,
       event_accumulator.AUDIO: 4,
       event_accumulator.SCALARS: 0,
       event_accumulator.HISTOGRAMS: 1,
  })
ea5 = event_accumulator.EventAccumulator('./Q4/q4_search_b_30000__lr_0.02__rtg_nnbaseline_HalfCheetah-v2_26-09-2021_19-50-02/events.out.tfevents.1632685807.bb359f2c915e',
   size_guidance={ # see below regarding this argument
        event_accumulator.COMPRESSED_HISTOGRAMS: 500,
        event_accumulator.IMAGES: 4,
        event_accumulator.AUDIO: 4,
        event_accumulator.SCALARS: 0,
        event_accumulator.HISTOGRAMS: 1,
   })
ea6 = event_accumulator.EventAccumulator('./Q4/q4_search_b_30000__lr_0.005__rtg_nnbaseline_HalfCheetah-v2_26-09-2021_18-49-32/events.out.tfevents.1632682177.bb359f2c915e',
    size_guidance={ # see below regarding this argument
         event_accumulator.COMPRESSED_HISTOGRAMS: 500,
         event_accumulator.IMAGES: 4,
         event_accumulator.AUDIO: 4,
         event_accumulator.SCALARS: 0,
         event_accumulator.HISTOGRAMS: 1,
    })
ea7 = event_accumulator.EventAccumulator('./Q4/q4_search_b_50000__lr_0.01__rtg_nnbaseline_HalfCheetah-v2_26-09-2021_21-11-31/events.out.tfevents.1632690696.bb359f2c915e',
    size_guidance={ # see below regarding this argument
         event_accumulator.COMPRESSED_HISTOGRAMS: 500,
         event_accumulator.IMAGES: 4,
         event_accumulator.AUDIO: 4,
         event_accumulator.SCALARS: 0,
         event_accumulator.HISTOGRAMS: 1,
    })
ea8 = event_accumulator.EventAccumulator('./Q4/q4_search_b_50000__lr_0.02__rtg_nnbaseline_HalfCheetah-v2_26-09-2021_20-19-07/events.out.tfevents.1632687552.bb359f2c915e',
    size_guidance={ # see below regarding this argument
         event_accumulator.COMPRESSED_HISTOGRAMS: 500,
         event_accumulator.IMAGES: 4,
         event_accumulator.AUDIO: 4,
         event_accumulator.SCALARS: 0,
         event_accumulator.HISTOGRAMS: 1,
    })
ea9 = event_accumulator.EventAccumulator('./Q4/q4_search_b_50000__lr_0.005__rtg_nnbaseline_HalfCheetah-v2_26-09-2021_22-05-12/events.out.tfevents.1632693917.bb359f2c915e',
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
ea7.Reload()
ea8.Reload()
ea9.Reload()



tags = ea1.Tags()
print(tags)
print(ea1.Scalars)
eval_return1 = ea1.Scalars('Eval_AverageReturn')
eval_return2 = ea2.Scalars('Eval_AverageReturn')
eval_return3 = ea3.Scalars('Eval_AverageReturn')
eval_return4 = ea4.Scalars('Eval_AverageReturn')
eval_return5 = ea5.Scalars('Eval_AverageReturn')
eval_return6 = ea6.Scalars('Eval_AverageReturn')
eval_return7 = ea7.Scalars('Eval_AverageReturn')
eval_return8 = ea8.Scalars('Eval_AverageReturn')
eval_return9 = ea9.Scalars('Eval_AverageReturn')
eval1 = []
eval2 = []
eval3 = []
eval4=[]
eval5 = []
eval6 = []
eval7 = []
eval8=[]
eval9=[]
for i in range(len(eval_return1)):
    eval1.append(eval_return1[i].value)
    eval2.append(eval_return2[i].value)
    eval3.append(eval_return3[i].value)
    eval4.append(eval_return4[i].value)
    eval5.append(eval_return5[i].value)
    eval6.append(eval_return6[i].value)
    eval7.append(eval_return7[i].value)
    eval8.append(eval_return8[i].value)
    eval9.append(eval_return9[i].value)


#print(eval3)
figure, ax = plot.subplots()

ax.set_xticks(np.arange(0, 100, 10))
#ax.set_yticks(np.arange(0, 100, 10))
ax.set_xlabel('number of iterations')
ax.set_ylabel('average_reward')
ax.set_title('Q4a')
plot.plot(eval1, label = 'b=10000,lr=0.01', alpha = 0.8)
plot.plot(eval2, label = 'b=10000,lr=0.02', alpha = 0.8)
plot.plot(eval3, label = 'b=10000,lr=0.005',alpha = 1)
plot.plot(eval4, label = 'b=30000,lr=0.01',alpha = 0.8)
plot.plot(eval5, label = 'b=30000,lr=0.02', alpha = 0.8)
plot.plot(eval6, label = 'b=30000,lr=0.005', alpha = 0.8)
plot.plot(eval7, label = 'b=50000,lr=0.01',alpha = 1)
plot.plot(eval8, label = 'b=50000,lr=0.02',alpha = 0.8)
plot.plot(eval9, label = 'b=50000,lr=0.005',alpha = 0.8)
plot.legend()
plot.show()
