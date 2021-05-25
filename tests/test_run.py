from run import read_description_directory
import os

def test_read_description_directory():
    test_description_directory = os.path.join(
        os.path.expanduser('~'),
        'Documents/'
        'google_class/'
        'project_8/'
        'tests/'
        'test_data/'
        'read_data'
    )
    test_dic = [{'name': 'Avocado',
                 'weight': 200,
                 'description': 'Avocado contains large amount of oleic acid, '
                                'a type of monounsaturated fat that can replace '
                                'saturated fat in the diet, which is very '
                                'effective in reducing cholesterol levels. '
                                'Avocado is also high in fiber. Its soluble '
                                'fiber can remove excess cholesterol from the '
                                'body, while its insoluble fiber helps keep '
                                'the digestive system functioning and prevent '
                                'constipation.',
                 'image_name': '002.jpeg'},
                {'name': 'Apple',
                 'weight': 500,
                 'description': 'Apple is one of the most nutritious and '
                                'healthiest fruits. It is very rich in '
                                'antioxidants and dietary fiber. Moderate '
                                'consumption can not only increase satiety, '
                                'but also help promote bowel movements. '
                                'Apple also contains minerals such as '
                                'calcium and magnesium, which can help prevent '
                                'and delay bone loss and maintain bone health. '
                                'It is good for young and old.\xa0 ',
                 'image_name': '001.jpeg'}]

    dic = read_description_directory(test_description_directory)
    assert (dic == test_dic)