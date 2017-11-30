#!/usr/bin/python3
# -*- coding : utf-8

from sklearn.linear_model import LogisticRegression
from sklearn import metrics

class DelayTime():
    '''
        Fazer os cálculos de acréssimo de tempo na rota utilizando
        Regressão Logistíca
    '''
    def __init__(self, rota):
        self.rota = rota
        self.model = LogisticRegression()

    def treinar(self):
        '''
            Treinar o algoritmo
        '''
        dataset = self.__get_dataset()
        self.model.fit(dataset['data'], dataset['target'])

    def __get_dataset(self):
        '''
            Ler o arquivo necessário da base de dados
        '''
        dataset = {'data' : [], 'target': []}
        with open('./dataset/'+ self.rota +'.csv','r') as data:
            for line in data.readlines():
                aux = [int(value) for value in line.replace('\n','').split(',')]
                dataset['data'].append(aux[:-1])
                dataset['target'].append(aux[-1])

        return dataset

    def prever(self, dia, hora, fluxo):
        '''
            Fazer a previsão com o algoritmo já treinado
        '''
        # data = self.__get_dataset()
        # previsto = self.model.predict(data['data'])
        # print(metrics.classification_report(data['target'], previsto))
        # print(metrics.confusion_matrix(data['target'], previsto))

        return self.model.predict([[dia, hora, fluxo]])[0]

    def __repr__(self):
        return "Rota: " + self.rota

if __name__ == "__main__":
    dt = DelayTime('1')
    dt.treinar()
    print(dt.prever(4,5,3))
