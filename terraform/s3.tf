resource "aws_s3_bucket" "test-bucket" {
  bucket = "my-tf-test-bucket-musicboxd"
  acl    = "public-read"

website {
    index_document = "index.html"
    error_document = "error.html"
    routing_rules = <<EOF
[{
    "Condition": {
        "KeyPrefixEquals": "docs/"
    },
    "Redirect": {
        "ReplaceKeyPrefixWith": "documents/"
    }
}]
EOF

}
  tags = {
    Name        = "musicboxd"
    Environment = "Dev"
  }
  versioning {
    enabled = true
  }

}

resource "aws_s3_bucket" "athena_bucket" {
  bucket = "athena-bucket-csvs-musicboxd"
  acl    = "private"

  tags = {
    Name        = "My bucket"
    Environment = "musicboxd"
  }
}

resource "aws_s3_bucket_object" "csv_files" {
  for_each = fileset("bucket_files", "*")
  bucket = aws_s3_bucket.athena_bucket.id
  key    = each.value
  source = "bucket_files/${each.value}"

  etag = filemd5("bucket_files/${each.value}")
}
