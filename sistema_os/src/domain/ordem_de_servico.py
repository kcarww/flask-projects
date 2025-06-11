class OrdemServico:
    def __init__(self, codigo, data, problema, solucao=None, status="Aberta"):
        self.codigo = codigo
        self.data = data
        self.problema = problema
        self.solucao = solucao
        self.status = status

    def __str__(self):
        return f"OrdemServico(codigo={self.codigo}, data='{self.data}', status='{self.status}')"