class Variant(object):
    
    
    
    def __init__(self, chromosome, nuc_loc, ref_all, alt_all, name=None):
        self.chromosome = chromosome
        self.nuc_loc = nuc_loc
        self.ref_all = ref_all
        self.alt_all = alt_all
        self.name = name
        
    @staticmethod    
    def load_validchroms(path):
        chrom_list = []
        with open(path) as valid_chromosomes:
            for line in valid_chromosomes:
                line = line.strip('\n').split('\t')
                chrom_list.append(line)
        return(chrom_list)
        
            
    def __str__(self):
        """ Provides a string representation of the variant
        """
        return "chromosome: {} BP: {} Ref_Allele: {} Alt_Allele: {} Name: {}".format(
            self.chromosome,
            self.nuc_loc,
            self.ref_all,
            self.alt_all,
            self.name)
    
    

    @staticmethod
    def validate_variants(chromosome, nuc_loc, ref_all, alt_all, name, clean_people, chrom_list):
        print(ref_all)
        unique_chrom_list = [chrom[0] for chrom in chrom_list]
        if str(chromosome) not in unique_chrom_list:
            print('Chromosome is invalid')
        else:
            for chrom in range(len(chrom_list)):
                if int(nuc_loc) >= 0 and int(nuc_loc) <= int(chrom_list[chrom][1]):
                    usable_allele_list = ['A', 'T', 'C', 'G']
                    if ref_all in usable_allele_list:
                        if alt_all in usable_allele_list:
                            if ref_all != alt_all: 
                                unique_people = [person[0] for person in clean_people]
                                if name in unique_people:
                                    good_var = chromosome, nuc_loc, ref_all, alt_all, name
                                    return(good_var)
                                else:
                                    print('This person is not in you people list')
                            else:
                                print('Reference and alternative alleles are the same')
                        else:
                            print('Alternative allele is invalid')
                    else:
                        print('Reference allele is invalid')
                else:
                    print("BP is invalid")

                                    



        


'''
test_variant = Variant('chr1', '55', 'A', 'C', 'Person_A')
assert test_variant.chromosome == 'chr1' 
print(test_variant)

'''



