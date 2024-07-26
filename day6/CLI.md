# CLI
- GUI (Grapic User Interface)
  - 그래픽(ex. 그림)으로 유저와 상호작용하는 접점

- CLI (Command Line Interface)
  - command line을 통해서 컴퓨터와 상호작용하는 접점
  - 터미널을 통해서!

> 왜? CLI를 써야하나요?
- 새폴더 생성할 때, 
  - GUI: 마우스 우클릭 -> 새로만들기 -> 폴더 선택 -> 'NEW' 폴더 선택
  - CLI: 터미널 켜서, 'mkdir new' 입력 (단계 최소화)
    cf. mkdir: make directory

# 경로
- 현재 내가 위치한 곳! 그 주소
1. 루트 디렉토리 (/)
   - 모든 파일과 폴더를 담고 있는 최상위의 폴더
   - C 드라이브!

2. 홈 디렉토리 (~)
   - 현재 로그인된 사용자의 홈폴더
   - C:/Users/alex
  
# 경로의 두 가지 종류
1. 절대경로: 절대적인 주소 ex. /c/Users/ADMIN/Desktop/파이썬
(루트디렉토리부터 목적지점을 모두 표현한 경로)

2. 상대경로: 현재 작업 디렉토리(working directory)를 기준으로 계산된 경로
   - . : 현재 작업하고 있는 폴더
   - .. : 현재 작업 폴더의 부모를 의미

# 터미널 명령어
1. 'touch': 파일을 생성하는 명령어 (여러개의 파일은 띄어쓰기로 구분)
   ex. touch new1.txt new2.txt

2. 'mkdir': make directory의 약자 -> 폴더를 만들어줌
   ex. mkdir 'hello world': 'hello'와 'world' 폴더를 따로 만들지 않게 하기 위한 코드

3. 'ls': list segments -> 현재 작업중인 디렉토리의 목록을 보여줌
   cf. ls -a: 숨긴 파일까지 모두 조회

4. 'mv': move의 약자 -> 파일을 폴더내로 이동시킴 & 파일명 변경
   ex. mv hello.py day6: hello 파일을 day6 폴더로 이동
   ex. mv new.txt day7: day7라는 폴더가 없는 경우, 파일명을 바꿔냄
   ex. mv hello.py ..: hello파일을 상위 폴더로 이동

5. 'cd': change directory의 약자 -> 현재의 위치를 변경
   ex. cd day6/
   cf. cd만 입력한 경우, '~'가 출력되어 홈폴더로 이동

6. 'pwd': print working directory -> 현재 나의 위치를 출력

7. 'rm': remove -> 폴더/파일을 (완전, 즉시 삭제) 지우는 명령어
   cf. rm -r: 폴더 속 파일을 하나하나 돌아가며 삭제해줘!
       rm *.txt: 텍스트 파일은 다 삭제해줘!