@echo off
cd /d "C:\Users\Admin\Documents\ProofOfPost\gitbook-proofofpost"

echo Removing .git directory...
rmdir /s /q .git

echo Initializing fresh git repository...
git init

echo Configuring git user...
git config user.name "CardanoTokenIO"
git config user.email "cardanotokenio@proofofpost.io"

echo Adding all files...
git add .

echo Creating initial commit...
git commit -m "Initial commit: Clean Proof of Post documentation with UTxO Maestro branding"

echo Adding remote origin...
git remote add origin https://github.com/CardanoTokenIO/ProoOfPost.git

echo Force pushing to GitHub...
git push -u origin master --force

echo Done! Git history has been reset.
pause
