from mpyc.runtime import mpc

m = len(mpc.parties)
l = m.bit_length()

mpc.run(mpc.start())
print('m    =', mpc.run(mpc.output(mpc.sum(mpc.input(mpc.SecInt(l+1)(1))))))
print('m**2 =', mpc.run(mpc.output(mpc.sum(mpc.input(mpc.SecInt(2*l+1)(2*mpc.pid + 1))))))
print('2**m =', mpc.run(mpc.output(mpc.prod(mpc.input(mpc.SecInt(m+2)(2))))))
print('m!   =', mpc.run(mpc.output(mpc.prod(mpc.input(mpc.SecInt(int(m*(l-1.4)+3))(mpc.pid + 1))))))
mpc.run(mpc.shutdown())