import csv 

class Owner:
    def __init__(self, id, l_name, f_name, street_address, city, state):
        self.id = id
        self.l_name = l_name 
        self.f_name = f_name 
        self.street_address = street_address
        self.city = city 
        self.state = state

    @classmethod
    def all_owners(cls):
        file_name = './support/owners.csv'
        owner_list = []
        headings = ['id','l_name','f_name','street_address','city','state']

        with open(file_name, newline='') as account_file:
            reader = csv.DictReader(account_file)
            reader.fieldnames = headings

            for row in reader:
                owner_list.append(Owner(int(row['id']),row['l_name'],row['f_name'],row['street_address'],row['city'],row['state']))
            
            print(owner_list)

        return owner_list

    def __str__(self):
        return f"Owner name: {self.f_name} {self.l_name}\nOwner id: {self.id}"