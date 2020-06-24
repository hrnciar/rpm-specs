# Generated by go2rpm
%bcond_without check

# https://github.com/ryszard/goskiplist
%global goipath         github.com/ryszard/goskiplist
%global commit          2dfbae5fcf46374f166f8969cb07e167f1be6273

%gometa

%global common_description %{expand:
This is a library implementing skip lists for the Go programming language.

Skip lists are a data structure that can be used in place of balanced trees.
Skip lists use probabilistic balancing rather than strictly enforced balancing
and as a result the algorithms for insertion and deletion in skip lists are
much simpler and significantly faster than equivalent algorithms for balanced
trees.

Skip lists were first described in Pugh, William (June 1990). "Skip lists: a
probabilistic alternative to balanced trees".
Communications of the ACM 33 (6): 668–676.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.markdown

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Skip list implementation in Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 17:29:44 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20190306git2dfbae5
- Update to new macros

* Sun Mar 03 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190306git2dfbae5
- First package for Fedora
