from Variant import Variant
from Person import Person

class load_information(object):
    '''Class is used to load in people and their variants.
    File path must be provided.
    '''
    
   
    
    def load_people(path):
        people_list = []
        with open(path) as people_file:
            for line in people_file:
                line = line.strip('\n').split('\t')
                usable_gender = any([line[1].lower() == i for i in ['female', 'f', 'male', 'm']])
                if usable_gender:      
                    people_list.append(line)
                else:
                    print("Not an acceptable gender:", line)
        clean_people_1 = Person.parents_in_people(people_list)
        clean_people = Person.no_dups(clean_people_1)
        return(clean_people)
         
        
    def load_validchroms(path):
        chrom_list = []
        with open(path) as valid_chromosomes:
            for line in valid_chromosomes:
                line = line.strip('\n').split('\t')
                chrom_list.append(line)
        return(chrom_list)


    def people_init(clean_peoplelist):
        person_instance_list = []
        for person in range(len(clean_peoplelist)):
            name = clean_peoplelist[person][0] 
            gender = clean_peoplelist[person][1] 
            father = Person(clean_peoplelist[person][2], 'male')
            mother = Person(clean_peoplelist[person][3], 'female')
            Person_i = Person(name, gender, father, mother)
            person_instance_list.append(Person_i)
        return(person_instance_list)



    def load_variants(path):
        variant_list = []
        with open(path) as variant_file:
            for line in variant_file:
                line = line.strip('\n').split('\t')
                chromosome = line[0]
                nuc_loc = line[1]
                ref_all = line[2]
                alt_all = line[3]
                name = line[4]
                pass_to_validate = Variant.validate_variants(chromosome, nuc_loc, ref_all, alt_all, name, all_people, valid_chromosome)
                variant_list.append(pass_to_validate)
                variant_list = [x for x in variant_list if x is not None]
        return(variant_list)
    
    def variant_init(variant_list):
        variant_instance_list = []
        for variant in range(len(variant_list)):
            chromosome = variant_list[variant][0]
            nuc_loc = variant_list[variant][1]
            ref_all = variant_list[variant][2]
            alt_all = variant_list[variant][3]
            name = variant_list[variant][4]
            Variant_i = Variant(chromosome, nuc_loc, ref_all, alt_all, name)
            variant_instance_list.append(Variant_i)
        return(variant_instance_list)
                          

    


all_people = load_information.load_people('People.txt')
#print(all_people)
valid_chromosome = load_information.load_validchroms('uscschromosomes.txt')
all_variants = load_information.load_variants('Variants.txt')
#print(all_variants)
instantiated_people = load_information.people_init(all_people)
instantiated_variants = load_information.variant_init(all_variants)

instantiated_people[0].add_single_variant(Variant('chr1','5', 'T', 'C'))
print(instantiated_people[0])
print(instantiated_people[0].variant_list[0])

instantiated_people[0].add_variant_list(instantiated_variants)
print(instantiated_people[0])
print(instantiated_people[0].variant_list[0])
print(instantiated_people[0].variant_list[1])
print(instantiated_people[0].variant_list[2])

for person in instantiated_people:
    person.add_variant_list(instantiated_variants)
    print(person)
    if len(person.variant_list) >= 1:
        print(person.variant_list[0])
        print(person.variant_list[-1])





