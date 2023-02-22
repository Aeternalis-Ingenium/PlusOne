from src.security.hashing.algorithms import Argon2Algorithm, BCryptAlgorithm, SHA256Algorithm, SHA512Algorithm

HashingAlgorithmSubClass = Argon2Algorithm | BCryptAlgorithm | SHA256Algorithm | SHA512Algorithm
