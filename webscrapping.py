from playwright.sync_api import sync_playwright


def passagens_vaidepromo(
    origem: str,
    destino: str,
    ano: int,
    mes: int,
    dia: int,
    adulto: int,
    crianca: int,
    bebe: int,
) -> list:
    with sync_playwright() as p:
        try:
            url = f"https://www.vaidepromo.com.br/passagens-aereas/pesquisa/{origem}{destino}{ano%100}{mes:02d}{dia:02d}/{adulto}/{crianca}/{bebe}/Y/?p"
            browser = p.chromium.launch(
                executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                headless=False,
            )
            context = browser.new_context()
            page = context.new_page()
            page.goto(url)
            saida = page.locator("._column_816x7_1 > strong").nth(0).text_content()
            chegada = page.locator("._column_816x7_1 > strong").nth(1).text_content()
            duracao = page.locator(
                "._duration_816x7_1 > span:first-child"
            ).first.text_content()
            preco = page.locator(
                "._totalContainerFinalPrice_m3tu2_298._totalContainerPriceRow_m3tu2_284 > strong:last-child"
            ).first.text_content()
        except:
            return ["VaidePromo", "Erro", "Erro", "Erro", "Erro", "Erro"]
        context.close()
        browser.close()
    duracao = duracao.replace("h ", ":").strip("m")
    preco = float(preco.strip(r"R$\xa0").replace(".", "").replace(",", "."))
    return ["VaidePromo", saida, chegada, duracao, preco, url]


def passagens_maxmilhas(
    origem: str,
    destino: str,
    ano: int,
    mes: int,
    dia: int,
    adulto: int,
    crianca: int,
    bebe: int,
) -> list:
    with sync_playwright() as p:
        try:
            url = f"https://www.maxmilhas.com.br/busca-passagens-aereas/OW/{origem}/{destino}/{ano}-{mes:02d}-{dia:02d}/{adulto}/{crianca}/{bebe}/EC"
            browser = p.chromium.launch(
                executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                headless=False,
            )
            context = browser.new_context()
            page = context.new_page()
            page.goto(url)
            saida = page.locator(".css-bmn3cy > strong").first.text_content()
            chegada = page.locator(".css-1f0u2gx > strong").first.text_content()
            duracao = page.locator(".css-1aqutjm > .time").first.text_content()
            preco = page.locator(".css-dgk618 > span:last-child").first.text_content()
        except:
            return ["Maxmilhas", "Erro", "Erro", "Erro", "Erro", "Erro"]
        context.close()
        browser.close()
    duracao = duracao.replace("h ", ":").strip("m")
    preco = float(preco.strip(r"R$\xa0").replace(".", "").replace(",", "."))
    return ["Maxmilhas", saida, chegada, duracao, preco, url]


def passagens_123milhas(
    origem: str,
    destino: str,
    ano: int,
    mes: int,
    dia: int,
    adulto: int,
    crianca: int,
    bebe: int,
) -> list:
    with sync_playwright() as p:
        try:
            url = f"https://123milhas.com/v2/busca?de={origem}&para={destino}&adultos={adulto}&criancas={crianca}&bebes={bebe}&ida={dia:02d}-{mes:02d}-{ano}&classe=3&search_id=2111924089"
            browser = p.chromium.launch(
                executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                headless=False,
            )
            context = browser.new_context()
            page = context.new_page()
            page.goto(url)
            saida = (
                page.locator(".flight-time__leg-info > .theme-text--subtitle-1")
                .first.text_content()
                .strip()
            )
            chegada = (
                page.locator(".flight-time__legs-info > .theme-text--subtitle-1")
                .first.text_content()
                .strip()
            )
            chegada = chegada.strip(f" {destino}")
            duracao = (
                page.locator(".flight-time__legs > div > .theme-text--caption-1")
                .first.text_content()
                .strip()
            )
            preco = page.locator(
                ".renewed-flight-card__total--container__value"
            ).first.text_content()
        except:
            return ["123milhas", "Erro", "Erro", "Erro", "Erro", "Erro"]
        context.close()
        browser.close()
    duracao = duracao.replace("h ", ":").strip("m").lstrip("0")
    preco = float(preco.strip(r"R$ ").replace(".", ""))
    return ["123milhas", saida, chegada, duracao, preco, url]


def passagens_azul(
    origem: str,
    destino: str,
    ano: int,
    mes: int,
    dia: int,
    adulto: int,
    crianca: int,
    bebe: int,
) -> list:
    with sync_playwright() as p:
        try:
            url = f"https://www.voeazul.com.br/br/pt/home/selecao-voo?c[0].ds={origem}&c[0].std={mes:02d}/{dia:02d}/{ano}&c[0].as={destino}&p[0].t=ADT&p[0].c={adulto}&p[0].cp=false&{'p[1].t=CHD&p[1].c={crianca}&p[1].cp=false&' if crianca > 0 else ''}{'p[2].t=INF&p[2].c={bebe}&p[2].cp=false&' if bebe > 0 else ''}f.dl=3&f.dr=3&cc=BRL"
            browser = p.chromium.launch(
                executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                headless=False,
            )
            context = browser.new_context()
            page = context.new_page()
            page.goto(url)
            saida = (
                page.locator(".departure.css-qxyl5a").first.text_content().strip(origem)
            )
            chegada = (
                page.locator(".arrival.css-10qt17w").first.text_content().strip(destino)
            )
            duracao = page.locator(
                ".duration.css-12pqtfr > strong"
            ).first.text_content()
            preco = page.locator(".current.css-2db79l").first.text_content()
        except:
            return ["Azul", "Erro", "Erro", "Erro", "Erro", "Erro"]
        context.close()
        browser.close()
    duracao = duracao.replace("\n", "").replace(" ", "").replace("h", ":").strip("m")
    preco = float(preco.strip(r"R$").replace(".", "").replace(",", "."))
    return ["Azul", saida, chegada, duracao, preco, url]


def passagens_gol(
    origem: str,
    destino: str,
    ano: int,
    mes: int,
    dia: int,
    adulto: int,
    crianca: int,
    bebe: int,
) -> list:
    with sync_playwright() as p:
        try:
            url = f"https://b2c.voegol.com.br/compra/busca-parceiros?pv=br&tipo=DF&de={origem}&para={destino}&ida={dia:02d}-{mes:02d}-{ano}&ADT={adulto}ADL=0&CHD={crianca}&INF={bebe}&voebiz=0"
            browser = p.chromium.launch(
                executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                headless=False,
            )
            context = browser.new_context()
            page = context.new_page()
            page.goto(url)
            saida = (
                page.locator(".a-desc__value").nth(0).inner_text().strip(f"{origem} - ")
            )
            chegada = (
                page.locator(".a-desc__value")
                .nth(1)
                .inner_text()
                .strip(f"{destino} - ")
            )
            duracao = page.locator(".a-desc__value").nth(2).inner_text().lstrip("0")
            preco = page.locator(
                ".a-desc__value.a-desc__value--price"
            ).first.inner_text()
        except:
            return ["Gol", "Erro", "Erro", "Erro", "Erro", "Erro"]
        context.close()
        browser.close()
    preco = float(preco.strip(r"R$\xa0").replace(".", "").replace(",", "."))
    return ["Gol", saida, chegada, duracao, preco, url]


def passagens_latam(
    origem: str,
    destino: str,
    ano: int,
    mes: int,
    dia: int,
    adulto: int,
    crianca: int,
    bebe: int,
) -> list:
    with sync_playwright() as p:
        try:
            url = f"https://www.latamairlines.com/br/pt/oferta-voos?origin={origem}&outbound={ano}-{mes:02d}-{dia:02d}T15%3A00%3A00.000Z&destination={destino}&adt={adulto}&chd={crianca}&inf={bebe}&trip=OW&cabin=Economy"
            browser = p.chromium.launch(
                executable_path=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                headless=False,
            )
            context = browser.new_context()
            page = context.new_page()
            page.goto(url)
            saida = (
                page.locator(
                    ".sc-jXbUNg.hdDlnc.latam-typography.latam-typography--heading-04.sc-dhKdcB.flightInfostyles__TextHourFlight-sc__sc-edlvrg-4.bOsUiC.qxdAH"
                )
                .nth(0)
                .inner_text()
            )
            chegada = (
                page.locator(
                    ".sc-jXbUNg.hdDlnc.latam-typography.latam-typography--heading-04.sc-dhKdcB.flightInfostyles__TextHourFlight-sc__sc-edlvrg-4.bOsUiC.qxdAH"
                )
                .nth(1)
                .inner_text()
            )
            duracao = page.locator(
                ".sc-jXbUNg.fIAEUU.latam-typography.latam-typography--paragraph-base.sc-dhKdcB.flightInfostyles__Duration-sc__sc-edlvrg-12.bOsUiC.iMnihw"
            ).first.inner_text()
            preco = page.locator(
                ".sc-jXbUNg.hdDlnc.latam-typography.latam-typography--heading-06.sc-dhKdcB.displayCurrencystyle__CurrencyAmount-sc__sc-hel5vp-2.bOsUiC.koxMWe"
            ).first.inner_text()
        except:
            return ["Latam", "Erro", "Erro", "Erro", "Erro", "Erro"]
        context.close()
        browser.close()
    if saida.find(":") == 1:
        saida = f"0{saida}"
    if chegada.find(":") == 1:
        chegada = f"0{chegada}"
    duracao = duracao.replace(" ", "").replace("min", "").replace("h", ":").strip(".")
    preco = float(preco.replace("BRL ", "").replace(".", "").replace(",", "."))
    return ["Latam", saida, chegada, duracao, preco, url]
