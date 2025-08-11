(message "proj-dir:%s" compile-target-project-directory)

(setenv "PYTHONPATH"
	(concat compile-target-project-directory
		"src/pyharp"
		":"
		compile-target-project-directory
		"tests"))

(message "env:%s" (getenv "PYTHONPATH"))

(compile-target-add "tests" "pytest")
(compile-target-add "pyharp" "src/pyharp/pyharp")
