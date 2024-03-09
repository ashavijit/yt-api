provider "aws" {
  region = "ap-southeast-1"
}

resource "aws_instance" "fampay-assignment" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = "aviral"
}

resource "aws_security_group" "fampay-security-group" {
  name        = "example-security-group"
  description = "Allow HTTP inbound traffic"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group_rule" "custom-ssh" {
  type        = "ingress"
  from_port   = 22
  to_port     = 22
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
  security_group_id = aws_security_group.example.id
}

resource "aws_security_group_rule" "allow_http" {
  type        = "ingress"
  from_port   = 80
  to_port     = 80
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
  security_group_id = aws_security_group.example.id
}

provisioner "remote-exec" {
  inline = [
    "sudo yum update -y",
    "sudo yum install -y git",
    "git clone https://github.com/yourusername/your-repo.git",
    
  ]

  connection {
    type     = "ssh"
    user     = "ec2-user"
    private_key = file("/path/to/your/key.pem")
    host     = aws_instance.example.public_ip
  }
}
