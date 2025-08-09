((nil . (
	 (eval . (progn
		   (message "dir-locals:%s" default-directory)
		   (compile-target-mode 1)
		   (setenv "PYTHONPATH" (concat (getenv "PYTHONPATH") ":./src/pyharp:./tests"))
		   t))
	 (compile-target-use-project-el t)
	 (compile-target-targets-list . ((name "pyharp" cmd "python3 src/pyharp.py")
					 (name "tests" cmd "pytest"))))))
