
import numpy as np
# 该模块为自定义模块，封装了构建决策树的基本方法
from CART import *
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
# 树的棵数
n_estimators = 10
# 列抽样最大特征数
max_features = 15
# 生成模拟二分类数据集
X, y = make_classification(n_samples=1000, n_features=20, n_redundant=0, n_informative=2,
                           random_state=1, n_clusters_per_class=1)
rng = np.random.RandomState(2)
X += 2 * rng.uniform(size=X.shape)
# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

class RandomForest():
    def __init__(self, n_estimators=100, min_samples_split=2, min_gain=0,
                 max_depth=float("inf"), max_features=None):
        # 树的棵树
        self.n_estimators = n_estimators
        # 树最小分裂样本数
        self.min_samples_split = min_samples_split
        # 最小增益
        self.min_gain = min_gain
        # 树最大深度
        self.max_depth = max_depth
        # 所使用最大特征数
        self.max_features = max_features

        self.trees = []
        # 基于决策树构建森林
        for _ in range(self.n_estimators):
            tree = ClassificationTree(min_samples_split=self.min_samples_split, min_impurity=self.min_gain,
                                      max_depth=self.max_depth)
            self.trees.append(tree)
            
    # 自助抽样
    def bootstrap_sampling(self, X, y):
        X_y = np.concatenate([X, y.reshape(-1,1)], axis=1)
        np.random.shuffle(X_y)
        n_samples = X.shape[0]
        sampling_subsets = []

        for _ in range(self.n_estimators):
            # 第一个随机性，行抽样
            idx1 = np.random.choice(n_samples, n_samples, replace=True)
            bootstrap_Xy = X_y[idx1, :]
            bootstrap_X = bootstrap_Xy[:, :-1]
            bootstrap_y = bootstrap_Xy[:, -1]
            sampling_subsets.append([bootstrap_X, bootstrap_y])
        return sampling_subsets
            
    # 随机森林训练
    def fit(self, X, y):
        # 对森林中每棵树训练一个双随机抽样子集
        sub_sets = self.bootstrap_sampling(X, y)
        n_features = X.shape[1]
        # 设置max_feature
        if self.max_features == None:
            self.max_features = int(np.sqrt(n_features))
        
        for i in range(self.n_estimators):
            # 第二个随机性，列抽样
            sub_X, sub_y = sub_sets[i]
            idx2 = np.random.choice(n_features, self.max_features, replace=True)
            sub_X = sub_X[:, idx2]
            self.trees[i].fit(sub_X, sub_y)
            # 保存每次列抽样的列索引，方便预测时每棵树调用
            self.trees[i].feature_indices = idx2
            print('The {}th tree is trained done...'.format(i+1))
    
    # 随机森林预测
    def predict(self, X):
        y_preds = []
        for i in range(self.n_estimators):
            idx = self.trees[i].feature_indices
            sub_X = X[:, idx]
            y_pred = self.trees[i].predict(sub_X)
            y_preds.append(y_pred)
            
        y_preds = np.array(y_preds).T
        res = []
        for j in y_preds:
            res.append(np.bincount(j.astype('int')).argmax())
        return res

rf = RandomForest(n_estimators=10, max_features=15)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print(accuracy_score(y_test, y_pred))



