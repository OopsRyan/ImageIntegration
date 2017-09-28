# coding = utf-8
import minecart.color


class PDFParser:
    def __init__(self, ):
        pass

    @staticmethod
    def get_image_from_pdf(self, pdf_path):
        pdf_file = open(pdf_path, 'rb')
        doc = minecart.Document(pdf_file)
        page = doc.get_page(0)
        for shape in page.shapes.iter_in_bbox((0, 0, 100, 200)):
            print shape.path, shape.fill.color.as_rgb()
        img = page.images[0].as_pil()  # requires pillow

        return img


