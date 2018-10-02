"""
===========
MovieWriter
===========

This example uses a MovieWriter directly to grab individual frames and write
them to a file. This avoids any event loop integration, but has the advantage
of working with even the Agg backend. This is not recommended for use in an
interactive setting.

"""
# -*- noplot -*-

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
