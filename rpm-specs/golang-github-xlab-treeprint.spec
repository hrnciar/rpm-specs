# Generated by go2rpm
# https://github.com/xlab/treeprint/issues/10
%ifnarch %{ix86} %{arm}
%bcond_without check
%endif

# https://github.com/xlab/treeprint
%global goipath         github.com/xlab/treeprint
%global commit          a009c3971eca89777614839eb7f69abed3ea3959

%gometa

%global common_description %{expand:
Package Treeprint provides a simple ASCII tree composing tool.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Simple ASCII tree composing tool

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 15:04:03 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190625gita009c39
- Initial package
