from uuid import UUID
from core.produto.application.use_cases.create_produto import CreateProdutoUseCase, CreateProdutoRequest
from core.produto.domain.produto import Produto
from core.produto.infra.in_memory_repository import InMemoryProdutoRepository

class TestCreateProduto:
    def test_can_create_produto(self):
        repository = InMemoryProdutoRepository()
        use_case = CreateProdutoUseCase(repository)
        request = CreateProdutoRequest(
            nome="Produto 1",
            preco=10.0,
            qtd_estoque=10
        )
        response = use_case.execute(request)
        assert response.nome == "Produto 1"
        assert response.preco == 10.0
        assert response.qtd_estoque == 10