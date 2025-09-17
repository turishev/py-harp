(let ((dd (expand-file-name default-directory)))
  (message "proj-dir:%s" dd)

  (setenv "PYTHONPATH"
	  (concat dd
		  "src/pyharp"
		  ":"
		  dd
		  "tests"))

  (message "env:%s" (getenv "PYTHONPATH"))

  (message "proj-dir (2):%s" dd)
  )

(compile-target-mode 1)
(compile-target-add "tests" "pytest")
(compile-target-add "pyharp" "src/pyharp/pyharp")

(find-file "src/pyharp/pyharp.py")
