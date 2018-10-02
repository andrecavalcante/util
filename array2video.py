
# does not require libx264 

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation

FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata, codec='rawvideo')

fig = plt.figure()

with writer.saving(fig, "writer_test.mp4", dpi=60):
    num_frames = 100
    for i in range(num_frames):
        
        # Create random frame
        frame = np.uint8(np.random.randint(0, 255, (100,100)))
        
        plt.imshow(frame)
        writer.grab_frame()
        
        plt.clf() # make sure to clear plot after each frame is grabbed so it does not slow down
