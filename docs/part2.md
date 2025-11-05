# Lab 1: AWS Development Environment and S3 Website Hosting

> Note: In the Learner Lab environment, the **LabIDEURL** and **LabIDEPassword** are not available in the Details panel. You will complete this activity using **Lab 2.1: Exploring AWS CloudShell and an IDE**. Start the lab and proceed with the steps below.
## Purpose
> In this lab, you will explore AWS CloudShell and Visual Studio Code IDE (code-server), host a static website using Amazon S3 and explore IAM roles and permissions.

**ℹ️Important:** After completing the lab, remember to delete all created resources to avoid incurring unnecessary charges.

## Step-by-step guide for student

### Step 1: Ensure that you have studied Module 1: Foundations of Cloud Developing (from canvas) properly

<details>
  <summary>👉Click to expand the step by step guide</summary>


To complete this lab, you will need to set up the following AWS services. It is important that you have studied Module 1 and is familiar with these services.

- AWS CloudShell
- Visual Studio Code IDE (code-server)
- Amazon Simple Storage Service (S3)
- AWS Identity and Access Management (IAM)
</details>

### Step 2: Lab Tasks 

#### Task 1: Exploring AWS CloudShell and VS Code IDE

> You will explore AWS CloudShell and connect to a Visual Studio Code IDE environment. You will run AWS CLI commands, create a Python script using the AWS SDK (Boto3), and transfer files between S3, CloudShell, and the IDE. The guide below uses Amazon Linux; ***if you choose Ubuntu, you need to use the equivalent commands***. 

<details>
  <summary>👉Click to expand the Task 1 Guide</summary>

### 1: Access AWS CloudShell

1. In the AWS Management Console, choose the **CloudShell** icon at the top.
2. Wait for the shell to initialize.
3. Run the following command to check the AWS CLI version:
   ```bash
   aws --version
   ```
   **Expected output:**
   ```
   aws-cli/2.15.x Python/3.11.x Linux/5.10.x botocore/2.15.x
   ```

4. List all S3 buckets:
   ```bash
   aws s3 ls
   ```
   **Expected output:**

   ```
   2024-05-12 10:15:43 example-sample-bucket-123456
   ```

   **Create a bucket using your own name, which will be used for this task.**
   
   > Use the command below, replacing ```<your-unique-bucket-name>``` with a bucket name that includes your own name, and update the region as needed.

  ```
   aws s3api create-bucket --bucket <your-unique-bucket-name> --region us-east-1
  ```
**Once created, run aws s3 ls again to verify it appears in the list:**

 ```
   aws s3 ls
  ```

### 2. Create and run a Python script using Boto3
1. In CloudShell, create a file named `list-buckets.py`:
   ```bash
   nano list-buckets.py
   ```
   Add the following code:
   ```python
   import boto3
   session = boto3.Session()
   s3_client = session.client('s3')
   b = s3_client.list_buckets()
   for item in b['Buckets']:
       print(item['Name'])
   ```
2. Run the script:
   ```bash
   python3 list-buckets.py
   ```
   **Expected output:**
   ```
   example-sample-bucket-123456
   ```

3. Upload the script to your S3 bucket:
   ```bash
   aws s3 cp list-buckets.py s3://example-sample-bucket-123456
   ```
   **Expected output:**
   ```
   upload: ./list-buckets.py to s3://example-sample-bucket-123456/list-buckets.py
   ```
4. List the contents of your bucket:
> The file list-buckets.py was created locally in your CloudShell environment and then uploaded as an object to your S3 bucket. To confirm that the upload succeeded, list the contents of your bucket:
```bash
   aws s3 ls s3://example-sample-bucket-123456
   ```
   **Expected output:**
   ```
 2025-11-03 11:42:10 215 list-buckets.py
   ```

### 3. Launch VS Code IDE
1. From the **AWS Details** panel where you started the lab, copy:
   - `LabIDEURL`
   - `LabIDEPassword`
2. Open the URL in a new tab, enter the password, and sign in.
3. Observe:
   - Left: File Explorer  
   - Bottom: Bash Terminal  

### 4. Copy files from S3 and run code in VS Code IDE
1. In the terminal:
   ```bash
   aws s3 ls
   aws s3 cp s3://example-sample-bucket-123456/list-buckets.py .
   ```
   Confirm that `list-buckets.py` appears in the Explorer.

2. Run the file:
   ```bash
   python3 list-buckets.py
   ```
   **Expected error:Please note that if you do not receive any error message, skip "3. Install Boto3" and proceed to 4. Otherwise, follow the instructions in step 3.** 
   ```
   ModuleNotFoundError: No module named 'boto3'
   ```

3. Install Boto3:
   ```bash
   sudo pip3 install boto3
   python3 list-buckets.py
   ```
   **Expected output:**
   ```
   example-sample-bucket-123456
   ```

4. Create a new HTML file:
   ```html
   <body>Hello World.</body>
   ```
   Save it as `index.html`.

5. Upload to S3:
   ```bash
   aws s3 cp index.html s3://example-sample-bucket-123456/index.html
   ```
   **Expected output:**
   ```
   upload: ./index.html to s3://example-sample-bucket-123456/index.html
   ```

---

### Submission: Required Screenshots for Task 1
* **T1.1:** Bucket list shown from CloudShell
* **T1.2:** VS Code IDE with terminal and file explorer visible that includes index.html file. ***You can also create error.html if you wish but not mandatory.***


</details>

#### Task 2: Configure public access and test website updates

> You will continue working with the same S3 bucket created in Task 1.In this section, you will enable **static website hosting**, configure **public access** with a **bucket policy**, test the website endpoint from the **AWS Management Console** and make a simple update to the `index.html` file.

<details>
  <summary>👉Click to expand the Task 2 Guide</summary>

### 1. Verify website files exist

If you already uploaded `index.html` in Task 1, skip this part of the task.

```bash
# Set your variables
REGION=us-east-1
BUCKET=<your-bucket-name>

# (Only if needed) Create simple index and error pages
echo '<!doctype html><html><body><h1>Welcome to the Café</h1></body></html>' > index.html
echo '<!doctype html><html><body><h1>Oops!</h1><p>Error page.</p></body></html>' > error.html

# Upload (or re-upload) to your bucket
aws s3 cp index.html s3://$BUCKET/index.html
aws s3 cp error.html s3://$BUCKET/error.html
```

**Expected output**

```
upload: ./index.html to s3://<your-bucket-name>/index.html
upload: ./error.html to s3://<your-bucket-name>/error.html
```

---

### 2. Enable static website hosting (Console)

1. Open the AWS Management Console → **S3 → Buckets → <your-bucket-name> → Properties**
2. Scroll to **Static website hosting** and choose **Edit**
3. Select **Enable**

   * **Index document:** `index.html`
   * **Error document:** `error.html`
4. Choose **Save changes**
---

### 3. Configure public access

> By default, S3 buckets block all public access. You must disable that restriction at the bucket level.

1. Go to **S3 → Buckets → <your-bucket-name> → Permissions**
2. Under **Block public access (bucket settings)** choose **Edit**
3. **Uncheck** “Block all public access” (you can leave ACL blocks on)
4. Type `confirm` and choose **Save changes**

---
### 4. Apply a bucket policy for public read

> Apply a public-read bucket policy using the **AWS Management Console**.

1. Go to **S3 → Buckets → <your-bucket-name> → Permissions**.
2. Scroll down to **Bucket policy** and choose **Edit**.
3. In the policy editor, paste the following JSON (replace `<your-bucket-name>` with your actual bucket name):

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "PublicReadForWebsite",
         "Effect": "Allow",
         "Principal": "*",
         "Action": ["s3:GetObject"],
         "Resource": "arn:aws:s3:::<your-bucket-name>/*"
       }
     ]
   }
   ```
4. Choose **Save changes**.
5. Review the permissions warning and choose **Confirm**.

---

### 5. Test the website endpoint

1. Console → **S3 → Buckets → <your-bucket-name> → Properties**
2. Scroll to **Static website hosting**
3. Copy the **Bucket website endpoint**, for example:

   ```
   http://<your-bucket-name>.s3-website-us-east-1.amazonaws.com
   ```
4. Open that URL in a new browser tab, you should see your web page.

If you receive **AccessDenied**, confirm:

* Static website hosting is **enabled**
* Bucket policy contains the correct bucket name and `/*`
* “Block all public access” is **unchecked**

### 6. Edit and re-upload `index.html`

Make a small change to your homepage (index.html) and upload the new version to S3.

```bash
# Edit in the IDE editor, then save the file.

# Upload the modified file to S3
aws s3 cp index.html s3://$BUCKET/index.html
```

**Expected output**

```
upload: ./index.html to s3://<your-bucket-name>/index.html
```

Refresh your browser at the **Bucket website endpoint**. Now you should now see the updated page.

> Note: In a real-world setup, you can automate this upload process using tools like `aws s3 sync` or IDE plugins that automatically deploy changes to S3 whenever you save your code. For this lab, we demonstrate it manually, but automation helps you focus on writing and testing your code instead of copying files manually.

---

### Submission: Required Screenshots for Task 2

* **T2.1:** Bucket Permissions → Bucket policy JSON
* **T2.2:** Website open in browser (via Bucket website endpoint)
* **T2.3:** Website showing updated heading after re-upload
---

</details>

#### Task 3: Exploring IAM Roles and Policies

> In this task, you will explore **AWS Identity and Access Management (IAM)** to understand how permissions and roles relate to the work you did in previous tasks. You will review existing IAM roles, policies, and users in the **lab environment**, observe their trust relationships, and understand how IAM integrates with the S3 website. Some IAM actions might be restricted in this environment therefore you need to focus on observation and understanding rather than creation.

<details>
  <summary>👉Click to expand the Task 3 Guide</summary>

### 1. Explore IAM in the Console

1. From the AWS Management Console, search for **IAM** and open the **IAM Dashboard**.
2. Observe the key sections on the left navigation pane:

   * **Users**: represent individuals or applications with credentials
   * **Roles**: grant temporary permissions to AWS services (for example, an EC2 instance accessing S3)
   * **Policies**: define what actions are allowed or denied

---

### 2. View existing roles

1. In the left menu, choose **Roles**.
2. Look for existing roles such as `EMR_EC2_DefaultRole` or `EC2RoleForLabInstance` (names may vary).
3. Click on one of these roles to open its details and review them.

> In your earlier tasks, the S3 operations you performed in CloudShell and the IDE worked because your lab session already has an IAM role with sufficient permissions.

---

### 3. Review a managed policy

1. In the IAM console, choose **Policies** from the left menu.
2. Search for the policy **AmazonS3ReadOnlyAccess**.
3. Choose the policy name to view its **JSON** permissions.
4. Observe how it defines specific allowed actions and resources, for example:

```json
   {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:Get*",
                "s3:List*",
                "s3:Describe*",
                "s3-object-lambda:Get*",
                "s3-object-lambda:List*"
            ],
            "Resource": "*"
        }
    ]
}

```

>  Policies like these control which S3 actions are possible. If your IAM role didn’t include a policy that allows `s3:PutObject`, your uploads in Task 1 and Task 2 would have failed.

### 5. How IAM connects with Tasks 1 and 2 that you did above?

* The **role you used in CloudShell/IDE** determined your ability to list, create, and modify S3 buckets.
* If your IAM permissions were limited (for example, read-only access), `aws s3 cp` or `aws s3 mb` commands would have failed.
* In real deployments, developers assign **EC2 IAM roles** so that applications running on EC2 can interact securely with S3 instead of embedding credentials in the code.

### Submission: Required Screenshots for Task 3

* **T3.1:** IAM console showing Roles list
* **T3.2:** Role details page with attached policies
* **T3.3:** Managed policy JSON (e.g., AmazonS3ReadOnlyAccess)

</details>

### Guidance and feedback
Guidance is available during the online consultation session or via Teams call.

### Evaluation
The evaluation is done based on the number of successfully completed tasks. Check the rubric.  

### Schedule and timing
Check the deadline in Canvas

### Submission
- **Document Submission:** Compile the required screenshots (as outlined at the end of each task) into a single Word document. Ensure each screenshot is clearly labeled to indicate which task it represents. ***Upload the word document to canvas.***
- **Self assessment:** In the submission comment box, provide a self-assessment based on the rubric guide. Clearly state how many points you believe you have earned for this task.  

### Clean Up 
- ℹ️ **Delete All Resources:** After completing the lab, be sure to delete all resources from the lab environment to avoid incurring unnecessary charges. Remember that you’ll need these credits for other lab tasks, so use them wisely. 