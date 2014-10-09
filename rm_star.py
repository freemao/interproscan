#!/sur/lib/python

def rmstar(fafile):
    f0 = open(fafile)
    olds = f0.read()
    if '*' in olds:
        print 'found star in your sequences...'
        print 'now removing stars...'
        news = olds.replace('*\n', '\n')
        f1 = open('.'.join(fafile.split('.')[0:-1])+'removed_star.fasta', 'w')
        f1.write(news)
        print 'Done...'
    else:
        print 'there seems no star symbol in your sequences...'
        print 'nothing to do ~'
    f0.close()
    f1.close()

if __name__ == "__main__":
    import sys
    rmstar(sys.argv[1])
