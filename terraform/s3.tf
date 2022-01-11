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