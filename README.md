# Proyecto del sprint 7

- Este repositorio esta enfocado en desarrollar e implementar en [Render](https://render.com/) el proyecto 7.
- La URL de donde esta alojado el Deploy es [tt-render.onrender.com](https://tt-render.onrender.com/)
- Las dependencias estan especificados en [requierements.txt](/requirements.txt)
  - El proyecto esta construido en [Streamlit](https://streamlit.io/)
  - Las graficas estan generadas con [Plotty](https://plotly.com/)
  - El analisis y manipulacion de datos es con la libreria [Pandas](https://pandas.pydata.org/)
  - Los datos estan en [ubicados](../Data/afluenciastc_desglosado_10_2024.csv)

- Los datos fueron obtenidos de la [pagina oficial](https://datos.cdmx.gob.mx/dataset/afluencia-diaria-del-metro-cdmx) de la CDMX
- Se generó un modulo personalizado para la correccion de datos

- La estructura es la siguiente:

```bash
$tree

├── README.md
├── app.py
├── lib.py
├── .gitignore
├── requirements.txt
└── notebooks
    └── EDA.ipynb
└── Data
    ── afluenciastc_desglosado_10_2024.csv
└── .streamlit
    └── config.toml
```
