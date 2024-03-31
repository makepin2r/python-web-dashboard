# 개발 환경 셋팅

## poetry 설치
**poetry**는 파이썬의 가상환경 생성 및 라이브러리 의존성 관리를 도와줌.

```bash
# poetry 설치 명령어
curl -sSL https://install.python-poetry.org | python3 -
# 설치 확인
poetry --version
```
### TroubleShooting: poetry 명령어가 인식되지 않을 경우
추후 추가 예정.  
[해당 글](https://takeknowledge.tistory.com/145) 참고.

## 가상환경 활성화 및 실행
### 최초 활성화
```bash
# 최초 활성화
poetry init
```
위 명령어를 실행해 설정을 입력하고 나면 **pyproject.toml** 파일이 생성되며, 프로젝트에서 사용할 라이브러리 의존성 및 설정이 기록됨  (**package.json**같은 역할)  

### 가상환경 쉘 접속 (실행)
```bash
poetry shell
```

### 라이브러리 설치 방법
```bash
# 설치 명령어
poetry add [라이브러리 이름]
# 라이브러리 설치 그룹핑을 하고 싶을 때 (ex. 개발 환경)
poetry add --group dev [라이브러리 이름]
# 라이브러리 제거
poetry remove
```

### 라이브러리 동기화 
라이브러리 설치시, **pyproject.toml**과 더불어 **poetry.lock** 파일이 생성되어 라이브러리 의존성을 관리해준다.   
두 파일이 있을 경우 아래 명령어로 라이브러리 동기화 가능.
```bash
# 라이브러리 동기화
poetry install
```

## vscode 관련 가상환경 설정
### vscode에 가상환경 자동 실행
poetry를 이용해 생성한 가상환경을 vscode에 등록할 수 있다.  
아래 설정을 완료하면 `poetry shell`을 입력하지 않아도 커맨드를 열면 자동으로 가상환경이 실행된다.
1. 가상환경 경로를 확인 
    ```bash
    poetry env info
    ```
    위 명령어를 입력하여 나오는 가상환경 정보 중, 'Executable' 항목의 경로를 복사한다.  
  
2. 인터프리터 선택
vscode에서 명령어 팔레트를 연 다음, (`cmd + shift + p`)  
'Python: Select Interpreter'를 선택.  
목록에 뜨는 가상환경을 선택하거나, 원하는 가상환경이 없을 경우 'Enter interpreter path'를 선택해 1에서 확인한 경로를 붙여넣는다.

### lint 관련 설정
1. ruff  
파이썬에서 제시하는 PEP8 스타일 가이드에 맞춘 경고 및 자동 포맷팅 기능을 제공한다.  
파이썬 라이브러리와 vscode 익스텐션 설치가 모두 필요.
    - 라이브러리 설치
        ```bash
        # ruff 설치 명령어
        poetry add --group dev ruff
        ```
    - 'Ruff'[(링크 참고)](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) 설치

2. mypy
정적 타입 검사 도구.  
개발 환경에서 타입 오류를 미리 검사할 때 활용 가능.  
파이썬 라이브러리와 vscode 익스텐션 설치가 모두 필요.  
    - 라이브러리 설치
        ```bash
        # mypy 설치 명령어
        poetry add --group dev mypy
        ```
    - 'Mypy Type Checker'[(링크 참고)](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker) 설치

3. settings.json 파일로 vscode 내 프로젝트 설정 정의  
위의 라이브러리 동작을 위해서는 프로젝트 내 vscode setting을 설정해주어야 한다.  
    - 프로젝트 루트 경로에 `.vscode/settings.json` 파일을 생성해 아래 내용을 입력한다.
        ```json
        {
            "editor.formatOnSave": true,
            "python.analysis.typeCheckingMode": "off",
            "ruff.importStrategy": "fromEnvironment",
            "mypy-type-checker.importStrategy": "fromEnvironment"
        }
        ```
        - `"editor.formatOnSave": true`: 저장 시 자동 포맷팅
        - `"python.analysis.typeCheckingMode": "off"`: vscdoe 파이썬 익스텐션의 기본 타입 검사 off
        - `"ruff.importStrategy": "fromEnvironment"`: 가상환경 내 버전의 ruff 사용
        - `"mypy-type-checker.importStrategy": "fromEnvironment"`: 가상환경 내 버전의 mypy 사용

---
#### 레퍼런스
- [poetry를 활용한 가상환경 설치 관련](https://sjquant.tistory.com/93)
- [dash 관련해 공부하며 참고중인 글](https://abluesnake.tistory.com/152)