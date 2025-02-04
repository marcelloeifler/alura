from restaurante import Restaurante

def main():
    restaurante_praca= Restaurante("praça", "Gourmet")
    restaurante_praca.receber_avaliacao("Gui",4)
    restaurante_praca.receber_avaliacao("Lais",5)

    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()