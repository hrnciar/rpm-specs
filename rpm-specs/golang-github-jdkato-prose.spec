# Generated by go2rpm
%bcond_without check

# https://github.com/jdkato/prose
%global goipath         github.com/jdkato/prose
Version:                1.1.1

%gometa

%global common_description %{expand:
Prose is a natural language processing library (English only) in pure Go. It
supports tokenization, segmentation, part-of-speech tagging, and named-entity
extraction.}

%global golicenses      LICENSE
%global godocs          AUTHORS.md README.md requirements.txt

Name:           %{goname}
Release:        2%{?dist}
Summary:        Golang library for text processing

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/montanaflynn/stats)
BuildRequires:  golang(github.com/shogo82148/go-shuffle)
BuildRequires:  golang(github.com/urfave/cli)
BuildRequires:  golang(gopkg.in/neurosnap/sentences.v1)
BuildRequires:  golang(gopkg.in/neurosnap/sentences.v1/data)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

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
%doc AUTHORS.md README.md requirements.txt
%{_bindir}/*

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 17:24:47 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-2
- Update to new macros

* Sat Feb 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest tagged version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20170911git2f94c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20170911git2f94c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20170911git2f94c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0-0.5.20170911git2f94c80
- Update revision
- Remove line changing test data files permissions

* Mon Sep 11 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0-0.4.20170806gita678fc7
- Remove Executable flag from test data files
- Fix binary file path in %%files section

* Fri Sep 08 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0-0.3.20170806gita678fc7
- Remove patch for gopkg.in dependencies. neurosnap/sentences ships both namespaces

* Fri Aug 18 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0-0.2.20170806gita678fc7
- Add missing neurosnap/sentences dependency
- Patch sources to depend on github neurosnap/sentences instead of gopkg.in releases

* Fri Aug 11 2017 Athos Ribeiro <athoscr@fedoraproject.org> - 0-0.1.20170806gita678fc7
- First package for Fedora

