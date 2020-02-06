resource "aws_s3_bucket" "raw_yahoo_bucket" {
	bucket = "pdl-yahoofinance"

	tags = {
		Environment = "Dev"
		Service = "Yahoofinance"
		Type = "Data Lake Storage"
	}
} 