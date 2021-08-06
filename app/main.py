from remediation.aws.iam.root_account_used_recently import apply

if __name__ == '__main__':
    # rule_executor.cloudtrail_rules()
    # rule_executor.async_cloudtrail_rules()
    apply('secops-test')
