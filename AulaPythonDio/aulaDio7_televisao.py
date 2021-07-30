class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1


if __name__ == '__main__':
    televisao = Televisao()
    print('TV LIGADA {}'.format(televisao.ligada))
    televisao.power()
    print('TV LIGADA {}'.format(televisao.ligada))
    televisao.power()
    print('TV LIGADA {}'.format(televisao.ligada))
    televisao.power()
    print('CANAL + {}'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('CANAL - {}'.format(televisao.canal))
    print('CANAL - {}'.format(televisao.canal))
    televisao.diminui_canal()
    televisao.diminui_canal()
    televisao.diminui_canal()
    print('CANAL - {}'.format(televisao.canal))