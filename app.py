"""
Talk to Twitter and give them my Consumer Key  and Consumer Secret
"""

secretFile = open("./secret.txt", "r")
consumerSecrets = []

for secret in secretFile:
    consumerSecrets.append(secret.strip())

print(consumerSecrets)

