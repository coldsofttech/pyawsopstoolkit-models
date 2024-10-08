# pyawsopstoolkit_models

The **pyawsopstoolkit_models** provides a comprehensive collection of data model classes specifically designed for
various AWS Ops Toolkit packages. These models are meticulously crafted to align closely with AWS services and their
respective properties, ensuring seamless integration and optimal performance.

## Getting Started

Ready to supercharge your AWS operations? Let's get started with **pyawsopstoolkit_models**!

### Installation

Install **pyawsopstoolkit_models** via pip:

```bash
pip install pyawsopstoolkit_models
```

## Documentation

- [ec2](#ec2)
    - [security_group](#security_group)
- [iam](#iam)
    - [permissions_boundary](#permissions_boundary)
    - [role](#role)
    - [user](#user)

### ec2

The **pyawsopstoolkit_models.ec2** subpackage offers specialized data model classes tailored for the Elastic Compute
Cloud (EC2) of AWS (Amazon Web Services). These models facilitate the efficient handling and manipulation of EC2,
ensuring seamless integration and interaction.

#### security_group

##### IPPermission

A class representing the IP Permissions for an EC2 Security Group.

###### Constructors

- `IPPermission(from_port: int, to_port: int, ip_protocol: str, ip_ranges: Optional[list[IPRange]] = None, ipv6_ranges: Optional[list[IPv6Range]] = None, prefix_list_ids: Optional[list[PrefixListID]] = None, user_id_group_pairs: Optional[list[UserIDGroupPair]] = None) -> None`:
  Initializes a new **IPPermission** object with the specified parameters.

###### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **IPPermission** object.

###### Properties

- `from_port`: The starting port of an EC2 security group rule entry.
- `ip_protocol`: The IP protocol of an EC2 security group rule entry.
- `ip_ranges`: The list of IPv4 ranges for an EC2 security group rule entry.
- `ipv6_ranges`: The list of IPv6 ranges for an EC2 security group rule entry.
- `prefix_lists`: The list of prefix lists for an EC2 security group rule entry.
- `to_port`: The ending port of an EC2 security group rule entry.
- `user_id_group_pairs`: The list of user ID group pairs for an EC2 security group rule entry.

##### IPRange

A class representing an IPv4 range for an EC2 Security Group.

###### Constructors

- `IPRange(cidr_ip: str, description: Optional[str] = None) -> None`: Initializes a new **IPRange** object with the
  specified parameters.

###### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **IPRange** object.

###### Properties

- `cidr_ip`: The IPv4 CIDR range.
- `description`: The description of the IPv4 CIDR range.

##### IPv6Range

A class representing an IPv6 range for an EC2 Security Group.

###### Constructors

- `IPv6Range(cidr_ipv6: str, description: Optional[str] = None) -> None`: Initializes a new **IPv6Range** object with
  the specified parameters.

###### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **IPv6Range** object.

###### Properties

- `cidr_ipv6`: The IPv6 CIDR range.
- `description`: The description of the IPv6 CIDR range.

##### PrefixList

A class representing a Prefix List for an EC2 Security Group.

###### Constructors

- `PrefixList(id: str, description: Optional[str] = None) -> None`: Initializes a new **PrefixList** object with the
  specified parameters.

###### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **PrefixList** object.

###### Properties

- `id`: The unique identifier of the prefix list.
- `description`: The description of the prefix list.

##### SecurityGroup

A class representing an EC2 Security Group.

###### Constructors

- `SecurityGroup(id: str, name: str, owner_id: str, vpc_id: str, ip_permissions: Optional[list[IPPermission]] = None, ip_permissions_egress: Optional[list[IPPermission]] = None, description: Optional[str] = None, tags: Optional[list] = None, in_use: Optional[bool] = None) -> None`:
  Initializes a new **SecurityGroup** object with the specified parameters.

###### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **SecurityGroup** object.

###### Properties

- `description`: The description of the EC2 security group.
- `id`: The unique identifier of the EC2 security group.
- `in_use`: Flag to indicate if the EC2 security group is associated with any Elastic Network Interface (ENI).
- `ip_permissions_egress`: The list of outbound rule entries for the EC2 security group.
- `ip_permissions`: The list of inbound rule entries for the EC2 security group.
- `name`: The name of the EC2 security group.
- `owner_id`: The owner ID of the EC2 security group.
- `tags`: The tags associated with the EC2 security group.
- `vpc_id`: The VPC ID of the EC2 security group.

##### UserIDGroupPair

A class representing a User ID Group Pair for an EC2 Security Group.

###### Constructors

- `UserIDGroupPair(id: str, name: str, status: str, user_id: str, vpc_id: str, description: Optional[str] = None, vpc_peering_connection_id: Optional[str] = None) -> None`:
  Initializes a new **UserIDGroupPair** object with the specified parameters.

###### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **UserIDGroupPair** object.

###### Properties

- `description`: The description of the user ID group pair.
- `id`: The unique identifier of the user ID group pair.
- `name`: The name of the user ID group pair.
- `status`: The status of the user ID group pair.
- `user_id`: The owner/user ID of the user ID group pair.
- `vpc_id`: The VPC ID of the user ID group pair.
- `vpc_peering_connection_id`: The VPC peering connection ID of the user ID group pair.

### iam

The **pyawsopstoolkit_models.iam** subpackage offers specialized data model classes tailored for the Identity and Access
Management (IAM) service of AWS (Amazon Web Services). These models facilitate the efficient handling and manipulation
of IAM resources, ensuring seamless integration and interaction with AWS IAM functionalities.

#### permissions_boundary

##### PermissionsBoundary

A class representing an IAM role permissions boundary.

###### Constructors

- `PermissionsBoundary(type: str, arn: str) -> None`: Initializes a **PermissionsBoundary** object with the specified
  type and Amazon Resource Name (ARN).

###### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **PermissionsBoundary** object.

###### Properties

- `arn`: The Amazon Resource Name (ARN) of the permissions boundary.
- `type`: The type of the permissions boundary.

#### role

##### LastUsed

The **LastUsed** class encapsulates the information regarding the last time an IAM role was used.

###### Constructors

- `LastUsed(used_date: Optional[datetime] = None, region: Optional[str] = None) -> None`: Initializes a new **LastUsed**
  instance with optional parameters for the date and time the IAM role was last used and the AWS region where it was
  used.

###### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **LastUsed** object.

###### Properties

- `region`: The AWS region where the IAM role was last used.
- `used_date`: The last date and time the IAM role was used.

##### Role

The **Role** class represents an IAM role in AWS, encompassing various attributes and methods to manage the role
effectively.

###### Constructors

- `Role(account: IAccount, name: str, id: str, arn: str, max_session_duration: int, path: str = '/', created_date: Optional[datetime] = None, assume_role_policy_document: Optional[dict] = None, description: Optional[str] = None, permissions_boundary: Optional[PermissionsBoundary] = None, last_used: Optional[LastUsed] = None, tags: Optional[list] = None) -> None`:
  Initializes a new **Role** instance with comprehensive parameters to define the IAM role, including account details,
  role name, ID, ARN, session duration, path, creation date, assume role policy, description, permissions boundary, last
  used information, and associated tags.

###### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **Role** object.

###### Properties

- `account`: The AWS account associated with the IAM role.
- `arn`: The Amazon Resource Name (ARN) of the IAM role.
- `assume_role_policy_document`: The trust relationship or assume role policy document defining the permissions for
  assuming the IAM role.
- `created_date`: The created date of the IAM role.
- `description`: A brief description of the IAM role.
- `id`: The unique identifier of the IAM role.
- `last_used`: An instance of LastUsed representing the last time the IAM role was utilized.
- `max_session_duration`: The maximum duration (in seconds) for which the IAM role can be assumed in a single session.
- `name`: The name of the IAM role.
- `path`: The path under which the IAM role is created, useful for organizational purposes.
- `permissions_boundary`: An optional permissions boundary that defines the maximum permissions the IAM role can have.
- `tags`: A list of tags associated with the IAM role for categorization and identification purposes.

#### user

##### AccessKey

A class representing the access key information of an IAM user.

###### Constructors

- `AccessKey(id: str, status: str, created_date: Optional[datetime] = None, last_used_date: Optional[datetime] = None, last_used_service: Optional[str] = None, last_used_region: Optional[str] = None) -> None`:
  Initializes a new **AccessKey** object with the specified parameters.

###### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **AccessKey** object.

###### Properties

- `created_date`: The creation date of the IAM user access key.
- `id`: The unique identifier of the IAM user access key.
- `last_used_date`: The last usage date of the IAM user access key.
- `last_used_region`: The AWS region where the IAM user access key was last used.
- `last_used_service`: The AWS service where the IAM user access key was last used.
- `status`: The current status of the IAM user access key (e.g., Active, Inactive).

##### LoginProfile

A class representing the login profile information of an IAM user.

###### Constructors

- `LoginProfile(created_date: Optional[datetime] = None, password_reset_required: Optional[bool] = False) -> None`:
  Initializes a new **LoginProfile** object with the specified parameters.

###### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **LoginProfile** object.

###### Properties

- `created_date`: The creation date of the IAM user login profile.
- `password_reset_required`: Indicates whether a password reset is required for the IAM user.

##### User

A class representing an IAM user.

###### Constructors

- `User(account: IAccount, name: str, id: str, arn: str, path: str = '/', created_date: Optional[datetime] = None, password_last_used_date: Optional[datetime] = None, permissions_boundary: Optional[PermissionsBoundary] = None, login_profile: Optional[LoginProfile] = None, access_keys: Optional[list[AccessKey]] = None, tags: Optional[list] = None) -> None`:
  Initializes a new **User** object with the specified parameters.

###### Methods

- `to_dict() -> dict`: Returns a dictionary representation of the **User** object.

###### Properties

- `access_keys`: A list of access keys associated with the IAM user.
- `account`: The AWS account associated with the IAM user.
- `arn`: The Amazon Resource Name (ARN) of the IAM user.
- `created_date`: The creation date of the IAM user.
- `id`: The unique ID of the IAM user.
- `login_profile`: The login profile associated with the IAM user.
- `name`: The name of the IAM user.
- `password_last_used_date`: The last date the IAM user's password was used.
- `path`: The path of the IAM user within the AWS IAM hierarchy.
- `permissions_boundary`: The permissions boundary associated with the IAM user.
- `tags`: A list of tags associated with the IAM user, useful for organization and management purposes.

# License

Please refer to the [MIT License](LICENSE) within the project for more information.

# Contributing

We welcome contributions from the community! Whether you have ideas for new features, bug fixes, or enhancements, feel
free to open an issue or submit a pull request on [GitHub](https://github.com/coldsofttech/pyawsopstoolkit-models).