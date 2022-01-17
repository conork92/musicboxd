resource "aws_elb" "main" {
  name               = "musicboxd-terraform-elb"
  availability_zones = ["eu-west-1c"]

  listener {
    instance_port     = 80
    instance_protocol = "http"
    lb_port           = 80
    lb_protocol       = "http"
  }
}

resource "aws_route53_record" "www" {
  zone_id = aws_route53_zone.primary.zone_id
  name    = "www.musicboxd.co.uk"
  type    = "A"

  alias {
    name                   = aws_elb.main.dns_name
    zone_id                = aws_elb.main.zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_zone" "primary" {
  name = "musicboxd.co.uk"
}