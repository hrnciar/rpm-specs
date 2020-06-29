# Generated by go2rpm 1
%bcond_without check

# https://github.com/elves/elvish
%global goipath         github.com/elves/elvish
Version:                0.13.1

%gometa

%global common_description %{expand:
Friendly Interactive Shell and Expressive Programming Language.}

%global golicenses      LICENSE
%global godocs          README.md CONTRIBUTING.md website/README.md\\\
                        website/home.md website/_ttyshot/README.md\\\
                        website/get/prelude.md website/ref/name.md\\\
                        website/ref/builtin.md website/ref/bundled.md\\\
                        website/ref/store.md website/ref/re.md\\\
                        website/ref/philosophy.md website/ref/prelude.md\\\
                        website/ref/epm.md website/ref/edit.md\\\
                        website/ref/language.md website/blog/newsletter-\\\
                        july-2017.md website/blog/0.11-release-notes.md\\\
                        website/blog/0.12-release-notes.md\\\
                        website/blog/newsletter-sep-2017.md\\\
                        website/blog/0.10-release-notes.md\\\
                        website/blog/0.9-release-notes.md\\\
                        website/blog/live.md website/blog/0.13-release-\\\
                        notes.md website/learn/unique-semantics.md\\\
                        website/learn/cookbook.md\\\
                        website/learn/fundamentals.md\\\
                        website/learn/effective-elvish.md examples

Name:           %{goname}
Release:        1%{?dist}
Summary:        Friendly Interactive Shell and Expressive Programming Language

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/boltdb/bolt)
BuildRequires:  golang(github.com/xiaq/persistent/hash)
BuildRequires:  golang(github.com/xiaq/persistent/hashmap)
BuildRequires:  golang(github.com/xiaq/persistent/vector)
BuildRequires:  golang(golang.org/x/sys/unix)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/kr/pty)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
# gopkginstall wants to install some examples to docs
# and seems to expect them at repo_root/examples
mv cmd/examples examples
# These actually aren't commands for end users; and
# confuse gopkginstall here.
rm -rf cmd

%build
%gobuild -o %{gobuilddir}/bin/elvish %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md website/README.md website/home.md
%doc website/_ttyshot/README.md website/get/prelude.md website/ref/name.md
%doc website/ref/builtin.md website/ref/bundled.md website/ref/store.md
%doc website/ref/re.md website/ref/philosophy.md website/ref/prelude.md
%doc website/ref/epm.md website/ref/edit.md website/ref/language.md
%doc website/blog/newsletter-july-2017.md website/blog/0.11-release-notes.md
%doc website/blog/0.12-release-notes.md website/blog/newsletter-sep-2017.md
%doc website/blog/0.10-release-notes.md website/blog/0.9-release-notes.md
%doc website/blog/live.md website/blog/0.13-release-notes.md
%doc website/learn/unique-semantics.md website/learn/cookbook.md
%doc website/learn/fundamentals.md website/learn/effective-elvish.md examples
%{_bindir}/*
%gopkgfiles

%changelog
* Tue May 19 21:36:38 EDT 2020 Carson Black <uhhadd@gmail.com> - 0.13.1-1
- Initial package

