kind: pipeline
type: docker
name: Testing Python CI/CD


steps:
- name: Black Code Format Check
  image: netw0rkaut0mati0n/netauto
  commands:
  - black . --check

trigger:
  event:
    exclude:
    - pull_request
