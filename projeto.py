from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    current_date = datetime.now().strftime("%d/%m/%Y")
    author_name = "Izaura Souza"  

    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'{PDF.author_name} - {PDF.current_date}', 0, 0, 'R')

    def doc_title(self, title, subtitle1, subtitle2):
        self.add_page()
        self.set_font('Arial', 'B', 14)
        self.cell(0, 30, title, ln=True, align='C')
        self.set_font('Arial', '', 12)
        self.cell(0, 10, subtitle1, ln=True, align='C')
        self.cell(0, 10, subtitle2, ln=True, align='C')
        self.ln(10)

    def doc_section(self, title, text):
        self.add_page()
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, text)

    def add_images_to_pages(self, image_paths):
        for path in image_paths:
            self.add_page()
            self.image(path, x=15, y=15, w=180)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

pdf.doc_title(
    "Desigualdade na Educação Brasileira: ",
    "A Crescente Preferência dos Alunos por Instituições de Ensino Superior Privadas",
    "e o Ensino a Distância (EAD)"
)

pdf.doc_section(
    "Introdução:",
    "A desigualdade na educação é uma realidade persistente no Brasil. Diferenças socioeconômicas, localização geográfica e acesso desigual a recursos educacionais influenciam diretamente a qualidade do ensino oferecido, criando lacunas significativas entre as instituições públicas e privadas. Esta disparidade afeta não apenas o acesso à educação, mas também a qualidade do aprendizado. A educação no Brasil é um tema central de discussão, caracterizado por desafios e disparidades significativas, principalmente entre as escolas públicas e privadas. Neste artigo, exploraremos o cenário da desigualdade educacional no país, com destaque para a crescente preferência dos estudantes por instituições privadas de ensino superior, especialmente na modalidade de Ensino a Distância (EAD).\nEm 2022, 72% dos alunos que foram aprovados no ensino superior privado optaram por estudar à distância, mostram dados do Censo da Educação Superior 2022, divulgados  pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (Inep).Nas licenciaturas (cursos de formação de professor), o índice foi ainda maior: 93,2%.O crescimento da Educação à Distância (EAD), tendência presente nos últimos anos, gera preocupação de especialistas, por causa da regulação frágil do setor e da dificuldade de mensurar a qualidade dessas graduações.\nOs mecanismos atuais de avaliação de cursos não levam em conta, por exemplo, o tipo de plataforma on-line usada pelas instituições de ensino e o tempo dedicado a aulas síncronas, em que os alunos podem interagir em tempo real com os professores. A tendência é que as faculdades gravem o material didático apenas uma vez e o vendam para um número cada vez maior de interessados."
)

pdf.doc_section(
    "Relação do número de matriculas ativas \n e inativas nos modelos EAD e Presencial",
    "Com base nos dados do MEC, foi gerado um gráfico que demonstra um aumento significativo de vagas ativas no modelo EAD em relação a Presencial.\nPara uma análise detalhada das tendências educacionais no Brasil, decidi utilizar os dados fornecidos pelo Ministério da Educação (MEC). Meu foco está na avaliação da distribuição de matrículas ativas e inativas nos modelos de ensino EAD e presencial, juntamente com a disponibilidade de vagas nas diferentes categorias de instituições de ensino.\nA intenção é compreender a proporção de alunos matriculados e inativos, proporcionando um panorama sobre as preferências em relação aos modelos de ensino. Além disso, pretendo analisar a oferta de vagas nas categorias específicas de instituições de ensino no Rio de Janeiro, incluindo instituições privadas com fins lucrativos, sem fins lucrativos (bolsas de estudos), públicas federais e estaduais.\nEsta análise visa não só compreender a dinâmica da matrícula de alunos, mas também identificar padrões de preferência entre os diferentes modelos de ensino e categorias de instituições. O objetivo final é obter insights valiosos que possam informar políticas e estratégias educacionais no estado do Rio de Janeiro."
)

image_paths = ["educação_modelo.png"]

pdf.add_images_to_pages(image_paths)

pdf.doc_section(
    "No gráfico de pizza, observamos:",
    "Educação a Distância (EAD): Apresenta um percentual mais expressivo (33,4%) de matrículas ativas comparado às inativas (2,7%). Isso sugere que os estudantes ativos veem na modalidade EAD uma alternativa viável para sua educação, o que pode ser motivado por fatores como flexibilidade, acessibilidade e custos reduzidos.\nPresencial: Embora a porcentagem de matrículas ativas (37,3%) seja similar à do EAD, a quantidade de matrículas inativas (26,7%) é mais significativa. Isso pode sinalizar desafios ou obstáculos que os estudantes enfrentam no formato presencial, como custos mais elevados, limitações geográficas, falta de flexibilidade ou dificuldades no acesso à infraestrutura educacional.\nAs análises dos modelos de ensino, tanto EAD quanto presencial, revelam diferentes cenários e desafios para os estudantes. No caso do Ensino a Distância (EAD), a expressiva proporção de matrículas ativas em relação às inativas (33,4% e 2,7%, respectivamente) destaca a crescente preferência dos estudantes por essa modalidade. Isso sugere que os alunos ativos encontram na modalidade EAD uma solução atrativa para sua educação. A flexibilidade de horários, a acessibilidade aos conteúdos e os custos reduzidos podem ser fatores determinantes nessa escolha.\nNo ensino presencial, a porcentagem de matrículas ativas (37,3%) é comparável à do EAD, porém, a quantidade de matrículas inativas (26,7%) é significativamente maior. Esse cenário sugere desafios específicos que os estudantes enfrentam no formato presencial. Custos mais elevados, limitações geográficas, falta de flexibilidade nos horários de aula e possíveis dificuldades de acesso à infraestrutura educacional podem ser fatores contribuintes para a maior proporção de matrículas inativas.Essas análises destacam a importância de compreender as preferências e desafios dos estudantes em cada modelo de ensino, fornecendo insights valiosos para aprimorar estratégias educacionais, adaptando-as às necessidades e expectativas dos alunos, tanto na modalidade presencial quanto na modalidade EAD."
)

image_paths = ["vagas_categoria_RJ.png"]

pdf.add_images_to_pages(image_paths)

pdf.doc_section(
    "Análise das Vagas Autorizadas no Ensino Superior \n por Categorias Administrativas",
    "Os dados representados no gráfico referem-se à quantidade de vagas autorizadas no ensino superior por diferentes categorias administrativas no Brasil. A desigualdade na educação brasileira é notável ao observar esses números.\nAs instituições privadas, tanto com fins lucrativos (totalizando 222.479.942 vagas autorizadas) quanto sem fins lucrativos (totalizando 6.762.243 vagas autorizadas), detêm uma quantidade muito maior de vagas em comparação com as instituições públicas, que incluem estaduais, federais e municipais. As instituições públicas estaduais dispõem de 25.175 vagas, as federais oferecem 160.237 vagas, e as municipais têm 284.617 vagas autorizadas.\nEsses números evidenciam uma disparidade significativa na distribuição de vagas entre as categorias administrativas, mostrando uma predominância massiva de vagas em instituições de ensino superior privados em comparação com as públicas. Essa disparidade é um reflexo da desigualdade educacional no país, destacando a concentração desproporcional de vagas nas instituições de ensino superior privadas, muitas vezes associada a variáveis socioeconômicas, qualidade de ensino e acesso a recursos educacionais."
)

pdf.doc_section(
    "Conclusão:",
    "Os dados indicam uma tendência marcante e crescente na preferência dos estudantes por instituições de ensino superior privadas e pelo formato de Ensino a Distância (EAD). As vagas autorizadas evidenciam uma expressiva predominância nas instituições privadas, tanto com fins lucrativos como sem fins lucrativos(bolsas estudantis), em comparação com as instituições públicas.\nA preferência por instituições privadas de ensino superior está evidenciada na quantidade massiva de vagas autorizadas, demonstrando uma escolha considerável e constante dos alunos por essas instituições. Além disso, a discrepância entre o número de vagas nas instituições públicas em comparação com as privadas reforça essa inclinação dos estudantes em buscar oportunidades nessas instituições privadas.\nO formato de Ensino a Distância (EAD) também mostra uma presença substancial nas vagas autorizadas, especialmente nas instituições privadas, refletindo uma preferência crescente dos alunos por esse método de aprendizado. A elevada quantidade de vagas disponibilizadas para EAD em instituições privadas destaca a atratividade desse formato, provavelmente devido à flexibilidade, acessibilidade e possibilidade de conciliação com outras atividades cotidianas.\nPortanto, esses dados refletem uma tendência crescente de alunos que buscam oportunidades de estudo no Ensino a Distância e em instituições privadas, indicando uma mudança significativa na preferência e na procura por formatos e entidades educacionais que oferecem maior flexibilidade e acessibilidade."
)

pdf.output("final.pdf")
