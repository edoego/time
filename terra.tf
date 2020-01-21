provider "aws" {
  access_key = "AKIAJK5BYOC7ZRRBBIMA"
  secret_key = "s4mrTyfzMwkg1evvU0n4s32PMC6v6mmfgetT+QLM"
  region     = "us-east-2"
}

resource "aws_instance" "example" {
  ami           = "ami-02ccb28830b645a41"
  instance_type = "t2.micro"

  user_data = <<-EOF
		#!/bin/bash
		
		sudo yum update -y
		sudo yum install git -y
		git config --global user.name Edgar
		git config --global user.email edoego87@gmail.com
		git clone https://github.com/edoego/time.git
		aws configure set region us-east-2 --profile default
		aws configure set aws_access_key_id AKIAJK5BYOC7ZRRBBIMA
		aws configure set aws_secret_access_key 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
		aws sns publish --message file://time/unittestresult.txt --topic arn:aws:sns:us-east-2:539331081044:Unit_test_results
		aws ec2 modify-instance-attribute \
    			--instance-id $(curl -s http://169.254.169.254/latest/meta-data/instance-id) \
    			--instance-initiated-shutdown-behavior terminate
		echo "sudo halt" | at now + 1 minutes		
		EOF
}		


