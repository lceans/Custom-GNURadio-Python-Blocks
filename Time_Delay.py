"""

Author: @lceans

"""

import time 
import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  
    """Embedded Python Block that time delays the input file"""

    # initializes the GRC Block input, output, block title, and parameters
    def __init__(self, delay = 0):  
        gr.sync_block.__init__(
            self,
            name='Time Delayed Input',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
 
        # sets a callback for time delay in seconds specified in the GRC block
        self.delay = time.sleep(delay)

    def work(self,  input_items,  output_items):
        
        # sets output equal to the input to just pass through the block 
        output_items[0][:] = input_items[0]
        
        # calls a time delay in seconds 
        sleep.delay

        # returns the input as the output after the specified delay 
        return len(output_items[0])
