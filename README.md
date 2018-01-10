the program is a simulation of an optical network with 8 computers.The description of the network follows

Description of the program:

In the optical network of the simulation each computer uses a wave lenght to send his packages to the server.
Computers 1,2 send packages in the wave length λ1,computers 3,4 send packages in the wave length λ2 and so on.
The connection between the server and the computers is being made with combiners and a WDM.The time is divided
into slots.Each slot represents the time that is needed for a package to be sent.Each computer has a buffer
which can store 5 packages.The probability for a package to arrive in a slot is p.If the package arrive and
the buffer is full the package will be discarded.At each slot,every computer that has at least one package at
its buffer will attempt to transmit the first package of the buffer with probability of 0.5 .If two computers
that use the same wave length send their packages in the same slot a collision occures,their packages are being
destroyed,both packages will stay in their perspective buffer and they will try to be retrasmitted at the next 
slot.

To run this programm run the simulator.py.You can specify two optinal arguments in the command line.One is to change the simulation time(default is 10 sec) and the other is to change the time slot(default is 0.01 sec).Use the -h option to take more information about how to use the command line arguments.


