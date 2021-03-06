from setuptools import setup

setup(name='NNFlow',
      version='0.1.9',
      description='NNFlow framework to convert ROOT files to Tensorflow models',
      url='https://github.com/kit-cn-cms/NNFlow',
      author='KIT CN CMS team: Maximilian Welsch, Marco A. Harrendorf',
      author_email='flyingcircus@example.com',
      packages=['NNFlow'],
      install_requires=[
          'matplotlib',
          'root-numpy',
          'tensorflow-gpu>=0.11.0*',
          'queuelib',
          'scikit-learn>=0.18.2',
          'graphviz>=0.7.1'
      ],
      zip_safe=True)
