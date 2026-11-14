---
title: "Using Terraform to automate the creation and deprovisioning of AWS Member Accounts"
date: "2021-08-06"
slug: "leaving-aws-subaccounts-behind"
categories: []
tags: []
abstract: "Using Terraform to automate AWS member accounts for developers and dealing with off-boarding those team members can be hindered by the inability to easily delete member accounts. I show we separate the off-boarding of team members from the need to delete member accounts to make this simple and automatic."
original_urls: ["https://cromwellhaus.com/leaving-aws-subaccounts-behind"]
redirect_from: ["/leaving-aws-subaccounts-behind"]
contentful_id: "5iKEnYgpVkq0ovIyOf9yra"
permalink: "/2021/08/leaving-aws-subaccounts-behind/"
---

We [automate provisioning developer AWS sandbox accounts](https://github.com/sparkbox/aws-infrastructure/tree/main/modules/development-team) for our team at Sparkbox. These accounts are paid for by the parent organization. This gives our team full access to learn and prototype with all of AWS' services. We use Billing threshold notifications to keep things from spinning out of control.

It's relatively easy to create the organizations, users, and AWS accounts. The code fits in a nice module. The challenge we face comes when a team member leaves. When they leave, we need to quickly remove access to Sparkbox resources per our security policy.

Terraform makes this seeming simple:

1. [Remove the user from teammembers.auto.tfvars](https://github.com/sparkbox/aws-infrastructure/commit/6ace68ae4fce1f76e45769c3de6d5a8fbd8f9a71#diff-4b9b83568bdde9f27a3f6763676955c22280a5a7bb9fde8a1ca9e17212b73506).
2. Push the commit to Github
3. [Terraform Cloud](https://www.terraform.io/cloud) kicks off a new run, planing and auto applying the changes necessary

Simple! User, policies, login profile, etc are all destroyed.

**Remove Access to Sandbox Accounts**

Unfortunately, [consolidated billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) throws a wrench in the situation. Deleting an account really just removes it from the organization. To do this, the account must have a payment method configured. This isn't an option to automate.

Our goal is to remove former team members' access to Sparkbox resources. Our Terraform automation was conflating this with deleting their accounts. It's reasonable think that, but not necessary. So instead, we'll separate the concepts of *enabled users that should have access* from *all users that we have created accounts* in our Terraform code:

```hcl
locals {
  enabled_user_names = [
    for user in var.users : user.name
    if user.is_enabled
  ]
  all_user_names = toset([
    for user in var.users : user.name
  ])
}
```

Now we can use these individually local variables for their unique purposes:

[*Users that should exist:*](https://github.com/sparkbox/aws-infrastructure/blob/24e4796315876292b4562bd2aa39efc6d85771a7/modules/development-team/main.tf#L46-L50)

```hcl
resource "aws_iam_user" "user" {
  for_each = toset(local.enabled_user_names)
  name = each.value
}
```

[*Accounts that should exist:*](https://github.com/sparkbox/aws-infrastructure/blob/24e4796315876292b4562bd2aa39efc6d85771a7/modules/development-team/main.tf#L59-L66)

```hcl
resource "aws_organizations_account" "account" {
  for_each  = local.all_user_names
  name      = "Dev Sandbox ${each.value}"
  email     = "${each.value}@heysparkbox.com"
  role_name = "Administrator"
  parent_id = aws_organizations_organizational_unit.dev_team_ou.id
}
```

![Terraform Cloud run showing the planning and apply of a team member being removed from AWS infrastructure.](/images/contentful/1BPX0t7CimxM9AetetXujM-image.png)

With this setup, former Sparkboxers no longer have accounts, login profiles, or any access to Sparkbox resources. We can still gain access to their sub account for whatever purpose we might have. And, if we choose, [remove and delete the member account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html).
