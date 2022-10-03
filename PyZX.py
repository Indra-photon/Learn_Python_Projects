#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install qiskit
get_ipython().system('pip install pyzx')


# ### Creating an 1D and 2D graph state in pyzx

# In[20]:


import pyzx as zx
g = zx.Graph() # we construct an empty ZX diagram
v = g.add_vertex (1,0,0) # we add a Z-spider at position (0,0)
w= g.add_vertex (2,0,1) # we add a X- spider at position (0,1)
g.add_edge((v,w))  # we connect the two spiders together
display(zx.draw(g)) #Draw the zx diagram onto the screen
print("We will now set the phase of the spiders to a different value")
g.add_to_phase(0, 3/2)  # o means add phase to the 0th vertex, phase = 3*pi/2
g.add_to_phase(1, 1/2)  # 1 means add phase to the 1st vertex, phase = pi/2
display(zx.draw(g))

# Let us create a 2D graph state

s = zx.Graph()
t = s.add_vertex (1,0,0) # we add a Z-spider at position (0,0)
u = s.add_vertex (2,0,1) # we add a X- spider at position (0,1)
s.add_edge((t,u))
x = s.add_vertex (1,1,0)
y = s.add_vertex (2,1,1)
s.add_edge((t,x))
s.add_edge((x,y))
s.add_to_phase(2, 1/2)
s.add_to_phase(3, 3/2)
display(zx.draw(s))


# ### Hadamard Operation

# In[48]:


import pyzx as zx
from qiskit import *
from numpy import pi
import numpy as np
#instate = [1/np.sqrt(2), 1/np.sqrt(2)]
qr = QuantumRegister(1)
cr = ClassicalRegister(1)
qc = QuantumCircuit(qr, cr)
#qc.append(Initialize(instate), [0])
qc.h(0)
qc = qc.decompose()
qc.draw('mpl')
qc.qasm(filename = 'hadamard')


# In[49]:


#ZX model
circ = zx.Circuit.from_qasm_file('hadamard')


# In[50]:


zx.draw_matplotlib(circ, figsize=(5,1), h_edge_draw='box')


# ###  any single-qubit unitary gate is equal (up to global phase) to a rotation of the Bloch sphere over some axis. Hence, by decomposing the rotation using Euler angles we can represent any single-qubit unitary with a Z-rotation followed by an X-rotation, followed once again by a Z-rotation:
# ### For hadamard operation this angle is equal to $\frac{\pi}{2}$, also the Z, X, and, Z rotation you can observe 
# 

# In[ ]:




