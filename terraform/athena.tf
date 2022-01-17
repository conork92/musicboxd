resource "aws_athena_database" "musicboxd" {
  name   = "musicboxd"
  bucket = aws_s3_bucket.athena_bucket.id
}
