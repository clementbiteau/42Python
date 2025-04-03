ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "France!")
ft_set.discard("tutu!")
ft_set.add("Paris!")
ft_dict["Hello"] = "42Paris!"

print(ft_list) #Mutable list :> can be changed by index
print(ft_tuple) #Immutabke tuple :> must be re created
print(ft_set) #Mutable set :> must discard item then add a new => unordered - ouput may vary
print(ft_dict) #Mutable dictionnary :> change the key by name