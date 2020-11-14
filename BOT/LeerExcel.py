import pandas as pd
import plotly.graph_objects as go


class LeerExcel:

    def leerExcelFuncion(self):
        data = pd.read_excel("./RecursoDatos.xlsx")
        fig = go.Figure(data=[go.Pie( labels= data["BANCO"], values=data["CLIENTES"])])
        fig.show()