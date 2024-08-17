import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


## --- PROJECT EXPLANATION 
st.title('Información relevante', anchor=False)
st.markdown(
    '''
    En esta sección encontrarás la documentación del proyecto, así como el planteamiento del mismo y su desarrollo.
    
    ## Origen del proyecto
    Este sitio web fue desarrollado con el fin de analizar y comprender la percepción política de Colombia a nivel nacional e internacional, como parte del [Programa CREDIBLE](https://www.omdena.com/programa-credible-laboratorio-de-ia-para-jovenes-aily-en-colombia-y-republica-dominicana), un ciclo educativo de formación en Ciencia de Datos para personas en Colombia y República Dominicana, en colaboración con [Omdena](https://www.omdena.com/) y [IREX](https://www.irex.org/project/credible-voces-de-la-juventud).
    
    Fecha de finalización: `17 de Agosto 2024`
    
    - [Lineamientos del proyecto](https://docs.google.com/document/d/152L5VsLgPlLHH-Gz_93hOaG3J5BapcxNvHiXiYxhPdc/edit?usp=sharing)

    ## Objetivos
    Como se mencionó anteriormente, el objetivo principal planteado durante este proyecto fue el análisis de noticias en Colombia, ya que el país se ha enfrentado a diversas olas de desinformación, lo que ha llevado a la población a polarizarse en gran medida, desconfiando de medios noticiosos afines a diversos partidos políticos. 
    
    Debido a esta problemática, se buscó desarrollar una herramienta capaz de brindar a los usuarios ayuda al momento de informarse, así como de asistir a los más jóvenes, mientras se encuentran en su etapa de formación, lo que les conferirá más adelante la capacidad de discernir con mayor eficacia las noticias encontradas. 
    
    ## Proceso y Metodología
    La metodología llevada a cabo consistió en un proceso iterativo para las etapas de procesamiento y modelado de datos. Sin embargo, en una sociedad cuya tecnología avanza significativamente en cortos periodos de tiempo, se tomó la decisión final de optar por modelos ya entrenados, empleando llamadas a APIs, de las cuales hablaré más adelante.
    
    Los pasos mencionados a continuación relatarán de manera breve el proceso empleado de principio a fin:
    1. :blue-background[Declaración del objetivo general]
    
        Al ser un proyecto enfocado en resolver una problemática de la vida real, fue necesario plantearse un objetivo que indicara el éxito o punto final del mismo. El alcance de esta herramienta fue seleccionado como la población susceptible a enfrentarse a la desinformación en Colombia, favoreciendo la igualdad al momento de consumir noticias dentro y fuera del país.
    
    2. :blue-background[Recolección de Datos]
    
        Para esta etapa se utilizó la API de [newsapi.ai](https://newsapi.ai/), la cual permitió la recolección de noticias con cantidades superiores a otras API encontradas, así como la capacidad de obtener el contenido completo de los artículos. Los parámetros de búsqueda utilizados se mencionan a fondo en el notebook correspondiente (primera entrega), el cual se encuentra en la sección `Documentación` de esta página.
        
        La recolección tuvo lugar en un periodo de 2 semanas, realizando múltiples llamadas a la API (o queries), entre las fechas del 02 al 13 de Julio del 2024, obteniéndose una base de datos con aproximadamente 5500 noticias, provenientes de medios nacionales e internacionales, cuyos temas tratasen principalmente sobre temas económicos, políticos y sociales de Colombia, para visualizar lo que comúnmente llega a la población al buscar dichos tópicos.
        
    3. :blue-background[Análisis Exploratorio de Datos (EDA)]
    
        Para continuar avanzando fue necesario acudir a una librería ampliamente utilizada en la comunidad al momento de resolver problemas de Procesamiento de Lenguaje Natural (NLP por sus siglas en inglés), llamada `Transformers`, con la que se realizó un análisis de sentimientos de los artículos obtenidos, y posteriormente un análisis de temas principales, el cual fue descartado debido a deficiencias al emplear modelos entrenados con bases de datos reducidas en Español.
        
        El modelo seleccionado fue una [versión afinada del BERT-multilingual](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment), cuya base fue desarrollada por Google y re-entrenada por miembros de la comunidad de [Hugging Face](https://huggingface.co/), clasificando en una escala del 1 al 5 los sentimientos generados por el artículo en cuestión. En el punto 6 se mencionarán los resultados obtenidos brevemente.
        
        El análisis también incluyó un punto importante, el número de palabras por artículo, ya que en la actualidad los medios buscan reducir sus tiempos de lectura por noticia, incrementando el número de noticias para retener a los lectores en sus sitios web.
    
    4. :blue-background[Revisión general de Datos]
    
        Luego de realizar el EDA, se observó que algunas llamadas a la API de noticias obtuvieron datos no relevantes para el proyecto, ya que, aunque eran fuentes de noticias colombianas, hacían referencia a artículos ajenos al país, por lo que se debió realizar una limpieza adicional de los datos previo a la etapa de modelado.
    
    5. :blue-background[Desarrollo de Machine Learning]
    
        Comprobar la veracidad y credibilidad de las noticias fue un punto de alta importancia para la resolución de este proyecto, ya que daría a conocer las fuentes menos relevantes a las cuales están expuestos los usuarios en mayor medida. Por lo tanto, se hizo uso de Modelos de Lenguaje de gran tamaño (Large Language Models, LLMs), que poseen una capacidad y precisión bastante elevadas para tareas de clasificación y análisis de texto.
        
        Fue empleado el modelo Llama 3.1 de Meta (en su versión [llama3.1:8b-instruct-q4_1](https://ollama.com/library/llama3.1:8b-instruct-q4_1) encontrada en Ollama), el cual se publicó el 23 de Julio del 2024 y es hasta el momento, uno de los modelos con mejores puntajes en diversos benchmark de LLMs.

        [Blog de lanzamiento de Llama 3.1](https://ai.meta.com/blog/meta-llama-3-1/)

        Se realizaron dos análisis sobre los artículos:
        
        * Verificación de hechos: Se utilizó el prompt correspondiente para etiquetar las noticias entre 0 y 5, donde 0 es opinión y 5 es basado en hechos. Esta escala fue utilizada debido a que el modelo no cuenta con una precisión perfecta, y de esta manera se reduce un poco su sesgo de entrenamiento.
        * Análisis de tema central: En este caso se le solicitó al modelo que redujera a una palabra el tema principal del que trataba la noticia.
    
    '''
)
    
st.header('Resultados y Conclusiones', anchor=False)
st.markdown(
    '''
    6. :blue-background[Resultados obtenidos]

        A continuación se mostrarán gráficamente los resultados más importantes obtenidos, y una breve explicación.
        
        * El análisis de sentimientos indicó que, en su mayoría, las noticias encontradas en la base de datos reflejaron situaciones negativas en el país, lo cual puede deberse a la alta polaridad que cubre el tema político en la nación, involucrando temas de conflictos armados, situaciones de peligro y discusiones entre partidos políticos relacionados con la corrupción y desequilibrio de poder.
        * La clasificación de hechos y opiniones demostró una alta tasa de noticias basadas en hechos verificables, cuya redacción no incluía en su mayoría opiniones personales, que incluyan una parcialidad. Sin embargo, también se observó un elevado número de errores (encontrados con la etiqueta -1), en los cuales el modelo no fue capaz de identificar correctamente si se trataba de hechos u opiniones. Este resultado fue el principal motivo detrás de la selección del modelo [GPT-4o-mini](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/) de OpenAI al realizar la versión actual de esta herramienta, ya que cuenta con procesamientos más rápidos y eficientes, capaces de brindar información más precisa.
        * Las fuentes mejor clasificadas en el punto anterior (valor promedio de 5), se encontrarán como "Top Fuentes", ya que alcanzaron un puntaje mayor al momento de redactar sus artículos. No obstante, contar con tantos errores pudo significar una desventaja para algunos medios confiables, por lo que se recomienda discreción al momento de tomar una decisión basándose únicamente en este factor.
        * Los temas frecuentes encontrados demostraron que en gran medida se habla de la "paz" en Colombia, en referencia al tratado de paz, notándose la importancia que tiene la historia del país en temas de conflictos internos y su interés conjunto en cambiar la situación. Como se indicó anteriormente, muchos de los temas adicionales tratan asuntos bastante negativos, los cuales deben ser combatidos principalmente con la información y el conocimiento.
    '''
)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        'Sentimientos', 
        'Hecho vs Opinión', 
        'Top Fuentes', 
        'Temas frecuentes',
        'DataFrame'
    ]
)


## --- DATA VISUALIZATION
data = pd.read_csv('./data/data_after_ml.csv')

with st.container():
    with tab1:
        st.bar_chart(data['titleSentiment'].value_counts())
    with tab2:
        st.bar_chart(data['factScore'].value_counts().sort_index())
    with tab3:
        author_scores = data.groupby('author')['factScore'].mean()
        sorted_authors = author_scores.sort_values(ascending=False)
        top_15 = sorted_authors.head(15)
        st.bar_chart(top_15)
    with tab4:
        st.bar_chart(data['mainTopic'].value_counts().sort_values(ascending=False).head(15))
    with tab5:
        st.dataframe(
            data,
            hide_index=True
        )


## --- CONCLUSIONS
st.markdown(
    '''
    7. :blue-background[Conclusiones]
    
        * La polarización política generó un conflicto de información en Colombia, el cual debe ser combatido haciendo uso de la tecnología actual, para mejorar la capacidad de discernimiento de las futuras generaciones.
        * Se obtuvo información crucial para desarrollar esta herramienta gracias a la experimentación realizada, encontrando una mayor eficiencia en modelos como GPT-4o-mini.
        * Se observó que a medida que aumentan los temas de conversación sobre aspectos negativos, también lo hace la calidad de los hechos, lo cual puede deberse en gran medida a la manera en que se consume la información actualmente, reduciendo la veracidad por incrementar el tráfico de visualizaciones.
    
    '''
)
    
    
## --- DOCUMENTATION
st.header('Documentación del proyecto', anchor=False)
st.markdown(
    '''
    La documentación completa del proyecto puede ser encontrada en el [repositorio de GitHub](https://github.com/eedx/StreamlitNews), y los Notebooks empleados fueron los siguientes:
    
    - [Primera entrega](https://colab.research.google.com/drive/1LGyeJ74Oy1ixMHJuTEv-tgegAuyHmx1h?usp=sharing), pasos 1 - 3
    - [Segunda entrega](https://colab.research.google.com/drive/17rvpBJ_ByemVUQGadFEOsocVnnjgHURL?usp=sharing), pasos 4 - 7
    '''
)
