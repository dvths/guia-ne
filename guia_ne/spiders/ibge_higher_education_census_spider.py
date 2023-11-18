import scrapy


class IBGEHigherEducationCensusSpyder(scrapy.Spider):
    name = "higher_education_census"
    start_urls = [
        "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-da-educacao-superior"
    ]

    def parse(self, response):
        titles = response.xpath("//li/a[@class='external-link']/text()").getall()
        urls = response.xpath("//li/a[@class='external-link']/@href").getall()

        for title, url in zip(titles, urls):
            yield {
                "Titulo": title,
                "Url": url,
            }
