#moviendo elementos de una lista a otra

#start with users that need to be verified

unconfirmed_users = ['Alice','brian','candance']#list of unconfirmed users
confirmed_users =[]#se crea una lista vacia - make an empty list

#verified each user until ther are no more uncofirmed users- verificar cada usuario 
#hasta que no haya mas usuarios en la lista

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("verificando usuario: "+ current_user)
    confirmed_users.append(current_user)

print("los siguiente usuarios han sido confirmados: ")
for confirmado in confirmed_users:
    print(confirmado.title())
