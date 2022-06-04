# watch-your-neck
당신의 거북목을 잡아드립니다. 


### dependencies
본 프로젝트는 `pyenv` 가상환경을 사용합니다. pyenv를 사용하지 않을 경우 별도의 가상환경을 설치하시기 바랍니다.

```bash
python==3.7.13
Django==3.2.13
django-pwa==1.0.10
pip==22.0.4
```

의존성 패키지 변경 시 아래 명령어로 requirements 를 업데이트 해주세요.
```bash
# 버전만 포함하도록 requirements 생성
pip list --format=freeze > requirements.txt
```