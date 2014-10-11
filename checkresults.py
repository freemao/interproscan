#!/usr/lib/python
def check_seq_num(tsvfile, fafile):
    ftsv = open(tsvfile)
    ffasta = open(fafile)
    tsv_seqname = set()
    fasta_seqname = set()
    for i in ftsv:
        tsv_seqname.add(i.split()[0])
    print 'there are total %s seq name in tsv file.'%len(tsv_seqname)
    for i in ffasta:
        if i.startswith('>'):
            fasta_seqname.add(i[1:-1])
    print 'there are total %s seq name in fasta file.'%len(fasta_seqname)

    if len(tsv_seqname) == len(fasta_seqname):
        print 'the interproscan results is normal!'

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print 'usage: python checkresults.py tsvfile fafile'
    if len(sys.argv) == 3:
        check_seq_num(sys.argv[1], sys.argv[2])
    else:
        print 'just type script name for help~'


