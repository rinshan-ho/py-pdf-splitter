from pypdf import PdfReader, PdfWriter
path = 'input.pdf'

# PDFの読み込み
reader = PdfReader(path)


print('ページ番号を入力しください。(全ページを分割する場合はEnterを入力してください)')
p = input('>> ')
if(p==''):
    for i,page in enumerate(reader.pages):
        writer = PdfWriter() # 書き込み用のオブジェクト作成
        writer.add_page(page)
        with open('output_{}.pdf'.format(i+1), 'wb') as f:
            writer.write(f)
# else:
#     # ページ抽出
#     pdf = reader.pages[p]
#     # 書き込み用オブジェクトに追加
#     writer.add_page(pdf)

#     # ファイルに書き出し
#     with open('output.pdf', 'wb') as f:
#         writer.write(f)
