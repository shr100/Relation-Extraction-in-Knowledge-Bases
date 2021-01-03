# Relation Extraction in Knowledge Bases

A Natural Language Processing based project that focuses on relation extraction between a pair of entities in Knowledge Bases using a clustering algorithm. Created using Python and tested on gold standard KnowledgeNet relations.

**USE** : Can be used to identify and predict relations between a pair of entities, that can improve search results in Knowledge Bases, such as Google's search engine. 

A description of files and folders in this project.
1. json_extract_trees.py - Extracts trees from input json sentences. (In the real world, these would be queries that are input into the search engine.)
2. subtree_extract.py - Extract SUBJECT-OBJECT subtrees from trees.
3. k_means.py - Build positive and negative clusters for each relation . Clustering algorithm uses data matrix obtained by running random_sample.py, that compares subtrees with each other.
4. logistic_reg.py - Trains and tests multi class logistic regressor.
5. Test_data - Contains a small amount of data to test each program file.
