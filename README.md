# 0. 목차
[1.목표와 기능](#1-목표와-기능)<br>
[2.개발 환경 ](#2-개발-환경)<br>
[3.프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)<br>
[4.UI 설계](#4-UI-설계)<br>
[5.DB 모델링](#5-DB-모델링)<br>
[6.메인 기능](#6-메인-기능)<br>
[7.추가 기능](#7-추가-기능)<br>
[8.느낀점](#8-느낀점)<br>

## 1. 목표와 기능
### 1-1. 목표
- 영화에 대한 견해를 나눌 수 있는 블로그
- 영화 추천이 가능한 블로그
- 최신 영화 소식을 접할 수 있는 블로그
### 1-2. 기능
- CRUD가 가능한 게시판
- ChatGPT API를 활용한 영화 추천을 받을 수 있는 블로그
- 회원가입, 로그인, 로그아웃 기능
- 로그인한 사용자에게만 CUD 기능 권한
- 게시글에 대한 댓글 등록(로그인한 사용자만 가능)

## 2. 개발 환경 
### 2-1. 개발환경

![image](https://github.com/jkhwang150/ormi_miniproject_blog/assets/75780140/5e05abc7-cca2-4a01-a963-538f37d87e4c)

 
## 3. 프로젝트 구조와 개발 일정
### 3-1. 프로젝트 구조

![image](https://github.com/jkhwang150/ormi_miniproject_blog/assets/75780140/5c840e67-14cd-49e2-84e8-99f3c481408e)

### 3-2. 일정
![일정 1](https://github.com/jkhwang150/ormi_miniproject_blog/assets/75780140/34bcf810-4928-4f48-85b0-1c320b12b041)
### Notion Address
https://www.notion.so/1f1872ff265b464c988e90501f039ee1 

## 4. UI 설계
![image](https://github.com/jkhwang150/ormi_miniproject_blog/assets/75780140/80fc0a81-d200-415a-a9f0-8a016507a50f)


## 5. DB 모델링
![image](https://github.com/jkhwang150/ormi_miniproject_blog/assets/75780140/4ab75449-2030-4a7c-b71a-0f4c3294b2d5)

## 6. 메인 기능
1. 회원 가입 및 로그인
![Accounts](https://github.com/jkhwang150/ormi_miniproject_blog/assets/75780140/9f6d6ee6-3ba3-40ce-b0a1-0ae361620f4f)

2. 게시판

![CRUD_LOGOUT](https://github.com/jkhwang150/ormi_miniproject_blog/assets/75780140/18eec2fc-b607-43e2-8993-d36c4bc06ec0)

![Logout](https://github.com/jkhwang150/ormi_miniproject_blog/assets/75780140/cd14f4d4-4b52-4bdd-9394-3ade8ac3965d)



## 7. 추가 기능
OpenAI API를 활용하여 영화 추천
![Recommand](https://github.com/jkhwang150/ormi_miniproject_blog/assets/75780140/d0f17868-ced2-49b4-a732-a19575e2772a)


## 8. 느낀점
1. 설계&기획
'영화'라는 소재를 가지고 수월하게 진행되었으며 하루 반나절만에 전체적으로 블로그를 구상하여 이를 문서화하는데 큰 어려움을 가지지 않아 기분좋게 프로젝트를 수행할 수 있었다.
2. MVT 모델
 3일차 부터는 Bootstrap과 JS, CSS를 이용하여 UI작업을 수행하였다. 이 또한 문제 없이 진행되었다. 하지만 Django 프로젝트를 만들고 이를 Template에 적용시켰을 때 수정해야하는 작업이 너무 많았다. Url 링크를 전부 바꾸어 주어야 했으면 데이터들의 id, name 등 Model에 맞게 form을 수정해야 했고 코드의 길이가 길고 많았던 만큼 빠트린 부분도 많고 실행이 안됬을 때도 많았으며 실행이 되더라도 url로 넘어가지 않는다던가 데이터가 저장되지 않는 등 다양한 문제에 직면하였다. 오류 페이지가 나와 어디서 오류가 발생했는지 찾으면 좋겠지만 아무 이상없이 실행은 되는데 데이터의 이동이 진행되지 않거나 기능이 수행되지 않는다면 간담이 서늘했다. 특히 DB에서 어려움을 겪었다. 외래키를 불러오면 데이터 Get되지 않았고 모델에 저장이 되지 않는 경우들이 많았다. 그래서 일정에 맞추기위해 크롤링을 통한 영화 정보 게시처럼 포기한 기능과 댓글입력과 같이 원하는대로 구현되지 않은 부분도 있어 너무 아쉬웠다. 시간을 많이 할애하고 구글링을 통해 다양한 사람들의 조언들으 참고했음에도 원하는 결과물에 도달하지 못한 나에게 자책도 많이했다.
3. 노력
 처음으로 직접 DB, UI, Function 등 모든 내용을 관리하며 연결해보았다. 위에 말한 것처럼 부족함도 많고 자책도 많이 했다. 하지만 CRUD나 OpenAI API를 통한 AI와의 대화기능 등 실제 동작하는 것을 보며 희열을 느낄 수 있었다. 이게 내가 구현한 거구나, 나도 할 수 있구나라는 위안을 주었고 프로젝트를 끝까지 달릴 수 있는 원동력이 될 수 있었습니다. 1만번의 법칙이라는 말이 있듯이 내가 부족한게 있으면 채우고 반복하여 다음 프로젝트에서는 원하는 결과물에 한 걸음 더 가까워질 수 있듯이 더 노력해야겠다고 생각했다.
