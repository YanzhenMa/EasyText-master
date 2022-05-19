import os
import re
import warnings
from typing import Dict, List, Tuple, Union

from paddlenlp import Taskflow


class NLPModelBase:

    def __init__(self, model_name, **kwargs):

        self.model_name = model_name
        self._model = None
        self.kwargs = kwargs

        # 初始化模型
        self._model_init(self.model_name, **kwargs)

    def _model_init(self, model_name, **kwargs):

        init_flag = os.getenv(model_name)
        if int(init_flag):
            self._model = Taskflow(model_name, **kwargs)

    @property
    def model(self):
        if self._model is None:
            raise RuntimeError(f'未启用模型: {self.model_name}')
        return self._model

    def parse(self, text: str):
        '''解析数据
        '''
        result = self.model(text)
        return result


class Nlp:

    def __init__(self):

        # 模型实例
        self._models = {}

    def register_model(self, nlp_model: NLPModelBase):
        '''注册模型，如果注册的模型已存在，新模型会覆盖原有模型

        Args:
            nlp_model (NLPModelBase): 模型实例
        '''
        model = nlp_model()
        if isinstance(model, NLPModelBase):
            self._models[model.model_name] = model

    def get_model(self, model_name: str):
        '''获取模型对象

        Args:
            model_name (str): 模型名字
        '''
        model = self._models.get(model_name)
        if not model:
            raise RuntimeError(f'未注册的模型：{model_name}')
        return model

    def split(self, text: str) -> List[str]:
        '''分句

        Args:
            text (str): 文本
        '''
        sentences = re.split(r'(\.|\!|\?|。|！|？|\.{6})', text)
        result = []
        for i in range(int(len(sentences)/2)):
            sent = sentences[2*i].strip() + sentences[2*i + 1].strip()
            result.append(sent)
        if not result:
            result = [text]
        return result

    def seg(self, text: str, auto_split=True) -> Union[List[str], List[List[str]]]:
        '''分词

        Args:
            text (str): 文本
            auto_split (bool): 是否自动分句，默认为True
        '''
        # 获取分词模型
        seg_model: WordSegmentation = self.get_model('word_segmentation')
        # 分句判断
        if auto_split:
            text = self.split(text)
        # 忽略警告信息
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            # 分词
            seg_result = seg_model.parse(text)
        # 分词结果清洗
        result = []
        for sr in seg_result:
            if not isinstance(sr, list):
                sr = sr.strip()
                if sr:
                    result.append(sr)
                continue
            cache_list = []
            for w in sr:
                w = w.strip()
                if w:
                    cache_list.append(w)
            if cache_list:
                result.append(cache_list)
        return result

    def tag(self, text: str, auto_split=True) -> Union[List[Tuple[str, str]], List[List[Tuple[str, str]]]]:
        '''词性标注

        所使用的词性标注工具：https://github.com/baidu/lac

        Args:
            text (str): 文本
            auto_split (bool): 是否自动分句，默认为True
        '''
        # 获取词性标注模型
        tag_model: PosTagging = self.get_model('pos_tagging')
        # 分句判断
        if auto_split:
            text = self.split(text)
        # 忽略警告信息
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            # 词性标注
            tag_result = tag_model.parse(text)
        # 词性标注结果清洗
        result = []
        for tr in tag_result:
            if not isinstance(tr, list):
                if tr[0].strip():
                    result.append(tr)
                continue
            cache_list = []
            for w in tr:
                if w[0].strip():
                    cache_list.append(w)
            if cache_list:
                result.append(cache_list)
        return result

    def ner(self, text: str, auto_split=True) -> Union[List[Tuple[str, str]], List[List[Tuple[str, str]]]]:
        '''命名实体识别

        所使用的词性标注工具：https://github.com/baidu/lac

        Args:
            text (str): 文本
            auto_split (bool): 是否自动分句，默认为True
        '''
        # 获取命名实体识别模型
        ner_model: Ner = self.get_model('ner')
        # 分句判断
        if auto_split:
            text = self.split(text)
        # 忽略警告信息
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            # 命名实体识别
            ner_result = ner_model.parse(text)
        # 命名实体识别结果数据清洗
        result = []
        for nr in ner_result:
            if not isinstance(nr, list):
                if nr[0].strip():
                    result.append(nr)
                continue
            cache_list = []
            for w in nr:
                if w[0].strip():
                    cache_list.append(w)
            if cache_list:
                result.append(cache_list)
        return result

    def ddp(self, text: str, auto_split=True) -> List[Dict[str, List[str or int]]]:
        '''依存句法分析

        所使用的依存句法分析工具：https://github.com/baidu/DDParser
        安装命令： pip install LAC --upgrade

        Args:
            text (str): 文本
            auto_split (bool): 是否自动分句，默认为True
        '''
        # 获取依存句法分析模型
        ddp_model: DependencyParsing = self.get_model('dependency_parsing')
        # 分句判断
        if auto_split:
            text = self.split(text)
        else:
            text = text.strip().replace(' ', '').replace('\n', '').replace('\r', '')
        # 忽略警告信息
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            ddp_result = None
            if text:
                ddp_result = ddp_model.parse(text)
        return ddp_result

    def ddp_show(self, text: str, auto_split=True):
        '''依存句法分析可视化

        所使用的依存句法分析工具：https://github.com/baidu/DDParser
        安装命令： pip install LAC --upgrade

        Args:
            text (str): 文本
            auto_split (bool): 是否自动分句，默认为True
        '''
        # TODO：
        pass

    def text_correction(self, text: str, auto_split=True) -> Union[List[Tuple[str, str]], List[List[Tuple[str, str]]]]:
        '''文本纠错
        所使用的模型：https://github.com/PaddlePaddle/PaddleNLP/blob/develop/docs/model_zoo/taskflow.md
        Args:
            text (str): 文本
            auto_split (bool): 是否自动分句，默认为True
        '''
        # 获取文本纠错模型
        correction_model: TextCorrection = self.get_model('text_correction')
        # 分句判断
        if auto_split:
            text = self.split(text)
        else:
            text = text.strip().replace(' ', '').replace('\n', '').replace('\r', '')
        # 忽略警告信息
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
        correction_result = None
        if text:
            correction_result = correction_model.parse(text)
        return correction_result

    def text_similarity(self, sentence1, sentence2) -> List[Dict[str, str]]:
        '''判断两句话的相似度
        所使用的模型：https://github.com/PaddlePaddle/PaddleNLP/blob/develop/docs/model_zoo/taskflow.md

        Args:
            sentence1 (str): 文本
            sentence2 (str): 文本
        '''
        # 获取相似度计算模型
        similarity_model: TextSimilarity = self.get_model('text_similarity')
        # 忽略警告信息
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
        similarity_result = None
        if sentence1 and sentence2:
            data = [[sentence1, sentence2]]
            similarity_result = similarity_model.parse(
                data)
        return similarity_result

    def sentiment_analysis(self, text: str, auto_split=True) -> Union[List[Tuple[str, str]], List[List[Tuple[str, str]]]]:
        '''情感分析
        所使用的模型：https://github.com/PaddlePaddle/PaddleNLP/blob/develop/docs/model_zoo/taskflow.md
        '''
        # 获取情感分析模型
        sentiment_model: Ner = self.get_model('sentiment_analysis')
        # 分句判断
        if auto_split:
            text = self.split(text)
        # 忽略警告信息
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
        sentiment_result = None
        if text:
            sentiment_result = sentiment_model.parse(text)
        return sentiment_result

    def question_answering(self, text: str or list) -> List[Dict[str, str]]:
        '''生成式问答
        所使用的模型：https://github.com/PaddlePaddle/PaddleNLP/blob/develop/docs/model_zoo/taskflow.md

        Args:
            text(str): 文本
        '''
        # 获取回答模型
        question_model: Question = self.get_model('question_answering')
        # 忽略警告信息
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
        question_result = None
        if text:
            question_result = question_model.parse(text)
        return question_result

    def poetry(self, text: str or list) -> List[Dict[str, str]]:
        '''智能写诗
        所使用的模型：https://github.com/PaddlePaddle/PaddleNLP/blob/develop/docs/model_zoo/taskflow.md

        Args:
            text(str): 文本
        '''
        # 获取写诗模型
        poetry_model: Poetry = self.get_model('poetry_generation')
        # 忽略警告信息
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
        poetry_result = None
        if text:
            poetry_result = poetry_model.parse(text)
        return poetry_result

    def dialogue(self, text: list) -> List:
        '''开放对话
        所使用的模型：https://github.com/PaddlePaddle/PaddleNLP/blob/develop/docs/model_zoo/taskflow.md

        Args:
            text(str): 列表型文本
        '''
        # 获取写诗模型
        dialogue_model: Dialogue = self.get_model('dialogue')
        # 忽略警告信息
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
        dialogue_result = None
        if text:
            dialogue_result = dialogue_model.parse(text)
        return dialogue_result


class WordSegmentation(NLPModelBase):

    def __init__(self):
        # 添加停用词失败 don't knwo why
        # data = {
        #     'user_dict': 'E:/eachina/easytext/Text/data/原始文件/停用词/自定义停用词表.txt'}
        # super().__init__('word_segmentation', **data)
        super().__init__('word_segmentation')


class PosTagging(NLPModelBase):

    def __init__(self):
        super().__init__('pos_tagging')


class Ner(NLPModelBase):

    def __init__(self):
        super().__init__('ner')


class DependencyParsing(NLPModelBase):

    def __init__(self):
        super().__init__('dependency_parsing')


class TextCorrection(NLPModelBase):

    def __init__(self):
        super().__init__('text_correction')


class TextSimilarity(NLPModelBase):

    def __init__(self):
        super().__init__('text_similarity')


class SentimentAnalysis(NLPModelBase):

    def __init__(self):
        super().__init__('sentiment_analysis')


class Question(NLPModelBase):

    def __init__(self):
        super().__init__('question_answering')


class Poetry(NLPModelBase):

    def __init__(self):
        super().__init__('poetry_generation')


class Dialogue(NLPModelBase):

    def __init__(self):
        super().__init__('dialogue')


nlp = Nlp()
nlp.register_model(WordSegmentation)
nlp.register_model(PosTagging)
nlp.register_model(Ner)
nlp.register_model(DependencyParsing)
nlp.register_model(TextCorrection)
nlp.register_model(TextSimilarity)
nlp.register_model(SentimentAnalysis)
nlp.register_model(Question)
nlp.register_model(Poetry)
nlp.register_model(Dialogue)
