class Variant(object):
    
    
    
    def __init__(self, chromosome, nuc_loc, ref_all, alt_all, name=None):
        self.chromosome = chromosome
        self.nuc_loc = nuc_loc
        self.ref_all = ref_all
        self.alt_all = alt_all
        self.name = name
        
        
   
            
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
        unique_people = [person[0] for person in clean_people]
        unique_chrom = [chrom[0] for chrom in chrom_list]
        bp_chrom = [chrom[1] for chrom in chrom_list]
        if str(chromosome) in unique_chrom:
            ind = unique_chrom.index(str(chromosome))
            if int(nuc_loc) >= 0 and int(nuc_loc) <= int(bp_chrom[ind]):
                usable_allele_list = ['A', 'T', 'C', 'G']
                if ref_all in usable_allele_list:
                    if alt_all in usable_allele_list:
                        if ref_all != alt_all: 
                            if name in unique_people:
                                good_var = chromosome, nuc_loc, ref_all, alt_all, name
                                return(good_var)
                            else:
                                print('This person is not in your people list')
                        else:
                            print('Reference and alternatice alleles are the same')
                    else:
                        print('Alternative allele is invalid')
                else:
                    print('Reference allele is invalid')
            else:
                print('BP is invalid')
        else:
            print('Chromosome is invalid')
                                
                      
                    
                           
        

                                    



        


'''
test_variant = Variant('chr1', '55', 'A', 'C', 'Person_A')
assert test_variant.chromosome == 'chr1' 
print(test_variant)

'''



