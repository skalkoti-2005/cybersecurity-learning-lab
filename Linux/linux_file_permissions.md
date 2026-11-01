# Linux File Permissions

## Objective
To understand how Linux controls access to files and directories using permissions.

## What are Linux File Permissions?
Linux file permissions determine who can read, write, or execute a file.

## Three Permission Types

| Permission | Symbol | Meaning |
|---|---|---|
| Read | r | View file contents |
| Write | w | Modify file contents |
| Execute | x | Run a file as a program |

## Three User Categories
- User (u) – File owner.
- Group (g) – Users belonging to the file's group.
- Others (o) – All other users.

## Important Commands

| Command | Purpose |
|---|---|
| `ls -l` | Displays file permissions |
| `chmod` | Changes file permissions |
| `chown` | Changes file ownership |
| `umask` | Sets default permission restrictions |

## Example
touch sample.txt
ls -l sample.txt
chmod 644 sample.txt
ls -l sample.txt

The permission `644` means:
- Owner: Read and write.
- Group: Read only.
- Others: Read only.

## Learning Outcomes
- Understanding Linux permissions.
- Identifying file owners and groups.
- Learning how to view and modify permissions.
- Understanding access control.

## Result
Learned the basics of Linux file permissions and access control.

