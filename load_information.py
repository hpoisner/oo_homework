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
                    if line[0] not in people_list:
                        people_list.append(line)
                    else:
                        print("Person is not unique:", line)
                else:
                    print("Not an acceptable gender:", line)
        clean_people = Person.parents_in_people(people_list)
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
            name = person[0] 
            gender = person[1] 
            father = Person(person[2], 'male')
            mother = Person(person[3], 'female')
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
        return(variant_list)

    


all_people = load_information.load_people('/Users/hpois/Documents/BMI_Software_Engineering/People.txt')
#print(all_people)
valid_chromosome = load_information.load_validchroms('/Users/hpois/Documents/BMI_Software_Engineering/uscschromosomes.txt')
all_variants = load_information.load_variants('/Users/hpois/Documents/BMI_Software_Engineering/Variants.txt')
print(all_variants)





