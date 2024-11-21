from ui import show_menu, handle_unidades, handle_faturas, handle_taxas, handle_veiculos, handle_itens_fatura, handle_funcionarios, handle_ocorrencias, handle_visitantes, handle_moradores, handle_areas_comuns, handle_reservas, handle_autorizacoes, handle_contratos, handle_fornecedores, handle_servicos


# Menu principal
menu = show_menu()

if menu == "Áreas Comuns":
    handle_areas_comuns()
elif menu == "Autorização de Visitantes":
    handle_autorizacoes()
elif menu == "Contratos de Serviços":
    handle_contratos()
elif menu == "Faturas":
    handle_faturas()
elif menu == "Fornecedores":
    handle_fornecedores()
elif menu == "Funcionários":
    handle_funcionarios()
elif menu == "Itens da Fatura":
    handle_itens_fatura()
elif menu == "Moradores":
    handle_moradores()
elif menu == "Ocorrências":
    handle_ocorrencias()
elif menu == "Reservas de Áreas Comuns":
    handle_reservas()
elif menu == "Serviços":
    handle_servicos()
elif menu == "Taxas":
    handle_taxas()
elif menu == "Unidades":
    handle_unidades()
elif menu == "Veículos":
    handle_veiculos()
elif menu == "Visitantes":
    handle_visitantes()
