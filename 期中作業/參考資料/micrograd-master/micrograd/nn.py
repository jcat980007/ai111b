import random
from micrograd.engine import Value

class Module:
    """
    所有模組的基礎類別
    """

    def zero_grad(self):
        """
        將所有參數的梯度設置為0
        """
        for p in self.parameters():
            p.grad = 0

    def parameters(self):
        """
        返回模組的參數列表
        """
        return []

class Neuron(Module):
    """
    單個神經元類別
    """

    def __init__(self, nin, nonlin=True):
        """
        初始化神經元
        :param nin: 輸入的特徵數量
        :param nonlin: 是否使用非線性激活函數（ReLU）
        """
        self.w = [Value(random.uniform(-1,1)) for _ in range(nin)]  # 權重列表
        self.b = Value(0)  # 偏差項
        self.nonlin = nonlin  # 是否使用非線性激活函數

    def __call__(self, x):
        """
        執行神經元的順向傳播
        :param x: 輸入特徵
        :return: 神經元的輸出
        """
        act = sum((wi*xi for wi,xi in zip(self.w, x)), self.b)  # 加權輸入的總和
        return act.relu() if self.nonlin else act  # 如果需要非線性激活，則應用ReLU函數

    def parameters(self):
        """
        返回神經元的參數列表（權重和偏差項）
        """
        return self.w + [self.b]

    def __repr__(self):
        """
        返回神經元的文字描述
        """
        return f"{'ReLU' if self.nonlin else 'Linear'}Neuron({len(self.w)})"

class Layer(Module):
    """
    神經元層類別
    """

    def __init__(self, nin, nout, **kwargs):
        """
        初始化神經元層
        :param nin: 輸入的特徵數量
        :param nout: 輸出的特徵數量（神經元數量）
        :param kwargs: 其他參數（例如是否使用非線性激活函數）
        """
        self.neurons = [Neuron(nin, **kwargs) for _ in range(nout)]  # 神經元列表

    def __call__(self, x):
        """
        執行神經元層的順向傳播
        :param x: 輸入特徵
        :return: 神經元層的輸出
        """
        out = [n(x) for n in self.neurons]  # 將輸入傳遞給每個神經元並收集其輸出
        return out[0] if len(out) == 1 else out

    def parameters(self):
        """
        返回神經元層的參數列表（所有神經元的參數）
        """
        return [p for n in self.neurons for p in n.parameters()]

    def __repr__(self):
        """
        返回神經元層的文字描述
        """
        return f"Layer of [{', '.join(str(n) for n in self.neurons)}]"

class MLP(Module):
    """
    多層感知機類別
    """

    def __init__(self, nin, nouts):
        """
        初始化多層感知機
        :param nin: 輸入的特徵數量
        :param nouts: 輸出的特徵數量列表（每層神經元數量）
        """
        sz = [nin] + nouts
        self.layers = [Layer(sz[i], sz[i+1], nonlin=i!=len(nouts)-1) for i in range(len(nouts))]  # 層列表

    def __call__(self, x):
        """
        執行多層感知機的順向傳播
        :param x: 輸入特徵
        :return: 多層感知機的輸出
        """
        for layer in self.layers:
            x = layer(x)  # 順向傳播輸入
        return x

    def parameters(self):
        """
        返回多層感知機的參數列表（所有層的參數）
        """
        return [p for layer in self.layers for p in layer.parameters()]

    def __repr__(self):
        """
        返回多層感知機的文字描述
        """
        return f"MLP of [{', '.join(str(layer) for layer in self.layers)}]"
