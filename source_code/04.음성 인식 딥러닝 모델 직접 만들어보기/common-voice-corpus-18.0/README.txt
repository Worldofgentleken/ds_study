Common Voice 데이터셋
이 리포지토리는 Common Voice 데이터셋의 릴리스 정보와 메타데이터를 포함하고 있습니다. 전체 데이터셋을 다운로드하려면 Common Voice 웹사이트를 방문하세요.

리포지토리 소개
이 리포지토리는 JSON 형식으로 각 데이터셋 릴리스에 대한 통계 정보를 포함하고 있으며, 릴리스 요약이 담긴 변경 로그(changelog)를 포함하고 있습니다. JSON 구조는 릴리스 간에 약간씩 변경될 수 있으므로, 비교 작업을 할 계획이라면 버전 간에 정규화(normalize)가 필요할 수 있습니다. 현재, 지난 1년 동안 릴리스된 데이터셋의 변경 로그와 통계 정보가 제공되며, 더 오래된 버전에 대한 정보도 추가할 예정입니다.

성별, 연령, 악센트 등의 인구 통계적 분류는 검증된 데이터셋뿐만 아니라 전체 데이터셋에 적용됩니다. 별도의 표시가 없는 한, 지속 시간은 밀리초(ms) 단위로, 파일 크기는 바이트(bytes) 단위로 측정됩니다.

이 리포지토리를 통해 파일 손상, 파티션 문제 등 데이터셋의 기술적인 문제에 대한 피드백을 제공할 수 있습니다. 질적 논의에 대한 더 확장된 토론은 Discourse에 참여해 주세요.

데이터셋 소개
이 데이터셋은 Common Voice 커뮤니티의 웹 플랫폼을 통해 기여받은 음성 데이터를 포함하고 있습니다. 새로운 데이터셋은 약 6개월마다 릴리스됩니다.

모든 음성 기여는 검증 상태와 관계없이 데이터셋의 일부로 릴리스됩니다. 사용자의 요청에 따라 클립이 제거되는 경우를 제외하고는 클립을 제거하지 않습니다. 클립은 Common Voice 번들링 도구를 사용하여 번들로 묶여 S3에 업로드됩니다.

다운로드된 .tar.gz 파일은 다음과 같은 구조를 가집니다. 여기서 [lang]는 해당 언어의 ISO 639-1 코드를 나타냅니다:

csharp
코드 복사
[lang].tar.gz/
├── clips/
│   ├── *.mp3 files
|__ dev.tsv
|__ invalidated.tsv
|__ other.tsv
|__ test.tsv
|__ train.tsv
|__ validated.tsv
|__ reported.tsv (as of Corpus 5.0)
각 .tsv 파일은 클립에 대한 파일 목록, 해당 클립의 주석(원본 소스 문장), 해시된 client_id, 검증 데이터 및 관련 인구 통계 데이터를 포함합니다. 특정 언어에 고유 발화자가 5명 미만일 경우, 개인정보 보호를 위해 인구 통계 데이터는 제거됩니다.

validated: 두 번 이상의 검증을 받은 클립 중 up_votes가 down_votes보다 많은 클립 목록
invalidated: 두 번 이상의 검증을 받은 클립 중 down_votes가 up_votes보다 많거나, down_votes와 up_votes가 같은 경우 세 번 이상의 검증을 받은 클립 목록
other: 상태를 결정하기에 충분한 검증을 받지 못한 클립 목록
Corpus 5.0부터는 각 언어의 기여자들이 소스 문장의 품질 관리를 더 잘 할 수 있도록 요청한 문장 목록을 게시하고 있습니다.

필드
각 tsv 파일의 각 행은 단일 오디오 클립을 나타내며, 다음 정보를 포함합니다:

client_id: 사용자의 해시된 UUID
path: 오디오 파일의 상대 경로
text: 오디오의 예상 전사(텍스트)
up_votes: 오디오가 텍스트와 일치한다고 평가한 사람 수
down_votes: 오디오가 텍스트와 일치하지 않는다고 평가한 사람 수
age: 화자의 연령대*
gender: 화자의 성별*
accent: 화자의 악센트*
segment: 문장이 커스텀 데이터셋 세그먼트에 속하는 경우 해당 세그먼트
나이, 성별, 악센트 옵션의 전체 목록은 인구 통계 사양에서 확인할 수 있습니다. 이는 화자가 해당 정보를 제공하도록 선택한 경우에만 보고됩니다.
머신러닝을 위한 사용
Mozilla Corpora Creator 도구를 사용하여 메타데이터를 파싱하고 테스트, 학습, 개발 세트를 생성합니다. Corpora Creator는 클립 중복을 제거하고 화자 다양성을 극대화합니다.

각 테스트/학습/개발 세트는 비결정적으로 생성되며, 이는 릴리스마다 다를 수 있습니다. 이는 각 후속 세트에서 인구 통계적 편향을 재생산하고 영속화하는 것을 피하기 위한 것입니다.

데이터셋 접근
HTTP를 통해 큰 파일(> 1-2 GB)을 다운로드하는 것은 이상적이지 않다는 것을 알고 있으며, 연구자와 개발자가 우리의 코퍼스를 더 쉽게 사용할 수 있도록 데이터셋 접근 메커니즘을 개선하고 있습니다. 그동안 다운로드가 중단되는 경우 커맨드 라인에서 curl을 사용하여 -C 옵션으로 중단된 다운로드를 재개하는 것을 권장합니다. curl 사용 방법에 대한 자세한 내용은 man 페이지 문서를 참조하세요.

인용
데이터를 학술 연구에 사용한 경우 다음 기사를 인용해 주시기 바랍니다:

Ardila, R., Branson, M., Davis, K., Henretty, M., Kohler, M., Meyer, J., Morais, R., Saunders, L., Tyers, F. M. and Weber, G. (2020) "Common Voice: A Massively-Multilingual Speech Corpus". Proceedings of the 12th Conference on Language Resources and Evaluation (LREC 2020). pp. 4211—4215

BibTex는 다음과 같습니다:

plaintext
코드 복사
@inproceedings{commonvoice2020,
  author    = {Ruben Ardila and
               Megan Branson and
               Kelly Davis and
               Michael Henretty and
               Moon Kohler and
               Josh Meyer and
               Reuben Morais and
               Lindsay Saunders and
               Francis M. Tyers and
               Gregor Weber},
  title     = {Common Voice: A Massively-Multilingual Speech Corpus},
  booktitle = {Proceedings of The 12th Language Resources and Evaluation Conference, {LREC} 2020},
  pages     = {4211--4215},
  publisher = {European Language Resources Association},
  year      = {2020}
}