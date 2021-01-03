from google.cloud import language_v1beta2


def nlp(content):
    client = language_v1beta2.LanguageServiceClient()
    result = []
    document = language_v1beta2.Document(content=content, type_=language_v1beta2.Document.Type.PLAIN_TEXT)
    encoding_type = language_v1beta2.EncodingType.UTF8
    entities = client.analyze_entities(request={'document': document, 'encoding_type': encoding_type})

    for entity in entities.entities:
        result.append({'name': entity.name, 'type': str(entity.type_), 'metadata': entity.metadata})
    return result


if __name__ == "__main__":
    print(nlp('[問卦] 哪裡買的到維大力'))
