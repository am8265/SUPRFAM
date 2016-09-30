#!/usr/bin/env python
import re
import sys
fh=open(sys.argv[1])
gene_sprfam=dict()
####{protein_id:{suprfam1:[list of evalues],suprfam2:[lis of evals]},pro_id2:{'-':['-','-']
#]...also consider the case..[('-','-'))
for line in fh:
    line=line.rstrip('\n').strip()
    parse=line.split('\t')
    pro_id=parse[0].strip()
    supr_id=parse[1].strip()
    #if evals!='-':
    evals=parse[2].strip()
    if evals!='-':
        evals=float(evals)
    if gene_sprfam.get(pro_id,'0')=='0':#if this is the first gene_id
        gene_sprfam[pro_id]=dict()
        gene_sprfam[pro_id][supr_id]=[evals]
    elif gene_sprfam[pro_id].get(supr_id,'NA')=='NA':#that supr_id doesn't exitst!
        gene_sprfam[pro_id][supr_id]=[evals]
    else:#if gene_id and surp_id exist already , we create a list of evals
        gene_sprfam[pro_id][supr_id].append(evals)
fh.close()
fh1=open(sys.argv[2])
sprfm_des=dict()
for line in fh1:
    line=line.rstrip('\n').strip()
    parse=line.split('\t')
    sprfam=parse[0].strip()
    des=parse[1].strip()
    if sprfm_des.get(sprfam,'0')=='0':
        sprfm_des[sprfam]=des
    else:
        pass
fh1.close()
#######let's create a table of pro_id, suprfam_id , suprfam_id[description], suprfam_id[min. evalues]
fh2=open(sys.argv[3],'w')
fh2.write('protein_id'+'\t'+'suprfam_id'+'\t'+'description'+'\t'+'Evals'+'\n')
for id in sorted(gene_sprfam.keys()):
    cat_sprfam_id=''
    cat_des=''
    cat_evals=''
    for suprfam_id in gene_sprfam[id].keys():#this can be a list of ['-','-']
        if suprfam_id!='-':#if there is valid hit for suprfam_id 
            des=sprfm_des.get(suprfam_id,'NA')#for this Superfam identifier , NO DESCRIPTION is available!
            min_eval=min(gene_sprfam[id][suprfam_id])#minimum of evalues  
            cat_sprfam_id+=suprfam_id+','
            cat_des+=suprfam_id+'['+des+']'+'; '
            cat_evals+=suprfam_id+'['+str(min_eval)+']'+'; '
        else:#no suprfam_id does not exist for that gene_id
            cat_des='-'
            cat_sprfam_id='-'
            cat_evals='-'
    cat_sprfam_id=cat_sprfam_id.strip(',')
    cat_des=cat_des.rstrip().rstrip(';')
    cat_evals=cat_evals.strip().rstrip(';')
    fh2.write(id+'\t'+cat_sprfam_id+'\t'+cat_des+'\t'+cat_evals+'\n')    
fh2.close()
