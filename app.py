#Mad libs Python Project

print(" Welcome to Mad libs Python Project: ")
 

name = input( "Enter the name:")

date_of_birth = input( "Entre the date_of_birth:" )

place1 = input("Enter the birthplace:")

place2 = input("Enter the place of education first:") 

place3 = input("Enter the place of education second:") 

year1 = int(input("Enter the year of Pakistan Resolution :"))

place4 = input("Enter the place of Pakistan Resolution:") 

indepandence_date = input("Enter the indepandence_date:")
 
motto = input("Enter the motto:")

year2 = int(input("Enter the year of his passing:"))

story = (f"""{name}, the founder of Pakistan and its first Governor-General, 
was born in {date_of_birth} in {place1}. He receive his education in {place2} and {place3},becoming
a barrister. Initially, Jinnah worked for India's independence, but later realized that Muslims needed a separate homeland.
    On 23rd March {year1} , he led the Pakistan Resolution in {place4}, which became the foundation for the creation 
of Pakistan. Under his leadership, Pakistan gained independence on {indepandence_date}. Quaid-e-Azam’s famous 
motto was: "{motto}" He passed away on 11th September {year2}, but his efforts and sacrifices will always
be remembered.""")
print("\nStory of Quaid-e-Azam\n")
print(story)