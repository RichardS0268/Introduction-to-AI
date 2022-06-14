import numpy as np
import pandas as pd
from cvxopt import matrix, solvers

# 实现线性可分支持向量机
# 硬间隔最大化策略
class Hard_Margin_SVM:
    # 线性可分支持向量机拟合方法
    def fit(self, X, y):
        # 训练样本数和特征数
        m, n = X.shape

        # 初始化二次规划相关变量：P/q/G/h
        self.P = matrix(np.identity(n + 1, dtype=np.float))
        self.q = matrix(np.zeros((n + 1,), dtype=np.float))
        self.G = matrix(np.zeros((m, n + 1), dtype=np.float))
        self.h = -matrix(np.ones((m,), dtype=np.float))

        # 将数据转为变量
        self.P[0, 0] = 0
        for i in range(m):
            self.G[i, 0] = -y[i]
            self.G[i, 1:] = -X[i, :] * y[i]
        
        # 构建二次规划求解
        sol = solvers.qp(self.P, self.q, self.G, self.h)

        # 对权重和偏置寻优
        self.w = np.zeros(n,) 
        self.b = sol['x'][0] 
        for i in range(1, n + 1):
            self.w[i - 1] = sol['x'][i]
        return self.w, self.b

    # 定义模型预测函数
    def predict(self, X):
        return np.sign(np.dot(self.w, X.T) + self.b)


# 定义近似线性可分支持向量机
# 软间隔最大化策略
class Soft_Margin_SVM:
    # 定义基本参数
    def __init__(self, kernel=linear_kernel, C=None):
        # 软间隔svm核函数，默认为线性核函数
        self.kernel = kernel
        # 惩罚参数
        self.C = C
        if self.C is not None: 
            self.C = float(self.C)
    
    # 定义线性支持向量机拟合方法
    def fit(self, X, y):
        # 训练样本数和特征数
        m, n = X.shape
        
        # 基于线性核计算Gram矩阵
        K = self._gram_matrix(X)
                
        # 初始化二次规划相关变量：P/q/G/h
        P = matrix(np.outer(y,y) * K)
        q = matrix(np.ones(m) * -1)
        A = matrix(y, (1, m))
        b = matrix(0.0)
        
        # 未设置惩罚参数时的G和h矩阵
        if self.C is None:
            G = matrix(np.diag(np.ones(m) * -1))
            h = matrix(np.zeros(m))
        # 设置惩罚参数时的G和h矩阵
        else:
            tmp1 = np.diag(np.ones(m) * -1)
            tmp2 = np.identity(m)
            G = matrix(np.vstack((tmp1, tmp2)))
            tmp1 = np.zeros(m)
            tmp2 = np.ones(m) * self.C
            h = matrix(np.hstack((tmp1, tmp2)))

        # 构建二次规划求解
        sol = solvers.qp(P, q, G, h, A, b)
        # 拉格朗日乘子
        a = np.ravel(sol['x'])

        # 寻找支持向量
        spv = a > 1e-5
        ix = np.arange(len(a))[spv]
        self.a = a[spv]
        self.spv = X[spv]
        self.spv_y = y[spv]
        print('{0} support vectors out of {1} points'.format(len(self.a), m))

        # 截距向量
        self.b = 0
        for i in range(len(self.a)):
            self.b += self.spv_y[i]
            self.b -= np.sum(self.a * self.spv_y * K[ix[i], spv])
        self.b /= len(self.a)

        # 权重向量
        self.w = np.zeros(n,)
        for i in range(len(self.a)):
            self.w += self.a[i] * self.spv_y[i] * self.spv[i]

    # 定义Gram矩阵计算函数
    def _gram_matrix(self, X):
        m, n = X.shape
        K = np.zeros((m, m))
        # 遍历计算Gram矩阵
        for i in range(m):
            for j in range(m):
                K[i,j] = self.kernel(X[i], X[j])
        return K
    
    # 定义映射函数
    def project(self, X):
        if self.w is not None:
            return np.dot(X, self.w) + self.b
    
    # 定义模型预测函数
    def predict(self, X):
        return np.sign(np.dot(self.w, X.T) + self.b)


# 定义高斯核函数
def gaussian_kernel(x1, x2, sigma=5.0):
    return np.exp(-1 * np.linalg.norm(x1-x2)**2 / (2 * (sigma ** 2)))

# 定义线性不可分支持向量机
# 借助于高斯核函数转化为线性可分的情形
class Non_Linear_SVM:
    # 定义基本参数
    def __init__(self, kernel=gaussian_kernel):
        # 非线性可分svm核函数，默认为高斯核函数
        self.kernel = kernel
    
    # 定义非线性可分支持向量机拟合方法
    def fit(self, X, y):
        # 训练样本数和特征数
        m, n = X.shape
        
        # 基于线性核计算Gram矩阵
        K = self._gram_matrix(X)
                
        # 初始化二次规划相关变量：P/q/A/b/G/h
        P = matrix(np.outer(y,y) * K)
        q = matrix(np.ones(m) * -1)
        A = matrix(y, (1, m))
        b = matrix(0.0)
        G = matrix(np.diag(np.ones(m) * -1))
        h = matrix(np.zeros(m))

        # 构建二次规划求解
        sol = solvers.qp(P, q, G, h, A, b)
        # 拉格朗日乘子
        a = np.ravel(sol['x'])

        # 寻找支持向量
        spv = a > 1e-5
        ix = np.arange(len(a))[spv]
        self.a = a[spv]
        self.spv = X[spv]
        self.spv_y = y[spv]
        print('{0} support vectors out of {1} points'.format(len(self.a), m))

        # 截距向量
        self.b = 0
        for i in range(len(self.a)):
            self.b += self.spv_y[i]
            self.b -= np.sum(self.a * self.spv_y * K[ix[i], spv])
        self.b /= len(self.a)

        # 权重向量
        self.w = None

    # 定义Gram矩阵计算函数
    def _gram_matrix(self, X):
        m, n = X.shape
        K = np.zeros((m, m))
        # 遍历计算Gram矩阵
        for i in range(m):
            for j in range(m):
                K[i,j] = self.kernel(X[i], X[j])
        return K
    
    # 定义映射函数
    def project(self, X):
        y_pred = np.zeros(len(X))
        for i in range(X.shape[0]):
            s = 0
            for a, spv_y, spv in zip(self.a, self.spv_y, self.spv):
                s += a * spv_y * self.kernel(X[i], spv)
            y_pred[i] = s
        return y_pred + self.b
    
    # 定义模型预测函数
    def predict(self, X):
        return np.sign(self.project(X))