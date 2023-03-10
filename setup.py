from setuptools import setup, find_packages

setup(
    name='deepke',  # 打包后的包文件名
    version='2.1.1',    #版本号
    keywords=["pip", "RE","NER","AE"],    # 关键字
    description='DeepKE 是基于 Pytorch 的深度学习中文关系抽取处理套件。',  # 说明
    long_description="client",  #详细说明
    license="MIT",  # 许可
    url='https://github.com/zjunlp/deepke',
    author='ZJUNLP',
    author_email='zhangningyu@zju.edu.cn',
    include_package_data=True,
    platforms="any",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        # 'torch>=1.5,<=1.11',
        # 'hydra-core==1.0.6',
        # 'matplotlib==3.4.1',
        # 'transformers==3.4.0',
        # 'jieba==0.42.1',
        # 'scikit-learn==0.24.1',
        # 'pytorch-transformers==1.2.0',
        # 'seqeval==1.2.2',
        # 'tqdm==4.60.0',
        # 'opt-einsum==3.3.0',
        # 'wandb==0.12.7',
        # "ujson",
        # "huggingface_hub==0.2.1",
        # "pytorch-crf==0.7.2",
        # "PyLD==2.0.3"
        'absl-py==1.0.0',
        'antlr4-python3-runtime==4.8',
        'beautifulsoup4==4.11.1',
        'bert4keras==0.7.7',
        'boto3==1.21.45',
        'botocore==1.24.45',
        'cachetools==4.2.4',
        'charset-normalizer==2.0.12',
        'click==8.1.2',
        'configparser==5.2.0',
        'cycler==0.11.0',
        'docker-pycreds==0.4.0',
        'filelock==3.6.0',
        'frozendict==2.3.2',
        'gdown==4.5.1',
        'gitdb==4.0.9',
        'gitpython==3.1.27',
        'google-auth==1.35.0',
        'google-auth-oauthlib==0.4.6',
        'grpcio==1.45.0',
        'huggingface-hub==0.2.1',
        'hydra-core==1.0.6',
        'importlib-metadata==4.11.3',
        'importlib-resources==5.7.1',
        'ipdb==0.13.9',
        'jieba==0.42.1',
        'jmespath==1.0.0',
        'joblib==1.1.0',
        'keras==2.9.0',
        'kiwisolver==1.4.2',
        'lxml==4.9.1',
        'markdown==3.3.6',
        'matplotlib==3.4.1',
        'nlpaug==1.1.11',
        'nlpcda==2.5.8',
        'nltk==3.7',
        'oauthlib==3.2.0',
        'omegaconf==2.0.6',
        'opt-einsum==3.3.0',
        'packaging==21.3',
        'pandas==1.4.3',
        'pathtools==0.1.2',
        'pillow==9.1.0',
        'promise==2.3',
        'protobuf==3.20.1',
        'pyasn1==0.4.8',
        'pyasn1-modules==0.2.8',
        'pyld==2.0.3',
        'pyparsing==3.0.8',
        'pytorch-crf==0.7.2',
        'pytorch-transformers==1.2.0',
        'pytz==2022.1',
        'pyyaml==6.0',
        'regex==2022.3.15',
        'requests==2.27.1',
        'requests-oauthlib==1.3.1',
        'rsa==4.8',
        's3transfer==0.5.2',
        'sacremoses==0.0.49',
        'scikit-learn==0.24.1',
        'scipy==1.8.0',
        'sentencepiece==0.1.91',
        'sentry-sdk==1.5.10',
        'seqeval==1.2.2',
        'setproctitle==1.2.3',
        'setuptools==59.5.0',
        'shortuuid==1.0.8',
        'smmap==5.0.0',
        'soupsieve==2.3.2.post1',
        'subprocess32==3.5.4',
        'tensorboard==2.4.1',
        'tensorboard-plugin-wit==1.8.1',
        'tensorboardx==2.5.1',
        'termcolor==1.1.0',
        'threadpoolctl==3.1.0',
        'tokenizers==0.9.2',
        'toml==0.10.2',
        'torch>=1.5,<=1.11',
        'tqdm==4.60.0',
        'transformers==3.4.0',
        'typing-extensions==4.2.0',
        'ujson==5.2.0',
        'wandb==0.12.7',
        'werkzeug==2.1.1',
        'wheel==0.37.1',
        'yaspin==2.1.0',
        'zipp==3.8.0',
    ], 
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
