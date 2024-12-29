# 강의에 사용한 AWS CLI 및 IAM 정책 설정 모음

```bash
aws ec2 describe-instances --region us-east-1

aws --version

aws ec2 describe-instances --query 'Reservations[*].Instances[*].{Name: Tags[?Key==`Name`].Value | [0], State: State.Name}' --output table
```

```yaml
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowDescribe",
      "Effect": "Allow",
      "Action": [
        "ec2:Describe*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowAllEC2ActionsOnSpecificResources",
      "Effect": "Allow",
      "Action": "ec2:*",
      "Resource": [
        "arn:aws:ec2:us-east-1:<수강생 여러분의 ID>:instance/<생성한 인스턴스 ID>",
        "arn:aws:ec2:us-east-1:<수강생 여러분의 ID>:volume/*",
        "arn:aws:ec2:us-east-1:<수강생 여러분의 ID>:network-interface/*",
        "arn:aws:ec2:us-east-1:<수강생 여러분의 ID>:snapshot/*"
      ]
    }
  ]
}

``` 