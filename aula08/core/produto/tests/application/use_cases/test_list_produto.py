from core.produto.application.use_cases.list_produto import ListProdutoUseCase, ListProdutoRequest
from core.produto.infra.in_memory_repository import InMemoryProdutoRepository
from core.produto.domain.produto import Produto
from uuid import uuid4
class TestListProduto:
    def test_can_list_produto(self):
        id_gerado = uuid4()
        repository = InMemoryProdutoRepository(
            [
                Produto(
                    id=id_gerado,
                    nome="Produto 1",
                    preco=10.0,
                    qtd_estoque=10
                )
            ]
        )
        use_case = ListProdutoUseCase(repository)
        response = use_case.execute(ListProdutoRequest())
        assert repository.produtos[0].nome == response.data[0].nome