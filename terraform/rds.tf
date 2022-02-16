resource "aws_db_instance" "musicboxd" {
  allocated_storage    = 10
  engine               = "postgres"
  engine_version       = "14"
  instance_class       = "db.t3.micro"
  name                 = "musicboxd"
  username             = "foo"
  password             = "foobarbaz"
  skip_final_snapshot  = true
}
