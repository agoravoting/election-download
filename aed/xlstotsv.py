import codecs
from openpyxl import load_workbook


def xls_to_tsv(src, dst):
    wb = load_workbook(src)
    sheets = wb.get_sheet_names()
    for s in sheets:
        ws = wb[s]
        dst1 = "%s_%s.tsv" % (dst, s)
        with codecs.open(dst1, 'w', 'utf8') as f:
            for r in ws.rows:
                for c in r:
                    if c.value is not None:
                        f.write(unicode(c.value))
                        f.write('\t')
                f.write('\n')


if __name__ == '__main__':
    import sys
    xls_to_tsv(sys.argv[1], '/tmp/out')
