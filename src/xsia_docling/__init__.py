from docling.document_converter import DocumentConverter


def main() -> None: # pyright: ignore[reportUnknownParameterType]
    converter = DocumentConverter()
    source = "https://arxiv.org/pdf/2408.09869"  # file path or URL
    doc = converter.convert(source).document
    print(doc.export_to_markdown())  # output: "### Docling Technical Report[...]"
