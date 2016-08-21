# rdkb-spark

This is pretty simple, Basically I just dowloaded data from [Microsoft's Academic Graph](https://academicgraph.blob.core.windows.net/graph-2016-02-05/index.html) and ran some basic map and reduce operations on it. The Amazon cluster had 1 master and 2 additional machines. Each was an m3.xlarge. 

### How big is the data?
There were roughly 530 million papers in the data, so pretty big. A lot of these operations took quite some time on the smallish cluster I was using.

### Steps
1. Download data
2. Unzip data
3. Import data into the hdfs (I did this by ssh into the master server
4. Run the python script
5. Wait a long time. (Presumably less with more servers)

### Results
Well, I was able to do some 'big data'. There is no real analysis to speak of - it's just basic SQL-like operations on a very large dataset. I am anxious to do some more complicated things. For example, with this dataset I'd like to build a author citation network, and then find min cuts. This is the first project I've done that costs money for server resources, so I will need to be a little more solid on my work before shelling out the dough.

Output from the last step:
```
[
(2144634347.0, (u'Molecular cloning : a laboratory manual', u'molecular cloning a laboratory manual', u'1989', u'1989', u'', u'BioScience', u'bioscience', u'0742FAC4', u'', u'9004')), 
(2100837269.0, (u'Cleavage of Structural Proteins during the Assembly of the Head of Bacteriophage T4', u'cleavage of structural proteins during the assembly of the head of bacteriophage t4', u'1970', u'1970/08/15', u'10.1038/227680a0', u'Nature', u'nature', u'08364228', u'', u'10099')), 
(1775749144.0, (u'Protein measurement with the folin phenol reagent', u'protein measurement with the folin phenol reagent', u'1951', u'1951/11/01', u'', u'Journal of Biological Chemistry', u'j biol chem', u'085C135E', u'', u'7223')), 
(2168526937.0, (u'A SIMPLE METHOD FOR THE ISOLATION AND PURIFICATION OF TOTAL LIPIDES FROM ANIMAL TISSUES', u'a simple method for the isolation and purification of total lipides from animal tissues', u'1957', u'1957/05/01', u'', u'Journal of Biological Chemistry', u'j biol chem', u'085C135E', u'', u'9360')), 
(2128635872.0, (u'A rapid and sensitive method for the quantitation of microgram quantities of protein utilizing the principle of protein-dye binding.', u'a rapid and sensitive method for the quantitation of microgram quantities of protein utilizing the principle of protein dye binding', u'1976', u'1976/05/07', u'10.1016/0003-2697(76)90527-3', u'Analytical Biochemistry', u'anal biochem', u'0077EA64', u'', u'10345')), 
(2134812217.0, (u'SINGLE STEP METHOD OF RNA ISOLATION BY ACID GUANIDINIUM-THIOCYANATE-PHENOL-CHLOROFORM EXTRACTION', u'single step method of rna isolation by acid guanidinium thiocyanate phenol chloroform extraction', u'1987', u'1987/04/01', u'10.1016/0003-2697(87)90021-2', u'Analytical Biochemistry', u'anal biochem', u'0077EA64', u'', u'11279')), 
(2106882534.0, (u'CLUSTAL W: improving the sensitivity of progressive multiple sequence alignment through sequence weighting, position-specific gap penalties and weight matrix choice', u'clustal w improving the sensitivity of progressive multiple sequence alignment through sequence weighting position specific gap penalties and weight matrix choice', u'1994', u'1994/11/11', u'10.1093/nar/22.22.4673', u'Nucleic Acids Research', u'nar', u'0806DF69', u'', u'9990')), 
(2143981217.0, (u'Density\u2010functional thermochemistry. III. The role of exact exchange', u'density functional thermochemistry iii the role of exact exchange', u'1993', u'1993/04/01', u'10.1063/1.464913', u'Journal of Chemical Physics', u'j chem phys', u'0497A7C5', u'', u'11423')), 
(2107277218.0, (u'Analysis of Relative Gene Expression Data Using Real-Time Quantitative PCR and the 2 \u2212\u0394\u0394CT Method', u'analysis of relative gene expression data using real time quantitative pcr and the 2 \u03b4\u03b4ct method', u'2001', u'2001', u'10.1006/meth.2001.1262', u'Methods', u'methods', u'04621F41', u'', u'12633')), 
(2028556299.0, (u'Analysis of relative gene expression data using real-time quantitative PCR and the 2(-Delta Delta C(T)) Method.', u'analysis of relative gene expression data using real time quantitative pcr and the 2 delta delta c t method', u'2001', u'2001/12', u'10.1006/meth.2001.1262', u'Methods', u'methods', u'04621F41', u'', u'10883'))
]
```
