((nil . (
	 (eval . (progn
		   (message "dir-locals:%s" default-directory)
		   (compile-target-mode 1)
		   t))
	 (compile-target-use-project-el t)
	 (compile-target-targets-list . ((name "pyharp" cmd "python3 src/pyharp.py"))))))
