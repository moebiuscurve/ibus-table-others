import re
if __name__ == "__main__":
    text = file('Phrases.ini', 'r').read()
    text = text.replace('\r', '').replace('\t','')
    lines = text.split('\n')
    r = re.compile('.*?([a-z]+),[0-9]+=(.*)$')
    of = open('emoji-table.txt.data', 'w+')
    for line in lines:
        try:
            key, val = r.match(line).groups()
            of.write('%s\t%s\t0\n' % (key, val))
        except Exception, e:
            print line;
    of.close()
    
