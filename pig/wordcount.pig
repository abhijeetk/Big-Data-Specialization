wordfile = LOAD '/user/cloudera/pigin/testfile*' USING PigStorage('\n') as (linesin:chararray);
wordfile_flat = FOREACH wordfile GENERATE FLATTEN(TOKENIZE(linesin)) as wordin;
wordfile_grpd = GROUP wordfile_flat by wordin;
word_counts = FOREACH wordfile_grpd GENERATE group, COUNT(wordfile_flat.wordin);
STORE word_counts into '/user/cloudera/pigoutnew/word_counts_pig';

