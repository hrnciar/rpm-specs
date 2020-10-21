# https://github.com/google/starlark-go
%global goipath             go.starlark.net
%global forgeurl            https://github.com/google/starlark-go

Version:                    0
%global commit              4379bb3f9ac0b7f6e21b1441663122a26f96be31

%gometa

%global common_description %{expand:
Starlark is a dialect of Python intended for use as a configuration language.
Like Python, it is an untyped dynamic language with high-level data types,
first-class functions with lexical scope, and garbage collection. Unlike
CPython, independent Starlark threads execute in parallel, so Starlark
workloads scale well on parallel machines. Starlark is a small and simple
language with a familiar and highly readable syntax. You can use it as an
expressive notation for structured data, defining functions to eliminate
repetition, or you can use it to add scripting capabilities to an existing
application.}

%global golicenses          LICENSE
%global godocs              *.md

%global gosupfiles      ${star[@]}

Name:                       %{goname}
Release:                    0.2%{?dist}
Summary:                    Dialect of Python intended for use as a configuration language

# A couple of test files are under the Apache License 2.0
License:                    BSD and ASL2.0
URL:                        %{gourl}
Source0:                    %{gosource}

BuildRequires:              golang(github.com/chzyer/logex)
BuildRequires:              golang(github.com/chzyer/readline)
BuildRequires:              golang(github.com/chzyer/test)

# The tests fail when using more than one path in the GOPATH
Patch0001:                  fix_tests.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0001 -p1

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
mapfile -t star <<< $(find . -name "*.star" -type f)
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%check
%gocheck

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Aug 17 14:27:43 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20190817git4379bb3
- Add star files

* Mon Jun 22 2020 Álex Sáez <asm@redhat.com> - 0-0.1.20190817git4379bb3
- First package for Fedora
