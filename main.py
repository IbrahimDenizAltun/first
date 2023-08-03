import random

suprising_facts = ["Ben varım!", "Matematiğe bayılırım!", "Kodlama yapmak hoşuma gider!", "Piyano çalıyorum!"]

fact_index = random.randint(0, len(suprising_facts)-1)
print(suprising_facts[fact_index])

add_1_more = input("Bir tane de sen yaz! \n")
print("Hobini asagiya yazayim o zaman! \n", add_1_more)
