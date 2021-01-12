
mkdir tmp
reviews="$1"
jq '.reviews | .[].text' $reviews | sed 's/\\n//g' > tmp/tmp_text
jq '.reviews | .[].business_id' $reviews > tmp/tmp_business
paste tmp/tmp_text tmp/tmp_business | sort -u > "$2"
rm -rf tmp