from elasticsearch_dsl import DocType, Text, Integer, Completion, analyzer, tokenizer

my_analyzer = analyzer(
    'my_analyzer',
    tokenizer=tokenizer(
        'trigram', 'edge_ngram', min_gram=1, max_gram=20),
    filter=['lowercase']
)


class YouTubeVideoDoc(DocType):
    video_title = Text(
        analyzer=my_analyzer
    )
    id = Integer()

    class Meta:
        index = 'youtube_video'
        using = 'art'
