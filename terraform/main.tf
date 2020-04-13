resource "aws_s3_bucket" "raw_yahoo_bucket" {
	bucket = "${var.bucket_name}"

	tags = {
		Environment = "${var.environment}"
		Service = "Yahoofinance"
		Type = "Data Lake Storage"
	}
} 