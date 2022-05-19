import unittest

from Text.base_trait.article import (
    adjacent_sentence_noun_overlap_avg, adjacent_sentence_noun_overlap_std,
    adjacent_sentence_reality_overlap_avg,
    adjacent_sentence_reality_overlap_std, adjacent_sentence_similarity_avg,
    adjacent_sentence_similarity_std, all_sentence_noun_overlap_avg,
    all_sentence_noun_overlap_std, all_sentence_reality_overlap_avg,
    all_sentence_reality_overlap_std, all_sentence_similarity_avg,
    all_sentence_similarity_std, get_sentiment)


class ArticleTest(unittest.TestCase):

    def setUp(self):

        self.text = '''近日，江苏扬州一所中学推行古诗词考试，引起了很多人的争论。在我看来，推行这样的古诗词考试利大于弊，但是我并不认同所谓的分等级规定。论证如下：首先，
                    我们知道，中华古典文化在经历了百年多的战乱之后，很多人已经不在认可它，反而追捧起西方文化，认为他们的文化更先进，更优秀。这正是一种缺乏文化自信的体现。
                    文化本无优劣之分，之人认为的划定罢了。况且，我从不认为流传了5000年也没有消失的文化是劣等文化。大文明古国，仅有我们的文化传承了下去，这难道还不足以说明问题么？
                    故而，提倡古诗词考试，能够引发青年学生们去了解，认识，甚至深入古典诗词文化。优秀的名篇佳作，可以培养人们的文化修养，提高自身的素质。读史明智，读诗则明理。
                    千年来幼儿启蒙的书籍，都以诗为载体，朗朗上口，发人深省。只有了解的人多了，有心智的人多了，我们才能更好的传承优秀的中华传统文化，甚至于向外表达我们的文化，真正做到文化自信。
                    但是，考试结果要把学生们分等级，我并不认同。人天生便是各不相同的。有的人擅长逻辑思维清晰，更加理性的科目，有的人则擅长比较感性的方面。
                    分等级考试，表面上看，好像是谁用功，谁不用功的体现，但是不同思维的差异，往往被大家忽略。那么，一部分认真学习了的同学因为思维与老师的，所谓标准答案的差异而没有得到好的等级，
                    被认为是不好好学习，这可能会损伤他们学习，感悟古诗词的积极性，不利于诗词文化的传播与传承。其次，诗词，在我看来不是定性的体验。
                    俗话说：“一千个读者，就有一千个哈姆莱特。”从不同的角度去看一首诗词，有的人感到的是惆怅，有的人却品出了丝丝乐观与豁达。
                    用一个人的体验，检验所有人的感受，非要分出是非黑白，有损古诗词的文化特质，也不能益于古诗词在今后世界的发展。
                    最后，当考试结果与一些非常重要的人生选择产生联系之后，有的人可能会滥用权柄，“帮助”那些得不到好成绩的同学们得到好的结果。
                    但这是所有人都不希望看到的现象。所以，我认为我们应该提倡古诗词考试，来促进后代对诗词的兴趣发展，而分等级与出发点相悖，并不可取。
                    '''
        # 处理空格和换行符
        self.text = self.text.replace(' ', '')
        self.text = self.text.replace('\n', '')

    def test_adjacent_sentence_noun_overlap_avg(self):
        """[相邻句子名词重叠平均数]
        """
        self.assertEqual(
            adjacent_sentence_noun_overlap_avg(self.text),
            0.6957
        )

    def test_adjacent_sentence_noun_overlap_std(self):
        """[相邻句子名词重叠标准差]
        """
        self.assertEqual(
            adjacent_sentence_noun_overlap_std(self.text),
            0.8041
        )

    def test_all_sentence_noun_overlap_avg(self):
        """[所有句子名词重叠平均数]
        """
        self.assertEqual(
            all_sentence_noun_overlap_avg(self.text),
            7.6667
        )

    def test_all_sentence_noun_overlap_std(self):
        """[所有句子名词重叠标准差]
        """
        self.assertEqual(
            all_sentence_noun_overlap_std(self.text),
            3.0064
        )

    def test_adjacent_sentence_reality_overlap_avg(self):
        """[相邻句子实词重叠平均数]
        """
        self.assertEqual(
            adjacent_sentence_reality_overlap_avg(self.text),
            0.913
        )

    def test_adjacent_sentence_reality_overlap_std(self):
        """[相邻句子实词重叠标准差]
        """
        self.assertEqual(
            adjacent_sentence_reality_overlap_std(self.text),
            1.0178
        )

    def test_all_sentence_reality_overlap_avg(self):
        """[所有句子实词重叠平均数]
        """
        self.assertEqual(
            all_sentence_reality_overlap_avg(self.text),
            12.625
        )

    def test_all_sentence_reality_overlap_std(self):
        """[所有句子实词重叠标准差]
        """
        self.assertEqual(
            all_sentence_reality_overlap_std(self.text),
            2.0936
        )

    def test_adjacent_sentence_similarity_avg(self):
        """[相邻句子相似度的平均数]
        """
        self.assertEqual(
            adjacent_sentence_similarity_avg(self.text),
            0.4388
        )

    def test_adjacent_sentence_similarity_std(self):
        """[相邻句子相似度的标准差]
        """
        self.assertEqual(
            adjacent_sentence_similarity_std(self.text),
            0.1219
        )

    def test_all_sentence_similarity_avg(self):
        """[所有句子相似度的平均数]
        """
        self.assertEqual(
            all_sentence_similarity_avg(self.text),
            4.613
        )

    def test_all_sentence_similarity_std(self):
        """[所有句子相似度的标准差]
        """
        self.assertEqual(
            all_sentence_similarity_std(self.text),
            0.1231
        )

    def test_get_sentiment(self):
        """[判断一段话是否积极]
        """
        self.assertEqual(
            get_sentiment(self.text),
            'neutral'
        )


if __name__ == '__main__':

    unittest.main()
