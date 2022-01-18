resource "aws_s3_bucket" "test-bucket" {
  bucket = "my-tf-test-bucket-musicboxd"
  acl    = "public-read"
  policy = data.aws_iam_policy_document.allow_access_for_website.json
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

resource "aws_s3_bucket_object" "index" {
  bucket = aws_s3_bucket.test-bucket.id
  key    = "index.html"
  source = "../musicboxd/templates/index.html"
  content_type = "text/html"
  etag = filemd5("../musicboxd/templates/index.html")
}

data "aws_iam_policy_document" "allow_access_for_website" {
  statement {
    principals {
      type        = "*"
      identifiers = ["AWS"]
    }

    actions = [
      "s3:GetObject",
    ]

    resources = [
      "arn:aws:s3:::my-tf-test-bucket-musicboxd",
      "arn:aws:s3:::my-tf-test-bucket-musicboxd/*",
    ]
  }
}
