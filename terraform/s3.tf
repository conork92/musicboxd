resource "aws_s3_bucket" "host" {
  bucket = "s3-website-test.hashicorp.com"
  acl    = "public-read"
  policy = file("policies/s3-policy.json")

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
}