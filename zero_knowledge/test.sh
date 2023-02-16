#!/bin/bash

PYSNARK_BACKEND=snarkjs python3 main.py
snarkjs powersoftau new bn128 14 pot.ptau -v > /dev/null
snarkjs powersoftau prepare phase2 pot.ptau pott.ptau -v > /dev/null
snarkjs zkey new circuit.r1cs pott.ptau circuit.zkey > /dev/null
snarkjs zkey export verificationkey circuit.zkey verification_key.json > /dev/null
snarkjs groth16 prove circuit.zkey witness.wtns proof.json public.json > /dev/null
snarkjs groth16 verify verification_key.json public.json proof.json